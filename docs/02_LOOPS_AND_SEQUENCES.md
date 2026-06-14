# Topic 2: Loops and Sequences

**Summary of content:**

- [Topic 2: Loops and Sequences](#topic-2-loops-and-sequences)
  - [1. Sequence Types: Lists and Tuples](#1-sequence-types-lists-and-tuples)
    - [1.1. Lists](#11-lists)
      - [A. Introduction \& Basics](#a-introduction--basics)
      - [B. Accessing Elements (Indexing \& Slicing)](#b-accessing-elements-indexing--slicing)
      - [C. Mutability \& Structuring Mechanics](#c-mutability--structuring-mechanics)
      - [D. Core List Methods](#d-core-list-methods)
    - [1.2. List Performance Reference (Time \& Space Complexity)](#12-list-performance-reference-time--space-complexity)


---


## 1. Sequence Types: Lists and Tuples

### 1.1. Lists

#### A. Introduction & Basics

In Python, a list is an **ordered** collection of items that can hold elements of **any data type** (including strings, numbers, booleans, or even other lists). Lists are **mutable** (modifiable after creation) and utilize a **zero-based** indexing system.

- **Creating Lists Using the Bracket Literal `[]` vs. the `list()` Constructor**

```python
# Using bracket literal []
cities = ['Los Angeles', 'London', 'Tokyo']
print(type(cities))  # Output: <class 'list'>

# Using the list() constructor to convert an iterable (like a string)
string = 'hello'
chars = list(string)
print(type(chars))  # Output: <class 'list'>
print(chars)        # Output: ['h', 'e', 'l', 'l', 'o']
```

- **Finding the Length of a List (`len()` function)**

```python
cities = ['Los Angeles', 'London', 'Tokyo']
print(len(cities))  # Output: 3
```

- **Checking if an Element Exists in a List (`in` and `not in` operators)**

```python
cities = ['Los Angeles', 'London', 'Tokyo']
print('Los Angeles' in cities)    # Output: True
print('New York' not in cities)   # Output: True
```

#### B. Accessing Elements (Indexing & Slicing)

- **Accessing Elements (Zero-based tracking):** Access an element by referencing its position inside square brackets, starting at `0`.

```python
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0])  # Output: Los Angeles
print(cities[2])  # Output: Tokyo
```

- **Negative Indexing:** Access elements from the end of the list backward. Index `-1` represents the last item.

```python
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[-1])  # Output: Tokyo
print(cities[-3])  # Output: Los Angeles
```

- **Index Out of Range Error:** Accessing a positive or negative index that is out of bounds for the list raises an `IndexError`.

```python
cities = ['Los Angeles', 'London', 'Tokyo']
# print(cities[5])  # Raises IndexError: list index out of range
```

- **Slicing Lists:** Extract a sub-list via the slice operator `:` using `list[start:stop]`. This captures elements from `start` up to, but excluding, `stop`.

```python
cities = ['Los Angeles', 'London', 'Tokyo', 'Paris', 'New York']
print(cities[1:4])  # Output: ['London', 'Tokyo', 'Paris']
print(cities[:2])   # Output: ['Los Angeles', 'London'] (start is omitted, defaults to 0)
print(cities[3:])   # Output: ['Paris', 'New York'] (stop is omitted, defaults to the end of the list)
```

- **Step Intervals:** Provide a third argument (`list[start:stop:step]`) to determine the increment between indices. A negative step of `-1` reverses the list.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:4])    # Output: [2, 3] (step is omitted, defaults to 1; stops before index 4)
print(numbers[2:8:2])  # Output: [2, 4, 6]
print(numbers[::3])    # Output: [0, 3, 6, 9]
print(numbers[::-1])   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

💡 **Interview Note — Slice Mutability: Can a sliced sub-list modify the original list?**

**Short Answer:** No. In Python, slicing a list creates a **shallow copy**. It allocates completely new memory for the sub-list structure. Because it is a new list object, modifying the sub-list (like changing an element, appending, or deleting) will not affect the original list.

```python
original = [1, 2, 3, 4, 5]
sub_list = original[1:4]  # Creates a brand new list: [2, 3, 4]

sub_list[0] = 99          # Modify the sub-list
print(sub_list)           # Output: [99, 3, 4]
print(original)           # Output: [1, 2, 3, 4, 5] (Original is completely untouched!)
```

- ⚠️ **The Interview Trap (Advanced Nuance):** If the list contains nested mutable objects (like a list inside a list), the slice copies the **references** to those inner objects. Modifying a primitive item inside the slice won't affect the original, but modifying a nested object *will* affect both, because both lists still point to that same inner object in memory.

---

#### C. Mutability & Structuring Mechanics

- **List Mutability:** Modify an element directly in place via index.

```python
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

- **Unpacking Values:** Assign elements of a list directly to multiple individual variables in a single expression. The number of variables must match the exact length of the list.

```python
coordinates = [10, 20, 30]
x, y, z = coordinates
print(x, y, z)  # Output: 10 20 30
```

- **Collecting Remaining Items (Extended Unpacking):** Use the wildcard star operator (`*`) during unpacking to capture all unassigned remaining elements into a separate sub-list.

```python
scores = [95, 88, 72, 64, 50]
highest, second, *remaining = scores
print(highest)    # Output: 95
print(second)     # Output: 88
print(remaining)  # Output: [72, 64, 50] (captures the remaining elements)
```

- **Nesting Lists:** Place lists inside other lists to form complex or multidimensional data structures (like a matrix). Access inner values by chaining index brackets sequentially (`[row][column]`).

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[0])     # Output: [1, 2, 3] (accesses the first row list)
print(matrix[1][2])  # Output: 6 (accesses row index 1, column index 2)
```

#### D. Core List Methods

**Adding Elements**

- `append(item)`: Adds a single element to the very end of the list.

```python
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

- **Appending Lists vs. Combining Lists:** Appending a list inside another list creates a nested structure. To combine elements flatly without nesting, use `.extend(iterable)` or the `+` operator.

```python
# Appending a list (nested structure)
nums1 = [1, 2]
nums1.append([3, 4])
print(nums1)  # Output: [1, 2, [3, 4]]
```

- `extend(iterable)`: Iterates through a collection (like another list) and adds each element individually to the end.

```python
nums2 = [1, 2]
nums2.extend([3, 4])
print(nums2)  # Output: [1, 2, 3, 4]
```

- `insert(index, item)`: Inserts an item at a specified `index`, shifting all subsequent elements to the right.

```python
languages = ['Python', 'Go', 'C++']
languages.insert(1, 'JavaScript')
print(languages)  # Output: ['Python', 'JavaScript', 'Go', 'C++']
```

---

💡 **Interview Note — `.extend()` vs loop `.append()`, which is faster?**

**Short Answer:** `.extend()` is significantly faster. While both operations achieve the same result and run in $O(k)$ time overall (where $k$ is the number of elements being added), `.extend()` is highly optimized at the C-level in CPython for two reasons:

1. **Memory Pre-allocation (Overallocation):**
   - When you use a loop with `.append()`, Python has to guess how much memory to allocate. If the list grows too large, Python is forced to pause, allocate a larger block of memory, copy the old elements over, and then resume appending. It might have to do this multiple times during a loop.
   - `.extend()` knows the exact size of the incoming collection upfront and can request the correct amount of memory from the OS **once**.

2. **C-Loop vs. Python-Loop Overhead:**
   - A standard `for` loop running `.append()` executes bytecode instructions in the Python virtual machine for every single iteration.
   - `.extend()` moves the entire looping mechanism down to highly optimized C code, completely bypassing Python interpreter overhead.

```python
my_list = [0, 1]
nums = [2, 3]

# SLOWER: Python interpreter loop + multiple memory reallocations
for num in nums:
    my_list.append(num)

# FASTER: Single C-level execution + single memory allocation
my_list.extend(nums)
```

---

**Removing Elements**

- `remove(item)`: Searches for and removes the first occurrence of a specific value. Raises a `ValueError` if the item is not found.

```python
items = ['a', 'b', 'c', 'b']
items.remove('b')
print(items)  # Output: ['a', 'c', 'b']
```

- `pop(index)`: Removes and returns the item at a specified index. If no index is provided, it defaults to `-1` (the last item).

```python
letters = ['x', 'y', 'z']
popped_item = letters.pop(1)
print(popped_item)  # Output: y
print(letters)      # Output: ['x', 'z']

last_item = letters.pop()
print(last_item)    # Output: z
print(letters)      # Output: ['x']
```

- `clear()`: Removes all elements from the list, leaving it completely empty.

```python
data = [10, 20, 30]
data.clear()
print(data)  # Output: []
```

**Searching & Ordering Elements**

- `index(item)`: Returns the zero-based index of the **first** occurrence of a specified value. Raises a `ValueError` if the value is missing.

```python
colors = ['red', 'blue', 'green', 'blue']
print(colors.index('blue'))  # Output: 1
```

- `reverse()`: Reverses the elements of the list **in place**, permanently changing the original list.

```python
letters = ['a', 'b', 'c']
letters.reverse()
print(letters)  # Output: ['c', 'b', 'a']
```

- **The `.sort()` Method vs. the `sorted()` Function:**
  - `.sort()` is a list method that mutates the original list in place and returns `None`.
  - `sorted(iterable)` is a *built-in* function that accepts any iterable and returns a brand-new sorted list, leaving the original completely unchanged.

```python
# Using the .sort() method (in place)
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]

# Using the sorted() function (creates a copy)
original = [5, 4, 6]
new_sorted = sorted(original)
print(original)    # Output: [5, 4, 6] (unchanged)
print(new_sorted)  # Output: [4, 5, 6] (new list)
```

### 1.2. List Performance Reference (Time & Space Complexity)

Let $n$ represent the total number of elements currently in the list, and $k$ represent the size of a sub-segment, slice, or incoming iterable.

| Operation | Time | Space | Behavior & Memory Impact |
| :--- | :--- | :--- | :--- |
| **Adding** | | | |
| `.append(item)` | $O(1)$ | $O(1)$ | Modifies in-place. Runs in **amortized** constant time; a worst-case $O(n)$ memory reallocation occurs rarely when the dynamic array buffer fills up. |
| `.extend(iterable)` | $O(k)$ | $O(1)$ | Modifies in-place; loops through the $k$ elements of the incoming collection at the C-level, triggering a single pre-allocated overallocation buffer tweak if needed. |
| `.insert(index, item)` | $O(n)$ | $O(1)$ | Modifies in-place; shifts items to the right to clear a spot. |
| **Removing** | | | |
| `.pop()` (from end) | $O(1)$ | $O(1)$ | Modifies in-place; drops the final element instantly. |
| `.pop(index)` / `remove(item)` | $O(n)$ | $O(1)$ | Modifies in-place; shifts items to the left to close the gap. |
| **Searching & Ordering** | | | |
| `item in list` / `.index(item)` | $O(n)$ | $O(1)$ | Linear scan; requires zero additional memory overhead. |
| `.reverse()` | $O(n)$ | $O(1)$ | Reverses elements directly in-place. |
| `.sort()` | $O(n \log n)$ | $O(n)$ | Sorts in-place, but **Timsort** requires up to $O(n)$ temporary space for merging. |
| `sorted(list)` | $O(n \log n)$ | $O(n)$ | **Allocates a new list** of size $n$ to store and return the sorted results. |
| **Accessing & Slicing** | | | |
| `list[i]` (indexing) | $O(1)$ | $O(1)$ | Constant lookup; direct access via memory address. |
| `list[start:stop]` (slicing) | $O(k)$ | $O(k)$ | **Allocates new memory** to hold and return the copied $k$ elements. |
