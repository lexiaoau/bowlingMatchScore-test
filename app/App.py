#!/usr/bin/python3
from enum import Enum

CONST_MAX_FRAME_PER_MATCH  = 10
CONST_MAX_PIN_PER_FRAME  = 10

class FrameType(Enum):
	NORMAL = 1
	SPARE = 2
	STRIKE = 3

class App:
	def __init__(self, matFrameCount=CONST_MAX_FRAME_PER_MATCH , matPinCount=CONST_MAX_PIN_PER_FRAME ):

		self.MAX_FRAME_PER_MATCH = matFrameCount			### maximum frames allowed in one match
		self.MAX_PIN_PER_FRAME = matPinCount			### maximum pin  allowed in one frame

		self.rolledPinList = []			### a list of pin numbers for each roll

		
	# add pin of one roll
	def roll(self , noOfPins ):
		self.rolledPinList.append(  noOfPins  )

	# add pin of all rolls
	def rollAll(self , noOfPinsList ):
		self.rolledPinList = noOfPinsList

	# get score for one player in this match
	def score(self):
		rolledPinList = self.rolledPinList

		rollCount = len(  rolledPinList  )

		if rollCount == 0 :
			return 0
		if rollCount == 1 :
			return rolledPinList[0]

		totalScore = 0

		cur_frame_type  = 0

		strikeCnt = 0

		return totalScore

if __name__== "__main__":
	app = App(10, 10)
	app.score()


