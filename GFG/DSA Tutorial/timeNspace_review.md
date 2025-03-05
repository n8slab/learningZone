# Time & Space Complexities Quick Review

Time/Space complexity analysis focuses on measuring the performance of algorithms. Goal is to measure **order of growths**

## Time Complexity
**Time Complexity** of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input (this is **NOT** the actual execution time of the machine its running on). So basically, Time Complexity is **the time required by the algorithm to solve a given problem.** 

To caclculate time complexity, we need to consider the cost of each fundamental command and the number of times the command is executed.

Example 1: Adding two scalar variables.
```
Algorithm ADD SCALAR(A, B)
//Description: Perform arithmetic addition of two numbers
//Input: Two scalar variables A and B
//Output: variable C, which holds the addition of A and B
C <- A + B
return C
```
The addition of two scalar numbers requires one addition operation. the time complexity of this algorithm is constant, so T(n) = O(1) .

