#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (58.21%)
# Total Accepted:    84.4K
# Total Submissions: 144.9K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water. Grid cells are connected
# horizontally/vertically (not diagonally). The grid is completely surrounded
# by water, and there is exactly one island (i.e., one or more connected land
# cells). The island doesn't have "lakes" (water inside that isn't connected to
# the water around the island). One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
# 
# Example:
# 
# [[0,1,0,0],
#  ⁠[1,1,1,0],
#  ⁠[0,1,0,0],
#  ⁠[1,1,0,0]]
# 
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
#
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        rowSize = len(grid)
        colSize = len(grid[0])
        for row in range(0, rowSize):
            for col in range(0, colSize):
                if grid[row][col] != 1:
                    continue
                # up
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # down
                if row == rowSize-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # right
                if col == colSize-1 or grid[row][col+1] == 0:
                    perimeter += 1

        return perimeter
