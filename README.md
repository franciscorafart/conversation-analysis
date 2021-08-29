## 1. Installation/running instructions

1. Extract the files 
2. In the extracted folder directory, activate the venv with `$ source bin/activate`
3. Install the packages with `$ pip install`
4. Run `$ python3 analysis.py` with arguments.
Example:
    `python3 analysis.py`
    `python3 analysis.py --starts-after 2020-10-22`
    `python3 analysis.py --query 'beginning'`
    `python3 analysis.py --similar 'the begining'` (With spelling error)

5. Run unit tests with `$ pytest tests`
6. Deactivate the environment when finished `$ deactivate`

## 2. How you approached the problem
My approach was to get the basic information parsed and printed at the beggining so I had results to show. After I figured that out I worked on implementing the more coplex fiunctionality such as date filtering, query, similar, and the snippet printing (random and query-based).

For the implementation of `similar`, I ended up using an external library, as implementing an efficient algorithm for this seemed very out of scope.

Explanation of health score:

For the Conversation Healh Score, I used 3 indicators that add up to a score:
    1. `balanced` - determines whether a conversation is balanced depending on the usage of time of the different people (except the moderator). I used the coefficient of variation and an arbitrary threshold of 0.6 to determine whether a conversation in balanced or not.
    2. `calmed` - compares the amount of time taken to speak with the actual time people speak words, as an indicator of how much time they take to deliver their message.
    3. `fluent` - evaluates the amount of time the facilator uses of the total, with the idea that a fluent conversation doesn't require the facilitator to intervene too much.


## 3. Any problems you ran into
Finding a way of implementing the 'query' and 'similar' was challengingg. I thought of a Trie structure to search for strings at the beginning, but then I realized it doesn't apply well because the text is not really a dictionary. I researched and found the fuzzy search library to implement the `similar` filter.

I also had some issues with getting pytest to find the external libraries I used. I had to uninstall the packages from my global env and reinstall them on venv.

## 4. Any optimizations or changes you’d make given more time
If I had more time I would do a better job separating the class logic from the helper code, which is a bit tightly-coupled. The helpef functions should be non-specific to the particular implementation of the Conversation class, so that they can be reused.

I would also spend some more time researching the fuzzysearch library to make sure I'm using the methods in the most performant way.

## 5. A rough breakdown of how you spent your time

- Researching libraries and possible approaches to solve problems: 1 hour
- Parsing Logic: 40 minutes
- Implementing Conversation class: 1 hour
- Implementing arguments, filtering, and search: 1 hour
- Unit test: 20 minutes
- Documenting: 30 minutes
- Manually test installation process to run the code: 30 minutes
