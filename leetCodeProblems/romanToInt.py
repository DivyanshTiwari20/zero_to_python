class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary with Roman numeral values
        romantoInt = {
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
        
        # Iterate over the Roman numeral string from end to start
        for char in reversed(s):
            value = romantoInt[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total

# Example usage:
solution = Solution()

print(solution.romanToInt("MCMXCIV"))  # Output: 1994
