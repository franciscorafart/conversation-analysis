
import argparse
from conversation import Conversation
from dates import date_from_args_string
from helpers import filter_conversations, import_json_files, print_convo_data 

file_data = import_json_files('conversations/')
    
# Argument parsing
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

conversations = []
for fd in file_data:
    conversations.append(Conversation(fd))

filtered_conversations = filter_conversations(
    conversations, 
    starts_after,
    query,
    similar,
)
     
for fc in filtered_conversations:
    print_convo_data(fc)
