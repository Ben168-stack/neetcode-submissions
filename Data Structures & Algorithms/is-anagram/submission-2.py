class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for x,y in list(zip(s,t)):
            if x not in hash_s:
                hash_s[x] = 1
            else:
                hash_s[x] += 1
            if y not in hash_t:
                hash_t[y] = 1
            else:
                hash_t[y] += 1
        

        for i_s, i_t in zip(sorted(hash_s),sorted(hash_t)):
            print(hash_s)
            print(hash_t)
            if i_s not in hash_t or i_t not in hash_s:
                return False
            elif (hash_s[i_s] != hash_t[i_t]):
                return False
        return True


