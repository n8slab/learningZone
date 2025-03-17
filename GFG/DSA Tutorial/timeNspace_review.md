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
The addition of two scalar numbers requires one addition operation. the time complexity of this algorithm is constant, so **T(n) = O(1)** .

To calculate time complexity on an algorithm, it is assumed that a **constant time c** is taken to execute one operation, and then the total operations for an input length on N are calculated.

Example 2: Suppose you're trying to find whether a pair **(X, Y)** exists in an array, A of **N** elements whose sum is **Z**. The simplest idea would be to consider every pair and check if it satisfies the given condition or not.

- The following pseudo-code helps us visualize this:
```
int a[n];
for(int i = 0;i < n;i++)
  cin >> a[i]
  
for(int i = 0;i < n;i++)
  for(int j = 0;j < n;j++)
    if(i!=j && a[i]+a[j] == z)
       return true
return false
```
The following is how to code it in Java:
```java
import java.lang.*;
import java.util.*;

class GFG{

// Function to find a pair in the given
// array whose sum is equal to z
static boolean findPair(int a[], int n, int z)
{
    
    // Iterate through all the pairs
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
        
            // Check if the sum of the pair
            // (a[i], a[j]) is equal to z
            if (i != j && a[i] + a[j] == z)
                return true;

    return false;
}

// Driver code
public static void main(String[] args)
{
    
    // Given Input
    int a[] = { 1, -2, 1, 0, 5 };
    int z = 0;
    int n = a.length;
    
    // Function Call
    if (findPair(a, n, z))
        System.out.println("True");
    else
        System.out.println("False");
}
}

// This code was sampled via GeeksForGeeks . org
// This code sample is for educational purposes only
```
Output:
```
False
```
Now, let's assume each operation takes a constant time, C, and the number of lines executed actually depends on the value of Z (sum of X,Y). When analyzing the algorithm for complexity, we mostly use the worst case scenario. In our case, this would be when there are no pair of elements with the sum of Z.
In the WORST case,
- **N*C** (Num elements in array * operation time) operations are required for input
- The outer loop (i loop) runs **N** times
- For each i, the inner j loop runs **N** times

This means our total execution time = **(N*C)  + (N * N * C) + C**
Now, we need to ignore the lower order terms since they are relatively insignificant for large input, so only the hightest order term is taken (without constant). In our case, this would be **N*N**. 
```
First, take out the value of C from the above function
(N*C)  + (N * N * C) + C --> N + N^2 

Then, take the highest order term
N + N^2 --> N^2
```
Different notations are used to describe a function's limiting behavior, but since the worst case is taken we will be using big-O notation to represent the time complexity.

That being said, the time complexity is **O($N^2$)** for the above algorition.

> Note that the time complexity is solely based on the number of elements in array A i.e the input length, so if the length of the array will increase the time of execution will also increase.

**Order of Growth** is how the time of execution depends on the length of the input. In the above example, the time of execution of the quadratically depends on the length of the array. (Remember calculus derivatives/integrals? Thats a great way to better understand it)