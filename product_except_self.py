class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
    
        prefixp = 1
        postfix = 1
        print(prefixp)
        print(len(nums))
        
        for i in range(len(nums)):
            
            answer[i] = prefixp
            prefixp *= nums[i]
            print(f"prefix", prefixp)
        

        for i in range((len(nums)-1),-1,-1):
            answer[i] *= postfix
            postfix *= nums[i]
            print(f"psotifc",postfix)

        return answer


            

        