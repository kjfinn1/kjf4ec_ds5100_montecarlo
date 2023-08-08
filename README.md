# ds5100_montecarlo
DS5100 Final Project
Final project for DS5100 as part of UVA data science masters degree
Project creates three classes and places them in montecarlo module that creates and analyzes a dice game.
Project name is Monte Carlo simulator

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
