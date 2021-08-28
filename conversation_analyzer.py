import os
import json
from analysis import print_convo_data
import argparse

# Arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--starts-after', type=str, nargs=1,
                    help='Starting date of conversation')
parser.add_argument('--query', type=str, nargs=1,
                    help='Starting date of conversation')
parser.add_argument('--similar', type=str, nargs=1,
                    help='Starting date of conversation')

args = parser.parse_args()

print('Arguments', args)
# Import, parse JSON, and store in working memory
file_data = []
for f in os.listdir('./'):
    if f.endswith('.json'):
        data = json.load(open(f, 'r'))
        file_data.append(data)
    else:
        continue

for fd in file_data:
    print_convo_data(fd) # TODO: Change to process and separate print portion


# import datetime
# dt_string = "2020-12-18 3:11:09" 
# format = "%Y-%m-%d %H:%M:%S"
# dt_object = datetime.datetime.strptime(dt_string, format)