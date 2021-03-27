class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()","o")
        command = command.replace("(al)","al")
        return command
# Runtime: 16 ms, faster than 99.88% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.2 MB, less than 70.16% of Python3 online submissions for Goal Parser Interpretation.
