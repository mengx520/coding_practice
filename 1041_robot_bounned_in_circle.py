'''
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dy =  (0, 1)
        x, y = 0, 0
        for instruction in instructions:
            if instruction == 'G':
                x, y = x + dy[0], y + dy[1]
            elif instruction  == 'L':
                dy = (-dy[1], dy[0])
            else:
                dy = (dy[1], -dy[0])
        return (x == 0 and y == 0) or dy != (0, 1)
