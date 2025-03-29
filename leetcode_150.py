from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]
                    
import unittest


class TestSolution(unittest.TestCase):
    def test_evalRPN(self):
        sol = Solution()
        self.assertEqual(sol.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(sol.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

if __name__ == '__main__':
    unittest.main()