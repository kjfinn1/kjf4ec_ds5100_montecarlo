import pandas as pd
import numpy as np

class Die:

    """The Die class defines the dice that will be used in future games. A die has sides, or “faces”, and weights, and can be rolled to select a face.

    Normally, dice and coins are “fair,” meaning that the each side has an equal weight. An unfair die is one where the weights are unequal.

    Each side contains a unique symbol. Symbols may be all alphabetic or all numeric.

    Weight defaults to 1 for each face but can be changed after the object is created.

    The weights are just numbers, not a normalized probability distribution.

    The die has one behavior, which is to be rolled one or more times."""

    def __init__(self, faces):

        """
        Takes a NumPy array of faces as an argument. Throws a TypeError if not a NumPy array.

        The arrays data type (dtype) may be strings or numbers.

        The arrays values must be distinct. Tests to see if the values are distinct and raises a ValueError if not.

        Internally initializes the weights to for each face.

        Saves both faces and weights in a private data frame with faces in the index."""
        
        if not isinstance(faces, list):
            raise TypeError("Dice faces must be an array")
        self.faces = pd.DataFrame({'Faces': faces})
        
        self.faces['Weights'] = 1
        
        if len(self.faces) != len(set(self.faces['Faces'])):
            raise ValueError("Each face value must be unique.")

    def weight_change(self, face_value, new_weight):

        """A method to change the weight of a single side.
        
        Takes two arguments: the face value to be changed and the new weight.

        Checks to see if the face passed is valid value, i.e. if it is in the die array. If not, raises an IndexError.

        Checks to see if the weight is a valid type, i.e. if it is numeric (integer or float) or castable as numeric. If not, raises a TypeError."""

        if face_value not in self.faces['Faces'].values:
            raise IndexError("Face value not found in the die.")
        if not np.issubdtype(type(new_weight), np.number):
            raise TypeError("Weight must be an int or float.")
        self.faces.loc[self.faces['Faces'] == face_value, 'Weights'] = new_weight

    def roll_die(self, rolls=1):

        """A method to roll the die one or more times.

            Takes a parameter of how many times the die is to be rolled; defaults to 1.

            This is essentially a random sample with replacement, from the private die data frame, that applies the weights.

            Returns a Python list of outcomes.

            Does not store internally these results."""

        results = []
        for i in range(rolls):
            result = self.faces.sample(weights=self.faces['Weights'])['Faces'].values[0]
            results.append(result)
        return pd.Series(results)

    def current_state(self):

        """A method to show the dies current state.
        
        Returns a copy of the private die data frame."""

        return self.faces
        
import pandas as pd

class Game:

    """A game consists of rolling of one or more similar dice (Die objects) one or more times.

    By similar dice, we mean that each die in a given game has the same number of sides
    
     and associated faces, but each die object may have its own weights.

    Each game is initialized with a Python list that contains one or more dice.

    Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times.

    Game objects only keep the results of their most recent play."""

    def __init__(self, *die_objects):
        
        """

    Takes a single parameter, a list of already instantiated similar dice."""

        self.die_objects = die_objects
        self.results_df = None 
        self.wide_table = None  

    def play(self, rolls=1):

        """

    Takes an integer parameter to specify how many times the dice should be rolled.

    Saves the result of the play to a private data frame.

    The data frame should be in wide format, i.e. have the roll number as a named index, 
    
    columns for each die number (using its list index as the column name), and the face rolled in that instance in each cell."""

        results = []
        for a, die_object in enumerate(self.die_objects):
            df = pd.DataFrame({'Die': f'Die {a}', 'Result': die_object.roll_die(rolls)})
            results.append(df)
        self.results_df = pd.concat(results, ignore_index=True) 

        
        self.results_df['Roll'] = self.results_df.groupby('Die').cumcount() + 1

        
        self.wide_table = self.results_df.pivot(index='Roll', columns='Die', values='Result')

        
        self.wide_table.reset_index(inplace=True)

    def results(self, narrow=False, wide=True):

        """A method to show the user the results of the most recent play.

    This method just returns a copy of the private play data frame to the user.

    Takes a parameter to return the data frame in narrow or wide form which defaults to wide form.

    The narrow form will have a MultiIndex, comprising the roll number and the die number (in that order), 
    
    and a single column with the outcomes (i.e. the face rolled).

    This method should raise a ValueError if the user passes an invalid option for narrow or wide."""

        if narrow:
            new_order = ['Roll', 'Die', 'Result']
            self.results_df = self.results_df[new_order]
            return self.results_df
        elif wide:
            return self.wide_table
        else:
            raise ValueError("Either 'narrow' or 'wide' parameter must be specified.")
            
import pandas as pd
import itertools 
from collections import Counter
import numpy as np

class Analyzer:
    """

    General Definition. An Analyzer object takes the results of a single game 
  
    and computes various descriptive statistical properties about it."""

    def __init__(self, game_objects):

      """

      Takes a game object as its input parameter. Throw a ValueError if the passed value is not a Game object."""

      if not isinstance(game_objects, Game):
        raise ValueError("game_objects must be an instance of the Game class.")
      self.game_objects = game_objects
      self.wide_table = game_objects.wide_table

    def jackpot(self):
      """

      A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die.

      Computes how many times the game resulted in a jackpot, if an individual roll resulted in a jackpot and 
      
      the jackpots per roll at that stage of the game.

      Returns an integer for the number of jackpots."""

      table1 = self.wide_table.copy()
      table1['Jackpot'] = table1.apply(lambda row: row.drop('Roll').nunique() == 1, axis=1)

      jackpot_count = 0
      for a in range(0, len(table1.Roll)):
        if table1['Jackpot'][a]:
          jackpot_count += 1
        table1.loc[a, 'Jackpot per roll'] = jackpot_count / (a+1)
      print("Total Jackpots " + str(jackpot_count))
      return table1


    def face_counts_per_roll(self):

      """

      Computes how many times a given face is rolled in each event.
        
      Returns a data frame of results.

      The data frame has an index of the roll number, face values as columns, 
      
      and count values in the cells (i.e. it is in wide format)."""

      roll_counts = []

      table5 = self.wide_table.drop(columns='Roll')

      for index, row in table5.iterrows():
        counts = Counter(row)
        roll_counts.append(counts)

      df = pd.DataFrame(roll_counts)
      df.index.name = 'Roll'
      df_filled = df.fillna(0)
      return df_filled


    def combo_count(self):

      """

      Computes the distinct combinations of faces rolled, along with their counts.

      Combinations are order-independent and may contain repetitions.

      Returns a data frame of results.

      The data frame should have an MultiIndex of distinct combinations and a column for the associated counts."""

      table2 = self.wide_table.copy()
      table2.drop(columns='Roll', inplace=True) 

      table2['Combination'] = table2.apply(lambda row: tuple(sorted(row)), axis=1)
        
      combination_counts = table2['Combination'].value_counts().reset_index()
      combination_counts.columns = ['Combination', 'Count']
        
      return combination_counts
      
    def perm_count(self):

      """
      Computes the distinct permutations of faces rolled, along with their counts.

      Permutations are order-dependent and may contain repetitions.

      Returns a data frame of results.

      The data frame should have an MultiIndex of distinct permutations and a column for the associated counts."""

      table2 = self.wide_table.copy()
      table2.drop(columns='Roll', inplace=True)  # Drop the 'Die' column

      return table2.apply(lambda row: tuple(row), axis=1).value_counts()