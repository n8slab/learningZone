# Input and Output
<!--  ```python

```

Output
```

``` --> 

## Taking Input 
Use the Python [input() Function](https://www.geeksforgeeks.org/python-3-input-function/) to take user input.
Example:
```python
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
```

Output
```
Enter your name: John
Hello, John ! Welcome!
```

## Printing Variables
```python
# Single variable
mouse = "Jerry"
print(mouse)

# Multiple vars
cat = "Tom"
age = 100
location = "Warner Bros Studios"
print(cat, age, location)
```

Output
```
Jerry
Tom 100 Warner Bros Studios
```

## Take Multiple Inputs
```python
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
```

Output
```
Enter two values: 5 10
Number of boys:  5  
Number of girls:  10
Enter three values: 5 10 15
Total number of students:  5
Number of boys is :  10     
Number of girls is :  15 
```
> For more info on the split() method, [click here](https://www.geeksforgeeks.org/python-string-split/)

## Take Conditional Input From User
```python
# Prompting the user for input
age_input = input("Enter your age: ")

# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

Output
```
Enter your age: 21
You are an adult.
```

## How to Change Input Type (Typecasting)
Python's default input() function takes user input as a string. To take in as an int, float, etc you have to typecast it first.

**Ex. 1: Print Names**
```python
# Taking input as string
name = input("What is your name?: \n")
print(name)
```

Output
```
What is your name?: 
Nate
Nate
``` 
## Printing Numbers (int and float)
```python
# Taking input and Typecasting to int
n = int(input("How many cups do you have?: "))
print(n)

# Taking input and Typecasting to float
price = float(input("How much does each cup cost?: "))
print(price)
```

Output
```
How many cups do you have?: 10
10

How much does each cup cost?: 19.99
19.99
``` 

## Find Data Type of Input
```python
a = "Hello World"
b = 10
c = 11.22
d = ("Who", "are", "you")
e = ["You", "Es", "Aye"]
f = {"Dog": 1, "Cat":2, "Bird":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
```

Output
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'tuple'>
<class 'list'>
<class 'dict'>
```

## Output Formatting

### Using Format()
**Ex. 1**
```python
amount = 199.99
print("Amount: ${:.2f}".format(amount))
```

Output
```
Amount: $199.99
```

**Ex. 2** Using sep and end
```python
# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")


# Seprating with Comma
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')
```

Output
```
Python@GeeksforGeeks
GFG
09-12-2016
pratik@geeksforgeeks
```

**Ex. 3** Using f-string
```python
name = 'John'
age = 44
print(f"Hello, My name is {name} and I'm {age} years old.")
```

Output
```
Hello, My name is John and I'm 44 years old.
```
**Ex. 4** Using % Operator
% values are replaced with zero or more value of elements. (like printf in C)
- %d –integer
- %f – float
- %s – string
- %x –hexadecimal
- %o – octal

```python
# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" %add)

```

Output
```
Enter a value: 50
The sum is 55
```

