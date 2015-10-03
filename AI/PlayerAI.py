#!/usr/bin/env python
#coding:utf-8

from random import randint
from BaseAI import BaseAI
from math import log
from Evalue import *
import time

possiblevalues = [2,4]

class PlayerAI(BaseAI):
	def getMove(self, grid):
		alpha = -float("inf")
		beta = float("inf")
		depth = 1
		flag = True
		gridCopy = grid.clone()
		starttime = time.clock()
		optmove,score = self.search(gridCopy,alpha,beta,depth,flag,starttime)
		return optmove

	def search(self, grid, alpha, beta, depth, playerTurn, starttime):
		bestmove = None		
		if playerTurn==True:
			flag = False
			moves = grid.getAvailableMoves()
			if len(moves)==0:
				return (None,0)
			elif time.clock()-starttime>=0.03:
				return (None,value(grid))
			for cur in moves:
				gridCopy = grid.clone()
				gridCopy.move(cur)			
				m,tempv = self.search(gridCopy,alpha,beta,depth+1,flag,starttime) 
				if tempv>alpha:
					alpha = tempv
					bestmove = cur
				if alpha>=beta:
					return (cur,tempv)
			bestscore = alpha
		else:
			cells = grid.getAvailableCells()
			flag = True
			for cur in cells:
				if grid.canInsert(cur):
					for pv in possiblevalues:
						grid.setCellValue(cur,pv)
						m,tempv = self.search(grid,alpha,beta,depth+1,flag,starttime)
						grid.setCellValue(cur,0)
						if tempv<beta:
							beta = tempv
						if beta<=alpha:
							return (None,tempv)
			bestscore = beta
		return (bestmove,bestscore)



