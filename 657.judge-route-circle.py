#
# [657] Judge Route Circle
#
# https://leetcode.com/problems/judge-route-circle/description/
#
# algorithms
# Easy (68.50%)
# Total Accepted:    83.2K
# Total Submissions: 121.4K
# Testcase Example:  '"UD"'
#
# 
# Initially, there is a Robot at position (0, 0). Given a sequence of its
# moves, judge if this robot makes a circle, which means it moves back to the
# original place. 
# 
# 
# 
# The move sequence is represented by a string. And each move is represent by a
# character. The valid robot moves are R (Right), L (Left), U (Up) and D
# (down). The output should be true or false representing whether the robot
# makes a circle.
# 
# 
# Example 1:
# 
# Input: "UD"
# Output: true
# 
# 
# 
# Example 2:
# 
# Input: "LL"
# Output: false
# 
# 
#
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dicCount = {}
        for c in moves:
            if c not in dicCount:
                dicCount.setdefault(c, 1)
            else:
                dicCount[c] += 1
        up = 0 if 'U' not in dicCount else dicCount['U']
        down = 0 if 'D' not in dicCount else dicCount['D']
        right = 0 if 'R' not in dicCount else dicCount['R']
        left = 0 if 'L' not in dicCount else dicCount['L']
        return True if up == down and right == left else False
