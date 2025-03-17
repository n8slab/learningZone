"""
Given a number n, we need to print its table. 

Examples : 

Input:  5
Output: 
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

I'll be using the iterative approach by using a loop to calculate and print the number and numbers in rage from 1-10
"""

# Take in number N
n = int(input("Hello and welcome!\n Pick a whole number and I'll give you its multiplication table: "))

# Use loop to print 
for i in range(1, 11):
    print(n, "*", i, "=", n*i)
