class Solution(object):
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for ch in reversed(s):
            current_value = values[ch]

            if current_value < prev_value:
                
                total=total-current_value
            else:
                total=total+current_value

        prev_value = current_value

        return total   

i = input("Enter a roman numeral: ")
obj = Solution()
print("The integer value is:", obj.romanToInt(i))
