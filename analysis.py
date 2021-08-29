
import random
import statistics
from dates import date_from_string

class Conversation:
    def __init__(self, conversation_file_data):
        self.title = conversation_file_data['title']
        self.data = self.speaker_data(conversation_file_data['snippets'])
        self.start_time = date_from_string(conversation_file_data['start_time'])
        self.query_coordinates = []

    def speaker_data(self, snippets):
        res = {}

        for _, s in snippets.items():
            speaker_name = s['speaker_name']

            if not res.get(speaker_name):
                res[speaker_name] = dict(
                    name = speaker_name,
                    num_words = 0,
                    duration = 0,
                    speaking_duration = 0, # Actual sound speaking time 
                    phrases = [],
                    facilitator = False,
                )

            current_count = res[speaker_name]['num_words']
            current_duration = res[speaker_name]['duration']
            current_speaking_duration = res[speaker_name]['speaking_duration']
            
            snippet_duration = s['audio_end_offset'] - s['audio_start_offset']
            facilitator = s['is_facilitator']
            # index_in_convo = s['index_in_conversation']
            words = s['words']

            text = ' '.join([w[0] for w in words])
            speaking_duration = sum([w[2] - w[1] for w in words])

            # Update
            res[speaker_name]['num_words'] = current_count + len(words)
            res[speaker_name]['duration'] = current_duration + snippet_duration
            res[speaker_name]['speaking_duration'] = current_speaking_duration + speaking_duration
            res[speaker_name]['phrases'].append(text)
            res[speaker_name]['facilitator'] = facilitator

        return res

    
    def print_convo_data(
        self, 
        starts_after=None,
        query=None,
        similar=None,
    ):
        if not starts_after or self.start_time > starts_after:
            speakers = self.data

            # evaluate query and similar here
            if query:
                query_cordinates = self.exact_comparator(query, speakers) if query else []

            print('query_cordinates', query_cordinates)

            print("============================================================")
            print(self.title)
            print("============================================================")

            for name, data in speakers.items():
                print(name)
                print('Num Words Spoken:', data['num_words'])
                print('Duration: ', int(data['duration']))
                print()

            print('Example Snippet')
            if query:
                print('query snippet')
            elif similar:
                print('similar snippet')
            else: 
                print(self.random_snippet(speakers), '...') # Random Snippets from non facilitators

            print('Health: ', self.health_analysis(speakers), '/ 3')

    def start_time(self):
        return self.start_time

    def random_snippet(self, speakers):
        names = [name for name, s in speakers.items() if not s['facilitator']]
        random_name = names[random.randint(0, len(names)-1)]
        random_speaker = speakers[random_name]
        phrases_for_snippet = [ph for ph in random_speaker['phrases'] if len(ph) > 80] # Minimum length for snippets
        
        # Run again if no phrases of minimum length
        if not phrases_for_snippet:
            return self.random_snippet(speakers)

        return phrases_for_snippet[random.randint(0, len(phrases_for_snippet)-1)]


    def health_analysis(self, speakers):
        speaker_data = [s for s in speakers.values() if not s['facilitator']]  # Do not consider moderator
        
        balanced = _balanced_conversation([s['duration'] for s in speaker_data])
        calmed = _calmed_conversation(speaker_data)
        fluent = _fluent_conversation(speakers.values())

        return balanced + calmed + fluent

    def exact_comparator(self, q, speakers):
        query_coordinates = []

        for name, data in speakers.items():
            for index_of_phrase, phrase in enumerate(data['phrases']):
                index_of_q = phrase.find(q)
                if index_of_q >= 0:
                    query_coordinates.append((name, index_of_phrase))

        return query_coordinates

    # TODO: Implement similar with Fuzzy search library 

# Evaluate the spread of speaking durations by calculating coefficient of variation
# Return 1 if the conversation is balanced, 0 if not
def _balanced_conversation(durations):
    coef_variation = statistics.stdev(durations) / statistics.mean(durations)
    return 1 if coef_variation < 0.6 else 0

# Evaluate the percentage of time speaking words vs. the time taken to speak
# I'm arbitrarily assigning a lower percentage as a more calm delivery
def _calmed_conversation(speaker_data):
    delivery_speed = statistics.mean([s['speaking_duration'] / s['duration'] for s in speaker_data])

    return 1 if delivery_speed < 0.75 else 0

# How much time facilitator takes vs total amount => More facilitator talks, less fluent conversation
# Threshold at 30%
def _fluent_conversation(speaker_data):
    total_duration = sum([sd['duration'] for sd in speaker_data])
    facilitator_duration = [sd['duration'] for sd in speaker_data if sd['facilitator']][0]

    facilitator_percentage = facilitator_duration / total_duration

    return 1 if facilitator_percentage < 0.3 else 0




