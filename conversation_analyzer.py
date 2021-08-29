import os
import json
from analysis import Conversation
import argparse
from dates import date_from_args_string

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

for c in conversations:
    c.print_convo_data(starts_after, query, similar)

