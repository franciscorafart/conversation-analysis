import datetime
# dt_string = "2020-12-18 3:11:09" 
full_format = "%Y-%m-%dT%H:%M:%S"
args_format = "%Y-%m-%d"

def date_from_string(date_string):
    return datetime.datetime.strptime(date_string, full_format)

def date_from_args_string(date_string):
    return datetime.datetime.strptime(date_string, args_format)