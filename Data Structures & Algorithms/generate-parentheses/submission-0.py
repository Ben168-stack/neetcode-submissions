class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack("", 0, 0, n, result)
        return result

    
    def backtrack(self, current, open_used, close_used,n,result):
        if len(current) == 2 * n:
            result.append(current)
            return result
    
        if open_used < n:
            self.backtrack(current + "(", open_used + 1, close_used,n, result)
    
        if close_used < open_used:
            self.backtrack(current + ")", open_used, close_used + 1,n, result)



    
    
