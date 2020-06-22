def containsDuplicate(self, nums: List[int]) -> bool:
        # store numbers seen as keys of a dictionary
        num_seen = {}
        
        # for each num in list
        for num in nums:
            
            # if num_seen has a key of num, there is a duplicate 
            if num in num_seen.keys():
                return True
            
            # otherwise add the key
            num_seen[num] = None
            
        # no duplicates were found
        return False