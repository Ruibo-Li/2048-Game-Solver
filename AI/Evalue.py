
from random import randint
from BaseAI import BaseAI
from math import log
import time
import sys
depthlimit = 4
possiblevalues = [2]


def value(grid):
	ew = 0.49
	maxw= 0.55
	sw = 0.1
	cw = 1
	clw = 0.15
	edw = 0.49
	
	value = ew*empty(grid)+maxw*maxcellvalue(grid)+sw*smoothness(grid)+cw*cornervalue(grid)+edw*edgevalue(grid)-clw*cluster(grid)
	return max(value,0)

def cornervalue(grid):
	cornersum = grid.map[0][3]+grid.map[0][0]+grid.map[3][0]+grid.map[3][3]
	return 0 if cornersum==0 else log(cornersum)

def edgevalue(grid):
	esum = 0
	for x in xrange(grid.size):
		for y in xrange(grid.size):
			if x==0 or x==3 or y==0 or y==3:
				esum = esum+grid.map[x][y]
	return 0 if esum==0 else log(esum)

def empty(grid):
	num = len(grid.getAvailableCells())
#	return 0 if num==0 else log(num)
	return num


def maxcellvalue(grid):
	num = grid.getMaxTile()
	return 0 if num==0 else log(num,2)


def smoothness(grid):
	smoothvalue = 0
	for x in xrange(grid.size):
		for y in xrange(grid.size):
			if grid.map[x][y]!=0:
				v = log(grid.map[x][y])/log(2)
				fary = y+1
				while (fary<grid.size) and (grid.map[x][fary]==0):
					fary = fary+1
				if fary<grid.size:
					v1 = log(grid.map[x][y])/log(2)
					smoothvalue = smoothvalue-abs(v1-v)
				farx = x+1
				while (farx<grid.size) and (grid.map[farx][y]==0):
					farx = farx+1
				if farx<grid.size:
					v1 = log(grid.map[farx][y])/log(2)
					smoothvalue = smoothvalue-abs(v1-v)
	return smoothvalue


def cluster(grid):
	clusterscore = 0
	for i in xrange(grid.size):
		for j in xrange(grid.size):
			if grid.map[i][j]==0:
				continue
			nN = 0
			sumn = 0
			neighbors = [-1,0,1]
			for k in neighbors:
				x = i+k
				if x<0 or x>=grid.size:
					continue
				for l in neighbors:
					y = j+l
					if y<0 or y>= grid.size:
						continue
					if grid.map[x][y]>0:
						nN = nN+1
						sumn = sumn+abs(log(grid.map[x][y],2)-log(grid.map[i][j],2))
			clusterscore = clusterscore+sumn/nN
	return clusterscore