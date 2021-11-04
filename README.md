# Project: Analyze conversations in JSON files with Python (Take home assignment)

# Instructions
You are to write a Python command line program which prints some information about conversations.

For each conversation
Read in the conversation file and print out the title
Print a random snippet
Produce a summary for each Speaker in the conversation with:
Number of words spoken
Duration of time spoken
Print a “health metric” for the conversation. Interpret how you would like— examples might be if everyone speaks for roughly the same amount of time, how often there is silence, speech pace, amount of speech per speaker turn, etc.
Add at least one unit test
Take in a parameter --starts-after [date] which is a date string. If this parameter is passed in, return only the conversations that took place after the passed in date.
Take in a parameter --query [string] which returns only conversations that have the query string mentioned at some point. In addition, instead of a random snippet, return a snippet that contains the query match
Take in a parameter --similar [string] which, instead of a random snippet, returns the snippet most “similar” to the passed in string. Interpret “similar” however you would like. You can assume --query and --similar will be used independently.

An example output might look like:
============================================================ 
Resistance and Resiliency within the Asian American Community ============================================================
T. Marie 
Num words spoken: xxx 
Duration: yyy 

Rob 
Num words spoken: xxx 
Duration: yyy 
... [continued on next page]

Example snippet 
I almost hesitate to say this because I don't want this to come across as insensitive, but truthfully I'm not scared because I don't want to live my life in fear of this... 

Health metrics 
[something]: [grade]

============================================================ 
East Side Public Safety Forum - Group 3
============================================================
...

# Solution

## 1. Installation/running instructions

1. Extract the files 
2. In the extracted directory, setup virtual environment `$ python3 -m venv ./`
2. Activate the venv with `$ source bin/activate`
3. Install packages `$ pip install -r requirements.txt`
4. Run `$ python3 analysis.py` with arguments.
Example:
    `python3 analysis.py`
    `python3 analysis.py --starts-after 2020-10-22`
    `python3 analysis.py --query 'beginning'`
    `python3 analysis.py --similar 'the begining'` (With spelling error)

5. Run unit tests with `$ pytest tests`
6. Deactivate the environment when finished `$ deactivate`

## 2. How I approached the problem
My approach was to get the basic information parsed and printed at the beggining so I had results to show. After I figured that out I worked on implementing the more coplex fiunctionality such as date filtering, query, similar, and the snippet printing (random and query-based).

Explanation of health score:

For the Conversation Healh Score, I used 3 indicators that add up to a score:
    1. `balanced` - determines whether a conversation is balanced depending on the usage of time of the different people (except the moderator). I used the coefficient of variation and an arbitrary threshold of 0.6 to determine whether a conversation in balanced or not.
    2. `calmed` - compares the amount of time taken to speak with the actual time people speak words, as an indicator of how much time they take to deliver their message.
    3. `fluent` - evaluates the amount of time the facilator uses of the total, with the idea that a fluent conversation doesn't require the facilitator to intervene too much.

For the implementation of `similar`, I ended up using an external library (fuzzysearch), as implementing an efficient algorithm for this seemed very out of scope.

## 3. Problems I ran into
Finding a way of implementing the 'similar' was challengingg. I thought of a Trie structure to search for strings at the beginning, but then I realized it doesn't apply well because the text is not really a dictionary. I researched and found the fuzzy search library, that works in a reasonably fast fashion.

I also had some issues with getting pytest to find the external libraries I used. I had to uninstall the packages from my global env and reinstall them on venv.

## 4. Optimizations or changes I would make given more time
If I had more time I would do a better job separating the class logic from the helper code, which is a bit tightly-coupled. The helpef functions should be non-specific to the particular implementation of the Conversation class, so that they can be reused.

I would also spend some more time researching the fuzzysearch library to make sure I'm using the methods in the most performant way. Also, I would try to implement the algorithm from scratch, to understand the nature of the problem with more depth.

## 5. A rough breakdown of how I spent my time

- Researching libraries and possible approaches to solve problems: 1 hour
- Parsing Logic: 40 minutes
- Implementing/refactoring Conversation class: 1 hour
- Implementing arguments, filtering, and search: 1 hour
- Unit test: 20 minutes
- Documenting: 30 minutes
- Manually test installation process to run the code in another machine: 20 minutes
