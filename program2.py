def decode_message(s: str, p: str) -> bool:
    memo = {}

    def match_helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j == len(p):
            return i == len(s)
        
        if j < len(p) and p[j] == '*':
            result = match_helper(i, j + 1) or (i < len(s) and match_helper(i + 1, j))
            memo[(i, j)] = result
            return result
        
        if i < len(s) and (p[j] == '?' or p[j] == s[i]):
            result = match_helper(i + 1, j + 1)
            memo[(i, j)] = result
            return result
        
        memo[(i, j)] = False
        return False

    return match_helper(0, 0)
