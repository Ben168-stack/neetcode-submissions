class Solution:
    def isValid(self, s: str) -> bool:
        bracket_hash = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack_bracket = []

        for i in range(0, len(s)):
            if s[i] in "({[":
                stack_bracket.append(s[i])

            elif s[i] in ")}]":
                if len(stack_bracket) == 0:
                    return False
                left_stack = stack_bracket.pop()
                if left_stack != bracket_hash.get(s[i], None):
                    return False

        if len(stack_bracket) != 0:
            return False

        return True


