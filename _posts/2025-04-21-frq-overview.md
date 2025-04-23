---
layout: post
title: FRQ Overview
comments: true
---

# There are four main types of CSA FRQ question.

## 1. Methods and Control Structures

- Write a method using loops, conditionals, and basic logic
- Often involves iterating over arrays or conditionally processing input

**Example:**
```java
public int countPositives(int[] arr) {
  int count = 0;
  for (int num : arr) {
    if (num > 0) count++;
  }
  return count;
}
```

### ✅ Tips:
- Pay close attention to loop boundaries and conditional logic
- Make sure to return the expected value
- Use enhanced for-loops when possible for clarity

### ❌ Common Mistakes:
- Off-by-one errors in loops
- Incorrect logic in conditionals
- Forgetting to initialize variables

### Practice!
- [2015 FRQ Question #4](https://secure-media.collegeboard.org/digitalServices/pdf/ap/ap15_frq_computer_science_a.pdf)

---

## 2. Classes

- Write or complete a class with fields, constructors, and methods
- Focus on object-oriented design: encapsulation, constructors, and method behaviors

**Example:**
```java
public class Book {
  private String title;
  private int pages;

  public Book(String t, int p) {
    title = t;
    pages = p;
  }

  public int getPages() {
    return pages;
  }

  public void addPages(int morePages) {
    pages += morePages;
  }
}
```

### ✅ Tips:
- Use `private` for fields, and provide `public` getters/setters
- Follow constructor signature exactly
- Avoid hardcoding values inside methods unless required

### ❌ Common Mistakes:
- Forgetting to initialize fields in the constructor
- Not using `this.` when necessary
- Incorrect return types or missing return statements

### Practice!
- [2023 FRQ Question #2](https://apcentral.collegeboard.org/media/pdf/ap23-frq-comp-sci-a.pdf)

---

## 3. Array / ArrayList

- Work with 1D arrays, 2D arrays, or `ArrayList` objects
- Common tasks: traversal, insertion, deletion, searching

**Example:**
```java
public int countLongWords(ArrayList<String> words) {
  int count = 0;
  for (String word : words) {
    if (word.length() > 5) {
      count++;
    }
  }
  return count;
}
```

### ✅ Tips:
- Use enhanced for-loops for clarity
- Use `.get(i)` for `ArrayList`, `array[i]` for arrays
- Understand 2D array row/column structure: `array[row][col]`

### ❌ Common Mistakes:
- Index out-of-bounds errors
- Confusing `.get(i)` with `[i]`
- Not updating the list/array properly during iteration

### Practice!
- [2022 FRQ Question #3](https://apcentral.collegeboard.org/media/pdf/ap22-frq-computer-science-a.pdf)

---

## 4. 2D Array

- Work with nested loops to process 2D arrays
- Focus on row/column logic and element access

**Example:**
```java
public int sumEvenValues(int[][] matrix) {
  int sum = 0;
  for (int row = 0; row < matrix.length; row++) {
    for (int col = 0; col < matrix[row].length; col++) {
      if (matrix[row][col] % 2 == 0) {
        sum += matrix[row][col];
      }
    }
  }
  return sum;
}
```

### ✅ Tips:
- Loop over `row`, then `col` (nested loop)
- Always use `matrix[row].length` for column length
- Draw out a matrix to help visualize iteration

### ❌ Common Mistakes:
- Mixing up rows and columns
- Hardcoding dimensions (like using `[3][3]`)
- Forgetting to return the result or initialize the accumulator

### Practice!
- [2023 FRQ Question #4](https://apcentral.collegeboard.org/media/pdf/ap23-frq-comp-sci-a.pdf)