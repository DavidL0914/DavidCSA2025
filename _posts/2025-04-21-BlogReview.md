---
layout: post
title: CSA Review
comments: true
---

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>CSA Unit Review</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }

    h1 {
      margin-bottom: 10px;
    }

    input[type="text"] {
      margin-bottom: 20px;
      padding: 6px;
      width: 300px;
      font-size: 14px;
    }

    .tag-buttons {
      margin-bottom: 20px;
    }

    .tag-buttons button {
      margin: 0 5px 10px 0;
      padding: 6px 10px;
      border: none;
      border-radius: 4px;
      background-color: #eee;
      cursor: pointer;
    }

    .tag-buttons button.active {
      background-color: #007bff;
      color: white;
    }

    .notecard {
      background-color: #f9f9f9;
      padding: 15px;
      margin: 15px 0;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      transition: background-color 0.3s;
    }

    .notecard:hover {
      background-color: #e9ecef;
    }

    .notecard-header {
      font-size: 1.2em;
      font-weight: bold;
      color: #333;
      cursor: pointer;
    }

    .notecard-body {
      font-size: 1em;
      color: #555;
      padding-left: 20px;
      display: none;
    }

    .notecard-body ul {
      list-style-type: none;
      padding-left: 0;
    }

    .notecard-body li {
      margin-bottom: 8px;
    }

    .search-container {
      margin-bottom: 20px;
    }

    .unit-header {
      font-weight: bold;
      font-size: 1.2em;
      color: #333;
    }

    .unit-content {
      margin-left: 20px;
      font-size: 1em;
      color: #666;
    }
  </style>
</head>
<body>

  <h1>CSA Unit Review</h1>

  <!-- Search Bar -->
  <input type="text" id="searchInput" placeholder="Search topics..." onkeyup="filterTopics()" />

  <!-- Tag-based Filtering -->
  <div class="tag-buttons">
    <button onclick="filterByTag('all')" class="active">All</button>
    <button onclick="filterByTag('loops')">Loops</button>
    <button onclick="filterByTag('arrays')">Arrays</button>
    <button onclick="filterByTag('methods')">Methods</button>
    <button onclick="filterByTag('classes')">Classes</button>
    <button onclick="filterByTag('recursion')">Recursion</button>
  </div>

  <!-- Unit Content (Notecards) -->
  <div id="checklist">

    <!-- Notecard Units -->
    {% for i in (1..10) %}
    <!-- Unit {{ i }} will be manually written below instead of looped -->
    {% endfor %}

    <!-- All Notecards below - updated to be clickable dropdowns -->
    <!-- Example below for one unit. All are updated the same way. -->

    <!-- Unit 1 -->
    <div data-tags="loops arrays" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 1: Primitive Types</div>
      <div class="notecard-body">
        <ul>
          <li>Integers, floats, booleans, and doubles</li>
          <li>Type conversion (casting between types)</li>
          <li>Overflow and underflow in integer types</li>
          <li>Floating-point precision (potential rounding errors)</li>
          <li>Use cases: loops, conditionals, comparisons</li>
        </ul>
      </div>
    </div>

    <div data-tags="loops arrays" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 2: Variables and Constants</div>
      <div class="notecard-body">
        <ul>
          <li>Variable scope: local, global, and instance variables</li>
          <li>Final variables (constants) and the `final` keyword</li>
          <li>Best practices for variable naming</li>
          <li>Memory management considerations for variables</li>
        </ul>
      </div>
    </div>

    <div data-tags="methods recursion" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 3: Operators</div>
      <div class="notecard-body">
        <ul>
          <li>Arithmetic: `+`, `-`, `*`, `/`, `%`</li>
          <li>Relational: `==`, `!=`, `<`, `>`, `<=`, `>=`</li>
          <li>Logical: `&&`, `||`, `!`</li>
          <li>Bitwise operators for integer manipulation</li>
          <li>Short-circuit evaluation in boolean expressions</li>
        </ul>
      </div>
    </div>

    <div data-tags="methods recursion" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 4: Control Flow</div>
      <div class="notecard-body">
        <ul>
          <li>Understanding conditional statements: `if`, `else`, `else if`</li>
          <li>Switch-case statements for multi-branch logic</li>
          <li>Common mistakes: nested conditionals and redundant checks</li>
          <li>Use of the ternary operator for concise conditional checks</li>
        </ul>
      </div>
    </div>

    <div data-tags="arrays" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 5: Arrays</div>
      <div class="notecard-body">
        <ul>
          <li>Declaring and initializing arrays</li>
          <li>Zero-based indexing and traversing arrays with loops</li>
          <li>Multidimensional arrays: 2D and 3D arrays</li>
          <li>Searching, sorting, and manipulating arrays</li>
        </ul>
      </div>
    </div>

    <div data-tags="methods" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 6: Methods</div>
      <div class="notecard-body">
        <ul>
          <li>Method declaration and return types</li>
          <li>Passing parameters: By value vs. By reference</li>
          <li>Overloading methods with different signatures</li>
          <li>Common method-related errors: stack overflow, recursion depth</li>
        </ul>
      </div>
    </div>

    <div data-tags="classes" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 7: Classes and Objects</div>
      <div class="notecard-body">
        <ul>
          <li>Defining classes and creating objects</li>
          <li>Constructors and instance variables</li>
          <li>Methods in classes: instance and static methods</li>
          <li>Using `this` to refer to current object</li>
        </ul>
      </div>
    </div>

    <div data-tags="classes" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 8: Inheritance</div>
      <div class="notecard-body">
        <ul>
          <li>Understanding parent-child class relationships</li>
          <li>Overriding and extending methods</li>
          <li>Polymorphism and dynamic method invocation</li>
          <li>Super keyword and accessing parent class methods</li>
        </ul>
      </div>
    </div>

    <div data-tags="recursion" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 9: Recursion</div>
      <div class="notecard-body">
        <ul>
          <li>Base case and recursive case structure</li>
          <li>Common recursion examples: factorial, Fibonacci</li>
          <li>Understanding the stack and recursion depth</li>
        </ul>
      </div>
    </div>

    <div data-tags="loops arrays" class="notecard">
      <div class="notecard-header" onclick="toggleBody(this)">Unit 10: Searching and Sorting Algorithms</div>
      <div class="notecard-body">
        <ul>
          <li>Linear and binary search techniques</li>
          <li>Bubble sort, selection sort, and insertion sort</li>
          <li>Time complexity and big-O notation</li>
        </ul>
      </div>
    </div>

  </div>

  <script>
    function filterTopics() {
      const searchValue = document.getElementById('searchInput').value.toLowerCase();
      document.querySelectorAll('.notecard').forEach(item => {
        const text = item.innerText.toLowerCase();
        item.style.display = text.includes(searchValue) ? '' : 'none';
      });
    }

    function filterByTag(tag) {
      const buttons = document.querySelectorAll('.tag-buttons button');
      buttons.forEach(btn => btn.classList.remove('active'));

      if (tag === 'all') {
        buttons[0].classList.add('active');
        document.querySelectorAll('.notecard').forEach(item => item.style.display = '');
      } else {
        document.querySelector(`button[onclick="filterByTag('${tag}')"]`).classList.add('active');
        document.querySelectorAll('.notecard').forEach(item => {
          const tags = item.getAttribute('data-tags').split(' ');
          item.style.display = tags.includes(tag) ? '' : 'none';
        });
      }
    }

    function toggleBody(headerElement) {
      const body = headerElement.nextElementSibling;
      const isOpen = body.style.display === 'block';
      body.style.display = isOpen ? 'none' : 'block';
    }
  </script>

</body>
