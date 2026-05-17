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