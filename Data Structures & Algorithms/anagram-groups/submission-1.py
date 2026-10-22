class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_hash_map = {}
        
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            
            if tuple(count) in anagrams_hash_map:
                anagrams_hash_map[tuple(count)].append(word)
            else:
                anagrams_hash_map[tuple(count)] = [word]
        return list(anagrams_hash_map.values())
        
                
               


        

        
        