class Solution(object):
    def isValid(self, s):
        stack = []

        for ch in s:

    # Opening brackets
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)

    # Closing bracket )
            elif ch == ")":

        # stack empty?
                if not stack:
                    return False

                top = stack.pop()

                if top != "(":
                    return False

    # Closing bracket ]
            elif ch == "]":

                if not stack:
                    return False

                top = stack.pop()

                if top != "[":
                    return False

    # Closing bracket }
            elif ch == "}":

                if not stack:
                    return False

                top = stack.pop()

                if top != "{":
                   return False


# After processing everything
        return len(stack) == 0