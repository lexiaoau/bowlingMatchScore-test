#!/usr/bin/python3
from unittest.mock import patch
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../app")

from App import App

class TestAppClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = App(10, 10)             # app instance to run test on

    def test_app_simpleRoll(self):        

        self.app.rollAll( [] )
        self.assertEqual(0, self.app.score() )

        oneRoll = 9
        self.app.rollAll( [oneRoll] )
        self.assertEqual(oneRoll, self.app.score() )

    def test_app_allStrike(self):        
        FULL_STRIKE_SCORE = 300

        strike_pin = 10

        strike_cnt = 1
        pinList = [strike_pin] * strike_cnt
        self.app.rollAll( pinList )
        self.assertEqual(10, self.app.score() )

        strike_cnt = 2
        pinList = [strike_pin] * strike_cnt
        self.app.rollAll( pinList )
        self.assertEqual(   ( (strike_cnt-1) * (strike_pin * 3)   )  , self.app.score() )

        strike_cnt = 5
        pinList = [strike_pin] * strike_cnt
        self.app.rollAll( pinList )
        self.assertEqual(   ( (strike_cnt-1) *  (strike_pin * 3)   )  , self.app.score() )

        strike_cnt = 9
        pinList = [strike_pin] * strike_cnt
        self.app.rollAll( pinList )
        self.assertEqual(   ( (strike_cnt-1) *  (strike_pin * 3)   )  , self.app.score() )

        strike_cnt = 10
        pinList = [strike_pin] * strike_cnt
        self.app.rollAll( pinList )
        self.assertEqual(   FULL_STRIKE_SCORE  , self.app.score() )

        strike_cnt = 10
        pinList = [strike_pin] * strike_cnt
        pinList = pinList + [1 , 2]
        self.app.rollAll( pinList )
        self.assertEqual(   FULL_STRIKE_SCORE  , self.app.score() )

    def test_app_allNormal(self):        

        oneFrame = [ 1, 2 ]
        oneFrameScore = 3

        cnt = 3
        lastFrame = [ 7]
        lastFrameScore = 7
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )        

        cnt = 9
        lastFrame = [ 7]
        lastFrameScore = 7
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )        

        cnt = 9
        lastFrame = [ 7 , 2]
        lastFrameScore = 9
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )    

        cnt = 10
        lastFrame = [ 7 , 2]
        lastFrameScore = 9
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt  , self.app.score() )    

        cnt = 11
        lastFrame = [ 7 , 2]
        lastFrameScore = 9
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * 10  , self.app.score() )       

    def test_app_all(self):        

        l1 = [ 4, 4]
        pinList = l1
        expectdScore = 8
        self.app.rollAll( pinList )
        self.assertEqual( expectdScore , self.app.score() )      

        l2 = [ 4, 6, 5 , 0 ]
        pinList = l2
        expectdScore = 20
        self.app.rollAll( pinList )
        self.assertEqual( expectdScore , self.app.score() )        

        l3 = [  10, 5, 4 ]
        pinList = l3
        expectdScore = 28
        self.app.rollAll( pinList )
        self.assertEqual( expectdScore , self.app.score() )    

        pinList = l1 + l3
        expectdScore = 36
        self.app.rollAll( pinList )
        self.assertEqual( expectdScore , self.app.score() )    

        pinList =  l3 + l1
        expectdScore = 36
        self.app.rollAll( pinList )
        self.assertEqual( expectdScore , self.app.score() ) 

        l4 = [  10, 4, 6, 5 , 0 ]
        pinList = l4
        expectdScore = 40
        self.app.rollAll( pinList )
        self.assertEqual( expectdScore , self.app.score() )  

        ### test last frame is strike
        ### test last frame is strike
        ### test last frame is strike
        oneFrame = [ 1, 2 ]
        oneFrameScore = 3
        cnt = 9
        lastFrame = [ 10]
        lastFrameScore = 10
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )    

        cnt = 9
        lastFrame = [ 10, 1]
        lastFrameScore = 11
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )    

        cnt = 9
        lastFrame = [ 10, 1 ,4]
        lastFrameScore = 15
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )     

        cnt = 9
        lastFrame = [ 10, 1 ,4 , 7]
        lastFrameScore = 15
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )     

        ### test last frame is spare
        ### test last frame is spare
        ### test last frame is spare
        oneFrame = [ 1, 2 ]
        oneFrameScore = 3

        cnt = 9
        lastFrame = [ 7, 3]
        lastFrameScore = 10
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )    

        cnt = 9
        lastFrame = [ 7, 3 , 2]
        lastFrameScore = 12
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )    

        cnt = 9
        lastFrame = [ 7, 3 , 2, 4]
        lastFrameScore = 12
        pinList = oneFrame * cnt + lastFrame
        self.app.rollAll( pinList )
        self.assertEqual( oneFrameScore * cnt + lastFrameScore , self.app.score() )    



