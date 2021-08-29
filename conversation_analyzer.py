import os
import json
from analysis import Conversation
import argparse
from dates import date_from_args_string

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

# Arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--starts-after', type=str, nargs=1,
                    help='Starting date of conversation')
parser.add_argument('--query', type=str, nargs=1,
                    help='Exact query')
parser.add_argument('--similar', type=str, nargs=1,
                    help='Similar query')

args = parser.parse_args()
starts_after = date_from_args_string(args.starts_after[0]) if args.starts_after else None
query = args.query[0] if args.query else None
similar = args.similar[0] if args.similar else None

# Import, parse JSON, and store in working memory
file_data = []
for f in os.listdir('./'):
    if f.endswith('.json'):
        data = json.load(open(f, 'r'))
        file_data.append(data)
    else:
        continue

# Class instances from file data
conversations = []
for fd in file_data:
    conversations.append(Conversation(fd))

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

# TODO: Fuzzy one
     
for fc in filtered_conversations:
    print_convo_data(fc)
