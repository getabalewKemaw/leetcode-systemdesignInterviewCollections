class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # n=len(s)
        # result=[]
        # for i  in range(0,n,2*k):
        #     first_k=s[i:i+k]
        #     next_k=s[i+k:i+2*k]
        #     result.append(first_k[::-1]+next_k)
        # return "".join(result)

        # Two pointwe approach
        m=list(s)
        n=len(m)
        for i in range(0,n,2*k):
            left=i
            right=min(i+k-1,n-1)
            while left<right:
                m[left],m[right]=m[right],m[left]
                left+=1
                right-=1
        return "".join(m)



       


        