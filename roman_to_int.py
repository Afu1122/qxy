class Solution(object):
    def romanToInt(self, s):
        roman_map={
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        total=0
        pre_num=0
        for i in range(len(s)-1,-1,-1):
            current_num=roman_map[s[i]]
            if current_num <pre_num:
                total-=current_num
            else :
                total+=current_num
            pre_num=current_num
        return total