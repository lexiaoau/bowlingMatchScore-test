#!/usr/bin/python3

CONST_MAX_FRAME_PER_MATCH  = 10
CONST_MAX_PIN_PER_FRAME  = 10

FULL_STRIKE_SCORE = 300

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

		### calc score when rolls less than 2
		if rollCount == 0 :
			return 0
		if rollCount == 1 :
			return rolledPinList[0]

		maxFrameCnt = self.MAX_FRAME_PER_MATCH 
		maxPinCnt = self.MAX_PIN_PER_FRAME 

		totalScore = 0

		usedFrameCunt = 0

		strikeCnt = 0

		#### loop roll list to calculate total score
		#### 
		#### check frame by sequence. If one frame found, calculate its score and add to total score
		#### loop until maximun frame reached or no more frame left.
		####
		ind = 0
		while ind < rollCount and usedFrameCunt < maxFrameCnt :
			if ind == (  rollCount - 1 ) :
				pass

			thisRollPin = rolledPinList[ ind ]
			firstRollPin = 0													### first roll pin after current roll
			if (ind+1) < rollCount :
				firstRollPin = rolledPinList[ ind + 1 ]
			secondRollPin = 0													### second roll pin after current roll
			if (ind+2) < rollCount :
				secondRollPin = rolledPinList[ ind + 2 ]

			if thisRollPin == maxPinCnt :										### this roll is STRIKE
				totalScore += thisRollPin + firstRollPin + secondRollPin
				usedFrameCunt += 1 
				strikeCnt += 1 
				ind += 1
			elif ( thisRollPin + firstRollPin  ) == maxPinCnt  :										### this roll is SPARE
				totalScore += thisRollPin + firstRollPin + secondRollPin
				usedFrameCunt += 1 
				ind += 2
			else:																													### assume all other condition is normal frame
				totalScore += thisRollPin + firstRollPin
				usedFrameCunt += 1 
				ind += 2
			pass

		if strikeCnt == maxFrameCnt :
			totalScore = FULL_STRIKE_SCORE

		self.rolledPinList = []										### clear roll records
		return totalScore

if __name__== "__main__":
	app = App(10, 10)
	app.rollAll(  [10, 10] )
	print(app.score())


