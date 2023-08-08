# ds5100_montecarlo
#Meta data
DS5100 Final Project
Final project for DS5100 as part of UVA data science masters degree
Project creates three classes and places them in montecarlo module that creates and analyzes a dice game.
Project name is Monte Carlo simulator

#Synopsis

Sample Code:

import pandas as pd 
import itertools 
from collections import Counter 
import numpy as np 
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

Examples for Die class:

test_object = Die(['a','b','c','d','e','f'])
test_object2 = Die(['a','b','c','d','e','f'])
test_object3 = Die(['a','b','c','d','e','f'])
test_object2.weight_change('a', 12)
test_object.weight_change('a', 12)
test_object.roll_die()
  0    f
  dtype: object
  
test_object2.current_state()

  Faces	Weights
0	a	    12
1	b	    1
2	c	    1
3	d	    1
4	e	    1
5	f	    1

Examples for Game class:

test_object4=Game(test_object2, test_object, test_object3)

test_object4.play(100)

test_object4.results()

Die	Roll	Die 0	Die 1	Die 2
0	  1	    a	    a	    f
1	  2	    b	    a	    c
2	  3	    e	    a	    c
3	  4	    e	    d	    e
4	  5	    f	    a	    b
...	...	  ...	  ...	  ...
95	96	  a	    a	    c
96	97	  a	    a	    d
97	98	  d	    a	    e
98	99	  a	    a	    e
99	100	  f	    a	    b
100 rows × 4 columns

Examples for Analyzer class:

test_object5=Analyzer(test_object4)

test_object5.face_counts_per_roll()

	    a	  f	  e	  b	  c	  d
Roll						
0	    2.0	1.0	0.0	0.0	0.0	0.0
1	    3.0	0.0	0.0	0.0	0.0	0.0
2	    1.0	0.0	1.0	1.0	0.0	0.0
3	    3.0	0.0	0.0	0.0	0.0	0.0
4	    2.0	0.0	0.0	0.0	1.0	0.0
...	  ...	...	...	...	...	...
95	  2.0	0.0	1.0	0.0	0.0	0.0
96	  1.0	0.0	0.0	1.0	0.0	1.0
97	  2.0	1.0	0.0	0.0	0.0	0.0
98	  2.0	1.0	0.0	0.0	0.0	0.0
99	  0.0	0.0	1.0	0.0	2.0	0.0
100 rows × 6 columns

test_object5.jackpot()

Total Jackpots 6
Die	Roll	Die 0	Die 1	Die 2	Jackpot	Jackpot per roll
0	  1	    a	    f	    a	    False	  0.000000
1	  2	    a	    a	    a	    True	  0.500000
2	  3	    e	    a	    b	    False	  0.333333
3	  4	    a	    a	    a	    True	  0.500000
4	  5	    a	    c	    a	    False	  0.400000
...	...	  ...	  ...	  ...	  ...	    ...
95	96	  e	    a	    a	    False	  0.062500
96	97	  b	    d	    a	    False	  0.061856
97	98	  a	    a	    f	    False	  0.061224
98	99	  a	    a	    f	    False	  0.060606
99	100	  c	    e	    c	    False	  0.060000
100 rows × 6 columns

test_object5.perm_count()

(a, a, d)    11
(a, a, c)    10
(a, a, b)     9
(a, a, f)     7
(a, a, a)     6
(a, a, e)     4
(a, f, a)     3
(d, a, b)     3
(e, a, a)     2
(a, d, b)     2
(a, e, f)     2
(f, a, d)     2
(f, a, f)     2
(c, a, e)     2
(a, b, f)     2
(a, c, f)     2
(e, a, b)     2
(b, a, f)     1
(f, c, e)     1
(d, d, b)     1
(b, a, a)     1
(b, a, b)     1
(f, a, b)     1
(a, d, a)     1
(a, e, d)     1
...
(a, b, e)     1
(a, f, b)     1
(a, c, a)     1
(c, e, c)     1
dtype: int64

test_object5.combo_count()

	Combination	Count
0	  (a, a, f)	13
1	  (a, a, a)	9
2	  (a, a, e)	9
3	  (a, a, d)	8
4	  (a, a, c)	8
5	  (a, a, b)	6
6	  (a, c, e)	5
7	  (a, c, f)	5
8	  (a, b, f)	4
9	  (a, d, f)	4
10	(a, d, d)	3
11	(a, e, f)	3
12	(a, b, c)	3
13	(a, b, b)	2
14	(a, b, d)	2
15	(b, d, f)	2
16	(a, d, e)	2
17	(a, c, d)	2
18	(a, c, c)	2
19	(c, e, f)	1
20	(c, d, f)	1
21	(b, e, f)	1
22	(d, e, e)	1
23	(b, b, c)	1
24	(a, b, e)	1
25	(c, d, d)	1
26	(c, d, e)	1

#API description

Die class:

	The Die class defines the dice that will be used in future games. A die has sides, or “faces”, and weights, 
 	and can be rolled to select aface.

	Normally, dice and coins are “fair,” meaning that the each side has an equal weight. An unfair die is one where the weights are unequal.

    	Each side contains a unique symbol. Symbols may be all alphabetic or all numeric.

    	Weight defaults to 1 for each face but can be changed after the object is created.

    	The weights are just numbers, not a normalized probability distribution.

    	The die has one behavior, which is to be rolled one or more times.

    Init method: 
    
        Takes a NumPy array of faces as an argument. Throws a TypeError if not a NumPy array.

        The arrays data type (dtype) may be strings or numbers.

        The arrays values must be distinct. Tests to see if the values are distinct and raises a ValueError if not.

        Internally initializes the weights to for each face.

        Saves both faces and weights in a private data frame with faces in the index.

    Weight change method:

	A method to change the weight of a single side.
        
        Takes two arguments: the face value to be changed and the new weight.

        Checks to see if the face passed is valid value, i.e. if it is in the die array. If not, raises an IndexError.

        Checks to see if the weight is a valid type, i.e. if it is numeric (integer or float) or castable as numeric. If not, raises a TypeError.

    Roll die method:
   
   	    A method to roll the die one or more times.

            Takes a parameter of how many times the die is to be rolled; defaults to 1.

            This is essentially a random sample with replacement, from the private die data frame, that applies the weights.

            Returns a Python list of outcomes.

            Does not store internally these results.

     Current state method:
     
     	    A method to show the dies current state.
        
            Returns a copy of the private die data frame.

Game class:

    A game consists of rolling of one or more similar dice (Die objects) one or more times.

    By similar dice, we mean that each die in a given game has the same number of sides
    
     and associated faces, but each die object may have its own weights.

    Each game is initialized with a Python list that contains one or more dice.

    Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times.

    Game objects only keep the results of their most recent play.

       Init method:

    	   Takes a single parameter, a list of already instantiated similar dice.

       Play method:

    	   A play method.

    	   Takes an integer parameter to specify how many times the dice should be rolled.

           Saves the result of the play to a private data frame.

           The data frame should be in wide format, i.e. have the roll number as a named index, 
    
           columns for each die number (using its list index as the column name), and the face rolled in that instance in each cell.

       Results method:

    	   A method to show the user the results of the most recent play.

    	   This method just returns a copy of the private play data frame to the user.

    	   Takes a parameter to return the data frame in narrow or wide form which defaults to wide form.

    	   The narrow form will have a MultiIndex, comprising the roll number and the die number (in that order), 
    
    	   and a single column with the outcomes (i.e. the face rolled).

    	   This method should raise a ValueError if the user passes an invalid option for narrow or wide.

Analyzer method:

    General Definition. An Analyzer object takes the results of a single game 
  
    and computes various descriptive statistical properties about it.

        Init method:

           Takes a game object as its input parameter. Throw a ValueError if the passed value is not a Game object.

        Jackpot method:

           A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die.

           Computes how many times the game resulted in a jackpot, if an individual roll resulted in a jackpot and 
      
           the jackpots per roll at that stage of the game.

           Returns an integer for the number of jackpots.

        Face counts per roll method:

           Computes how many times a given face is rolled in each event.
        
           Returns a data frame of results.

           The data frame has an index of the roll number, face values as columns, 
      
           and count values in the cells (i.e. it is in wide format).

       Combo counts method:

          Computes the distinct combinations of faces rolled, along with their counts.

          Combinations are order-independent and may contain repetitions.

          Returns a data frame of results.

          The data frame should have an MultiIndex of distinct combinations and a column for the associated counts.

       Permutation counts method:

          Computes the distinct permutations of faces rolled, along with their counts.

          Permutations are order-dependent and may contain repetitions.

          Returns a data frame of results.

          The data frame should have an MultiIndex of distinct permutations and a column for the associated counts.
    
