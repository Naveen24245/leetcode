class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result

# Instantiate and test
s = Solution()
print(s.letterCombinations("23"))   # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(s.letterCombinations(""))     # []
print(s.letterCombinations("2"))    # ["a", "b", "c"]
