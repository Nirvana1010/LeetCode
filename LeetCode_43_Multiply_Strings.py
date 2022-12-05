class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = 0
        for i in range(n-1, -1, -1):
            digit = int(num2[i])
            product = 0
            for j in range(m-1, -1, -1):
                product += int(num1[j]) * digit * 10 ** (m-1-j)
            result += product * 10 ** (n-1-i)
        return str(result)