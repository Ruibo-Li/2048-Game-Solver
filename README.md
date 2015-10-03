# 2048-Game-Solver
File Description:
ComputerAI.py: The computer AI module.
PlayerAI.py: The player AI module
Evalue.py: The heuristic functions and the value function for player AI and computer AI.

AI Description:
The PlayerAI and ComputerAI are both for the game 2048. The algorithm is depth first alpha-bate search. Instead of depth limit, I use time limit to control the time of the search. The reason is that at the start of the game, the branch factor is big, the algorithm can only run with low depth limit. While when the empty tiles in the grid become  less, the depth the DFS can go with become larger. Using the time limit enables larger depth in this case.

The PlayerAI and ComputerAI modules are designed using the MinMax and alpha-beta pruning method, in which the Max function refers to the PlayerTurn and the Min function refers to the ComputerTurn. Several heuristics are used to evaluate the grid:

(1)empty
This evaluation function grades the grid according to the number of empty tiles. The grid with more empty tiles will be less possible to lose, thus is graded better than those with less empty tiles.

(2)maxcellvalue
This evaluation function grades the grid according to the max value of the tiles in the grid. The grid with larger max value is more likely to reach the tile with larger value. So it will be graded better.

(3)smoothness
This evaluation function tends to evaluate higher for the grid with less difference between adjacent tiles. A smooth grid is more likely to have grids that can merge.

(4)cornervalue
This evaluation function measures the values of the corner tiles of the grid. The grid with larger corner tile values is graded higher. The object of this function is to maintain the tiles with larger values into the corner, because they are relatively difficult to merge.

(5)edgevalue
This evaluation function measures the values of the values of the tiles that are at the edges of the grid. The grid with larger edge tile values is graded higher. The object of this function is to keep the tiles with larger values to the edge for them to merge with each other and keep away from the tiles with small value.

(6)cluster
 This evaluation function measures how much scattered are the values of the grid. Tiles with similar close values are easier to merge. Thus the function graded higher for the grid with scattered values. The score is used as a penalty in the evaluation.

Different weights are used for the total evaluation.

The player AI acts as MAX, which tends to get moves which will maximize the value of the grid from the evaluation function. While the computer AI acts as MIN, which tends to set value to cells, which could minimize the evalues. The play AI and the computer AI are designed symmetrically.
