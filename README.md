# bowlingMatchScore-test
bowling Match Score - test

calculate bowling Match Score using python 3

## Prerequisites

All code are tested under Python 3.6.9.

Nose library should be install for unittest. For example, use following command:

```
pip install nose
``` 
 

## Installation

Download the code and install on a path.

## Run

### Run unit test

```
nosetests <code install path>
```

Expected result should be as following:

```
.......
----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK

```
### Run production code

The running test can be modified in "def main" function of App.py .

```
python3 <code install path>/app/App.py
```
Expected result should be as following:

```
30
```

### Notes

In App.py , function "roll(noOfPins )" will accept a number as pins in this roll and put it into records for score calculation.

In App.py , function "rollAll(noOfPins )" will accept a list of number as pins in all rolls and put it into records for score calculation.   *Be careful* : this function will use provided list to replace/overwrite all previously provided pin records. This function provide a convenient method for providing all roll records, comparing to input one by one using "roll()" function. 

In App.py , function "score()" will return total score as a number.

### Project Requirements

Project Requirements are from https://github.com/DiUS/coding-tests/blob/master/dius_bowling.md






  
  

