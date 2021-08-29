import datetime

full_format = "%Y-%m-%dT%H:%M:%S"
args_format = "%Y-%m-%d"

def date_from_string(date_string):
    return datetime.datetime.strptime(date_string, full_format)

def date_from_args_string(date_string):
    return datetime.datetime.strptime(date_string, args_format)