# Python Core Concepts & Study Journal

**Summary of Topics:**

- [Python Core Concepts \& Study Journal](#python-core-concepts--study-journal)
  - [I. Python Basics](#i-python-basics)
    - [1. Variables](#1-variables)
      - [Declaring Variables](#declaring-variables)
      - [Naming Conventions \& Constraints](#naming-conventions--constraints)
    - [2. Comments](#2-comments)
      - [Single Line Comments](#single-line-comments)
      - [Multi-line "Comments" (Docstrings)](#multi-line-comments-docstrings)
    - [3. Data Types and Mutability](#3-data-types-and-mutability)
      - [3.1. Immutable Types (Cannot be changed)](#31-immutable-types-cannot-be-changed)
      - [3.2. Mutable Types (Can be changed)](#32-mutable-types-can-be-changed)
    - [4. Working with Strings](#4-working-with-strings)
      - [4.1. Core Operations](#41-core-operations)
      - [4.2. Membership and Methods](#42-membership-and-methods)
      - [4.3. The Performance Pitfall: Concatenation](#43-the-performance-pitfall-concatenation)
    - [5. Common Operations used with Integers and Floats](#5-common-operations-used-with-integers-and-floats)
      - [5.1. Basic Math Operations](#51-basic-math-operations)
      - [5.2. Modulo Operator (%)](#52-modulo-operator-)
      - [5.3. Floor Division (//)](#53-floor-division-)
      - [5.4. Exponentiation Operator (\*\*)](#54-exponentiation-operator-)
      - [5.5. `int()` and `float()` Functions](#55-int-and-float-functions)
      - [5.6. Rounding, Floor, and Ceiling Functions](#56-rounding-floor-and-ceiling-functions)
      - [5.7. `abs()` and `pow()` Functions](#57-abs-and-pow-functions)
    - [6. Augmented Assignments](#6-augmented-assignments)
    - [7. Working with Functions](#7-working-with-functions)
      - [7.1. Basic Function Structure](#71-basic-function-structure)
      - [7.2. Common Built-in Functions](#72-common-built-in-functions)
      - [7.3. Parameters vs. Arguments](#73-parameters-vs-arguments)
      - [7.4. Types of Arguments](#74-types-of-arguments)
    - [8. Scope in Python](#8-scope-in-python)
      - [8.1. The LEGB Rule](#81-the-legb-rule)
      - [8.2. Reading vs. Modifying Variables](#82-reading-vs-modifying-variables)
      - [8.3. The `global` and `nonlocal` Keywords](#83-the-global-and-nonlocal-keywords)


## I. Python Basics

### 1. Variables

#### Declaring Variables

To declare a variable, use the assignment operator (`=`) to bind a value to a name. Python uses **Dynamic Typing**, meaning variables are not tied to a specific data type and can be reassigned to different types during execution.

```python
full_name = "Python Variables"
```

#### Naming Conventions & Constraints

Python follows specific rules for identifiers. Violating these will trigger a `SyntaxError`.

| Rule               | Description                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| Starting Character | Must be a letter or an underscore (`_`), not a number.                                    |
| Allowed Characters | Only alphanumeric characters (a-z, A-Z, 0-9) and underscores.                             |
| Case Sensitivity   | `age`, `Age`, and `AGE` are all considered unique.                                        |
| Reserved Keywords  | Cannot use Python's built-in keywords (e.g., `if`, `class`, or `def`).                    |
| Pythonic Style     | Use **snake_case** (lowercase words separated by underscores) to follow PEP 8 guidelines. |


### 2. Comments

#### Single Line Comments

Created using the hash symbol (`#`). Python ignores everything from the # to the end of the line.
```python
# Set the user's initial score to zero
```

#### Multi-line "Comments" (Docstrings)

Python doesn’t have a specific syntax for multi-line comments. Instead, triple-quoted strings (`"""` or `'''`) are used.

> **How it works:** If these strings are not assigned to a variable or placed immediately after a function/class definition, Python treats them as expressions and ignores them during execution.

**Best Practice:** For actual multi-line comments, use `#` on every line to stay strictly PEP 8 compliant.

```python
'''
This is a 
multi-line comment.
'''

# This is a
# multi-line comment (recommended approach).
```


### 3. Data Types and Mutability

#### 3.1. Immutable Types (Cannot be changed)
If you modify an immutable object, Python creates a new object in memory with the new value.
- `int` / `float` / `complex`: Numeric values (e.g., `5`, `3.14`).
- `str`: Strings (e.g., `'Hello'`).
- `bool`: Boolean values (`True` or `False`).
- `tuple`: An ordered, unchangeable collection (e.g., `(1, 2, 3)`).

#### 3.2. Mutable Types (Can be changed)
These objects can be modified **"in-place"** without creating a new object in memory.
- `list`: An ordered, changeable collection (e.g., `[1, 2, 3]`).
- `dict`: A collection of key-value pairs (e.g., `{'name': 'John'}`).
- `set`: An unordered collection of unique items (e.g., `{2, 1, 3}`).

---
💡 **Interview Insight: Tuples vs. Lists**

**Question**: If Lists and Tuples both store collections, why use Tuples?

**Answer**:
- **Immutability (Safety)**: Tuples are **"read-only."** This prevents accidental data modification and side effects.
- **Performance (Efficiency)**: Tuples are **statically allocated**. Because their size is fixed, Python allocates the exact memory needed. In contrast, Lists are dynamically resized and require a "memory buffer" (over-allocation) to handle growth, making them heavier and slower to create than tuples.
---


### 4. Working with Strings

#### 4.1. Core Operations

**Length (`len()`)**: Returns the total count of characters in a string.
```python
print(len("abc"))  # Output: 3
```

**Character Indexing**: Access individual characters using `[index]`.
- Positive Indexing: `s[0]` (first character)
- Negative Indexing: `s[-1]` (last character)

**Slicing (`[start:stop:step]`)**: Extracts a portion of a string. The `stop` index is **exclusive** (not included).
```python
s = "Hello World"

# If start is omitted, it defaults to 0
print(s[:5])  # Output: "Hello"

# If stop is omitted, it defaults to the end of the string
print(s[6:])  # Output: "World" (Index 5 was the space)

# step defaults to 1 if omitted
print(s[0:5]) # Output: "Hello"
print(s[0:5:2]) # Output: "Hlo"
```

**Pythonic Reverse**: `s[::-1]` is the standard idiom for reversing a string.
```python
s = "abc"
print(s[::-1]) # Output: "cba"
```

**Escape Characters**: Use backslashes (`\`) to include special characters like quotes or new lines.
```python
print('I\'m learning Python.') # Output: "I'm learning Python."
```

**f-strings (Interpolation)**: The modern way to embed expressions inside string literals using `{}`.
```python
val = 2.1234
print(f"Value: {val:.2f}") # Output: "Value: 2.12"
```

#### 4.2. Membership and Methods

**The `in` Operator**: Returns True if a substring exists within a string.
```python
is_found = "Py" in "Python"  # is_found = True
```

**Common Methods**:
- `.strip()`: Removes all leading and trailing whitespace (spaces, tabs, newlines).
- `.lower()` / `.upper()`: Converts the string to all lowercase or uppercase.
- `.split(sep)`: Splits the string into a list based on the separator (sep). If sep is not provided, it splits by any whitespace.
- `.join(iterable)`: Joins elements of a list (or other iterable) into a single string. This is the standard way to concatenate multiple strings efficiently.

#### 4.3. The Performance Pitfall: Concatenation

Because strings are immutable, using the `+` operator in a loop forces Python to create a new object and copy all existing data during every iteration. This leads to $O(n^2)$ time complexity.

> 💡 **The Pro Fix**: Accumulate substrings in a `list`, then use `''.join(list)` at the end. This achieves $O(n)$ (linear) complexity because Python calculates the total memory needed once and performs a single join operation.

```python
# AVOID (Slow: O(n^2))
s = ""
for word in ["a", "b", "c"]:
    s += word 

# PREFER (Fast: O(n))
words = ["a", "b", "c"]
s = "".join(words)
```


### 5. Common Operations used with Integers and Floats

#### 5.1. Basic Math Operations

Standard operators follow the order of operations (PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).

```python
# +, -, *: Work as expected.
# / (True Division): Always returns a Float, even if the result is a whole number.
print(10 / 2)  # Output: 5.0
```

#### 5.2. Modulo Operator (%)

Returns the remainder of a division. This is a critical tool in logic building.

```python
print(10 % 3)  # Output: 1 (Because 3 goes into 10 three times with 1 left over)
```

**Common Use Case**: Checking if a number is even (`num % 2 == 0`) or odd.

#### 5.3. Floor Division (//)

Divides two numbers and rounds down to the nearest whole number (integer). It truncates or "chops off" the decimal part for positive numbers.

```python
print(10 // 3)   # Output: 3
print(-10 // 3)  # Output: -4 (Careful! It rounds down toward negative infinity)
```

#### 5.4. Exponentiation Operator (**)

Calculates the power of a number.

```python
print(2 ** 3)  # Output: 8 (2 * 2 * 2)
```

#### 5.5. `int()` and `float()` Functions

These are used for **Type Casting** (converting one data type to another).

- `int(value)`: Converts a value to an integer. If converting a float, it truncates (chops off) the decimal toward zero
- `float(value)`: Converts a value to a floating-point number.

```python
print(int(3.9))    # Output: 3
print(int("10"))   # Output: 10

print(float(5))      # Output: 5.0
print(float("3.14")) # Output: 3.14
```

#### 5.6. Rounding, Floor, and Ceiling Functions

`round(number, ndigits)`: Rounds a number to the nearest integer or specified decimal places.

```python
print(round(3.14159, 2))  # Output: 3.14
```

⚠️ **The "Banker's Rounding" Rule**: If a number is exactly halfway between two integers (e.g., `.5`), Python rounds to the nearest **even** number.

```python
print(round(2.5))  # Output: 2
print(round(3.5))  # Output: 4
```

**Why?** This reduces cumulative rounding errors in large financial datasets by averaging rounds up and down equally over time.

**Advanced Rounding (`math` module):**
Requires importing Python's built-in `math` library.
- `math.floor(number)`: Always rounds down to the nearest whole number.
- `math.ceil(number)`: Always rounds up to the nearest whole number.

```python
import math

print(math.floor(3.9))  # Output: 3
print(math.ceil(3.1))   # Output: 4
```

#### 5.7. `abs()` and `pow()` Functions

- `abs(number)`: Returns the absolute value (the positive distance from zero).
- `pow(base, exp)`: Returns the power of a number (the functional equivalent of `base ** exp`).

```python
print(abs(-5))    # Output: 5
print(pow(2, 3))  # Output: 8
```

---
**💡 Interview Gotcha: `int()` vs `math.floor()`**

While they yield the same results for positive numbers, they behave differently with negative values:

```python
print(int(-3.1))         # Output: -3 (Truncates toward zero)
print(math.floor(-3.1))  # Output: -4 (Rounds down toward negative infinity)
```
---


### 6. Augmented Assignments

Augmented assignment combines an arithmetic operation with a variable assignment into a single step. It modifies the variable **"in-place"** by applying the operation to its current value and saving the result back to that same variable.

```python
# Addition assignment
my_var = 10
my_var += 5
print(my_var)  # Output: 15

# Subtraction assignment
count = 14
count -= 3
print(count)  # Output: 11

# Multiplication assignment
product = 65
product *= 7
print(product)  # Output: 455

# Division assignment (always returns a float)
price = 100
price /= 4
print(price)  # Output: 25.0

# Floor Division assignment
total_pages = 23
total_pages //= 5
print(total_pages)  # Output: 4

# Modulo assignment
bits = 35
bits %= 2
print(bits)  # Output: 1

# Exponentiation assignment
power = 2
power **= 3
print(power)  # Output: 8
```

Python also supports augmented assignments for **Bitwise Operators**, which are used in low-level programming or performance optimization:
- `&=` (Bitwise AND assignment)
- `|=` (Bitwise OR assignment)
- `^=` (Bitwise XOR assignment)
- `>>=` (Bitwise Right Shift assignment)
- `<<=` (Bitwise Left Shift assignment)

---
💡 **Interview Tip: The Missing Increment Operator**

In languages like C++, Java, and JavaScript, you can increment a variable using `x++`. **Python does not support** `x++` or `x--`. To change a value by 1 in Python, you must explicitly use the augmented addition/subtraction operators:

```python
x = 5
x += 1  # Correct way to increment (x is now 6)
```
---


### 7. Working with Functions

#### 7.1. Basic Function Structure

Functions allow you to reuse code and keep your logic modular.

- **Definition**: Use the `def` keyword followed by the function name, parentheses `()`, and a colon.
- **The `return` Statement**: Explicitly sends a value back to the caller. If a function does not contain a `return` statement, it implicitly returns `None` by default.

```python
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)  # Output: "Hello, Alice!"
```

#### 7.2. Common Built-in Functions

Python provides a rich library of globally available functions:
- `type(object)`: Evaluates and returns the exact data type of an object.
- `print(*objects)`: Outputs data to the system console.

```python
print(type(10))  # Output: <class 'int'>
```

#### 7.3. Parameters vs. Arguments

While used interchangeably in casual conversation, these terms have distinct architectural meanings in software development:
- **Parameters**: The variable placeholders declared inside a function's signature (the definitions on the `def` line).
- **Arguments**: The real, concrete values supplied to the function when it is executed.

```python
def multiply(a, b):  # 'a' and 'b' are PARAMETERS
    return a * b

print(multiply(5, 10))  # 5 and 10 are ARGUMENTS (Output: 50)
```

#### 7.4. Types of Arguments

Python provides flexible mechanics for executing functions:
- **Positional Arguments**: Must be passed in the exact sequential order defined by the function parameters.
- **Keyword Arguments**: Arguments passed by name, allowing you to ignore the sequential order.
- **Default Parameters**: Allow fallback values directly inside the function signature. If the caller omits an argument, the default value kicks in.

```python
def division(a, b=1):
    return a / b

# 1. Positional Arguments (Order determines the result)
print(division(6, 3))    # Output: 2.0
print(division(3, 6))    # Output: 0.5

# 2. Default Parameter (Omitting 'b' uses the fallback value of 1)
print(division(5))       # Output: 5.0

# 3. Keyword Arguments (Explicitly named, so order doesn't matter)
print(division(b=3, a=6)) # Output: 2.0
```

---
💡 **Interview Note: Pass by Object Reference**

Python uses a **Pass by Object Reference** (also called *call-by-sharing*) approach. You are passing an object's reference (memory address), not the actual raw value.

- **Immutable Objects**: Cannot be modified. Any change inside the function creates a new object in memory, leaving the caller's original variable completely untouched.
- **Mutable Objects**: The function receives a reference. Modifying the object inside the function **mutates the original object**.
---


### 8. Scope in Python

#### 8.1. The LEGB Rule

When you reference a variable name, Python looks for it across four layers of scope. It uses the first match it finds:

- **L - Local**: Variables defined inside the current function.
- **E - Enclosing**: Variables inside any nested/outer function structures (relevant in closures and inner functions).
- **G - Global**: Variables defined at the top-most level of the script or module.
- **B - Built-in**: Keywords and functions pre-loaded by Python (e.g., `len`, `int`, `print`).

#### 8.2. Reading vs. Modifying Variables

- **Reading**: A function can freely read variables from outer scopes (Global or Enclosing) without requiring any special keywords.

- **Modifying**: A function cannot modify an outer variable directly. Attempting to reassign an outer variable inside a function causes Python to create a **new local variable** with that same name, shielding the original variable from changes.

```python
x = 10  # Global variable

def my_func():
    x = 5  # Creates a NEW local variable 'x'; does NOT change global 'x'
    print(f"Local x: {x}")

my_func()               # Output: Local x: 5
print(f"Global x: {x}") # Output: Global x: 10 (unaffected)
```

#### 8.3. The `global` and `nonlocal` Keywords

To explicitly modify a variable residing outside the local scope, you must declare your intent before mutating it:

- **`global`**: Informs Python that a variable belongs to the top-level (Global) scope.
- **`nonlocal`**: Informs Python that a variable inside a nested function belongs to an outer (Enclosing) function's scope.

```python
# 1. Using the global keyword
counter = 0

def increment_global():
    global counter
    counter += 1

increment_global()
print(counter)  # Output: 1

# 2. Using the nonlocal keyword (Nested Functions)
def outer_func():
    message = "Hello"

    def inner_func():
        nonlocal message
        message = "World"  # Modifies the variable in outer_func

    inner_func()
    print(message)  # Output: World

outer_func()
```

---
💡 **Interview Tip: Why Global Variables are an Anti-Pattern**

Excessive use of the `global` keyword is heavily penalized in interviews.
- **The Problem**: Global state makes code fragile and hard to debug because any function can unexpectedly mutate data from anywhere in the program.
- **The Solution**: Instead of using `global`, **pass the variable as an argument and explicitly return the updated value**. This keeps your functions isolated, predictable, and clean.
---
