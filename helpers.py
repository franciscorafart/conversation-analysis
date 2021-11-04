import os
import json

def import_json_files(path):
    file_data = []

    for f in os.listdir(path):
        if f.endswith('.json'):
            data = json.load(open(path+f, 'r'))
            file_data.append(data)
        else:
            continue
    
    return file_data

def filter_conversations(
    conversations, 
    starts_after=None, 
    query=None, 
    similar=None
):
    filtered_conversations = []

    if starts_after:
        filtered_conversations = [c for c in conversations if c.start_time > starts_after]
    elif query:
        for c in conversations:
            if c.exact_comparator(query):
                filtered_conversations.append(c)
    elif similar:
        for c in conversations:
            if c.fuzzy_comparator(similar):
                filtered_conversations.append(c)
    else: 
        filtered_conversations = conversations

    return filtered_conversations

def print_convo_data(
    convo,
):
    speakers = convo.data

    print("============================================================")
    print(convo.title)
    print("============================================================")

    for name, data in speakers.items():
        print(name)
        print('Num Words Spoken:', data['num_words'])
        print('Duration: ', int(data['duration']))
        print()

    if convo.query_coordinates:
        name, idx = convo.query_coordinates[0] # First element that matches the query
        print(convo.data[name]['phrases'][idx])
    else: 
        print(convo.random_snippet(speakers), '...')

    print()
    print('Health: ', convo.health_analysis(speakers), '/ 3')