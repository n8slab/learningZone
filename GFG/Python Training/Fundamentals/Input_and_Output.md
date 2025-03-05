# Input and Output
<!--  ```python

```

Output
```

``` --> 
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
Enter a value: 50The sum is 55
```
