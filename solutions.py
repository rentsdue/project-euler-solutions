import math

#Problem 1: Find the sum of all the multiples of 3 or 5 below 1000.

def sumOfMultiples():
    sum = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

#Problem 2: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def evenTermsOfSequence():
    sum = 0
    num1 = 1
    num2 = 2
    while (num1 < 4000000):
        if num1 % 2 == 0:
            sum += num1
        nextNum = num1 + num2
        num1 = num2
        num2 = nextNum
    return sum

#Problem 3: Find the largest prime factor of 600851475143
def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True 
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def largestPrimeFactor(number):
    primeFactorList = []
    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0 and isPrime(num):
            primeFactorList.append(num)
    return primeFactorList[len(primeFactorList) - 1]

#Problem 4: Find the largest palindrome made from the product of two 3-digit numbers.

#Problem 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Problem 6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def diffBetweenSquares(n):
    sumOfSquares = 0
    for i in range(1, n + 1):
        sumOfSquares += i ** 2
    
    squareOfTotal = 0
    for i in range(1, n + 1):
        squareOfTotal += i
    squareOfTotal = squareOfTotal ** 2

    return squareOfTotal - sumOfSquares