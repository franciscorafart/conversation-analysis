## 1. Installation/running instructions

1. Extract the files 
2. In the extracted folder directory, activate the venv with `$ source bin/activate`
3. Install the packages with `$ pip install`
4. Run `$ python3 conversation_analyzer.py` with any arguments you want.
5. Run unit tests with `$ pytest tests`
6. Deactivate the environment when finished `$ deactivate`

## 2. How you approached the problem
I started with a rudimentary implementation of the print so I could get the parsing logic out of the way. I did this mainly with functions.

I refactored the code intoa class when I realized I would have to reference the parsed data several times.

## 3. Any problems you ran into
Finding a way of implementing the 'query' and 'similar' in a performant way was challenging. I thought of a Trie structure to search for strings performatly, but then I realized it doesn't apply well because the text is not really a dictionary.

I realized a fuzzy search would be better fit for the task with the time I have at hand.

## 4. Any optimizations or changes you’d make given more time
If I had more time I would do a better job separating the class logic from the interface code. For example, the whole handling of conversation filtering could be done either by a separate module/functions or a new class.

## 5. A rough breakdown of how you spent your time
Spent about an hour refreshing researching tools and methods I could use for the implementation such as statistics, argsparse.

Then I spent about an hour implementing the parsing logic.

About 20 minutes writting the tests.



TODO:
Environment setup => Test before