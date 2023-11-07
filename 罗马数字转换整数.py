# s = "abc"
# print(s)
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[-1])
# print(s[-2])
class Solution:
    def romanToInt(self, s):
        ROMAN = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        if s == "":
            return 0
        index = len(s) - 2
        sum = ROMAN[s[-1]] #the last position num
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum
#main
temp = Solution()
string1 = input("string1: ")
print("string1 is ",string1)
print("the result is ", temp.romanToInt(string1))
