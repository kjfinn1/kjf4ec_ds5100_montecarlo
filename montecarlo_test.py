import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
class MonteCarloTestSuite(unittest.TestCase):

    def test_1_init(self):
        die_object = Die(['a', 'b'])
        self.assertEqual(type(die_object), Die)

    def test_2_weight_change(self):
        die_obj = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        die_obj.weight_change('a', 2)
        self.assertTrue(die_obj.faces.Weights[0]==2)
        
    def test_3_roll_die(self):
        die_obj = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        roll1 = die_obj.roll_die()
        self.assertTrue(roll1[0] == 'a' or roll1[0] == 'b' or roll1[0] == 'c' or roll1[0] == 'd' or roll1[0] == 'e' or roll1[0] == 'f')

    def test_4_current_state(self):
        die_obj = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        current = die_obj.current_state()
        self.assertTrue(current['Weights'][4]==1)
        
    def test_5_init(self):
        die_object = Die(['a', 'b'])
        game_obj=Game(die_object)
        self.assertEqual(type(game_obj), Game)   

    def test_6_play(self):
        die_obj = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        game_obj=Game(die_obj)
        game_obj.play()
        roll2=game_obj.wide_table['Die 0'][0]
        self.assertTrue(roll2 == 'a' or roll2 == 'b' or roll2 == 'c' or roll2 == 'd' or roll2 == 'e' or roll2 == 'f')

    def test_7_results(self):
        die_obj = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        game_obj=Game(die_obj)
        game_obj.play(20)
        game_obj.results()
        roll2=game_obj.wide_table['Die 0'][19]
        self.assertTrue(roll2 == 'a' or roll2 == 'b' or roll2 == 'c' or roll2 == 'd' or roll2 == 'e' or roll2 == 'f')
        
    def test_8_init(self):
        die_object = Die(['a', 'b'])
        game_obj=Game(die_object)
        analyzer_object=Analyzer(game_obj)
        self.assertEqual(type(analyzer_object), Analyzer)   

    def test_9_jackpot(self):
        die_obj = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        die_obj2 = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        game_obj=Game(die_obj, die_obj2)
        game_obj.play(20)
        analyzer_object=Analyzer(game_obj)
        self.assertTrue(analyzer_object.jackpot()['Jackpot'][5] == True or analyzer_object.jackpot()['Jackpot'][5]  == False)

    def test_10_jackpot(self):
        die_obj = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        die_obj2 = Die(['a', 'b', 'c', 'd', 'e', 'f'])
        game_obj=Game(die_obj, die_obj2)
        game_obj.play(20)
        analyzer_object=Analyzer(game_obj)
        roll3=analyzer_object.face_counts_per_roll()['a'][5]
        self.assertTrue(roll3== 1.0 or roll3 == 2.0 or roll3== 0.0)

    def test_11_combo_count(self):
        die_obj = Die(['a', 'b'])
        die_obj2 = Die(['a', 'b'])
        game_obj=Game(die_obj, die_obj2)
        game_obj.play(20)
        analyzer_object=Analyzer(game_obj)
        roll4=analyzer_object.combo_count()['Count'][0]
        self.assertTrue(roll4 >=6)
        
    def test_12_perm_count(self):
        die_obj = Die(['a', 'b'])
        die_obj2 = Die(['a', 'b'])
        game_obj=Game(die_obj, die_obj2)
        game_obj.play(20)
        analyzer_object=Analyzer(game_obj)
        roll5=analyzer_object.perm_count()[0]
        self.assertTrue(roll5 >=5)

if __name__ == '__main__':
    unittest.main()