---
layout: post
title: CSA Review
comments: true
---

<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }

  .navbar {
    background-color: #f8f9fa;
    padding: 10px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #ddd;
  }

  .navbar-left {
    font-size: 1.2em;
    font-weight: bold;
    color: #333;
  }

  .navbar-center,
  .navbar-right {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .dropdown {
    position: relative;
  }

  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #fff;
    min-width: 160px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    z-index: 1;
    margin-top: 5px;
  }

  .dropdown-content a {
    display: block;
    padding: 8px 12px;
    text-decoration: none;
    color: #333;
    background-color: #f9f9f9;
  }

  .dropdown-content a:hover {
    background-color: #007bff;
    color: white;
  }

  .dropdown:hover .dropdown-content {
    display: block;
  }

  h1 {
    margin: 20px 30px;
  }

  input[type="text"] {
    display: block;
    width: calc(100% - 60px);
    margin: 10px 30px 20px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 6px;
  }

  .notecard {
    background-color: #f9f9f9;
    padding: 15px;
    margin: 15px 30px;
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

  .see-more-button {
    margin-top: 10px;
    display: inline-block;
    background-color: #007bff;
    color: white;
    padding: 6px 12px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.9em;
  }

  .see-more-button:hover {
    background-color: #0056b3;
  }

  @media (max-width: 768px) {
    .navbar {
      flex-direction: column;
      align-items: flex-start;
    }

    .navbar-center,
    .navbar-right {
      margin-top: 10px;
    }

    input[type="text"] {
      width: calc(100% - 40px);
      margin: 10px 20px 20px;
    }

    .notecard {
      margin: 15px 20px;
    }
  }

  /* 🔹 Navbar buttons updated with minimalistic style */
  .navbar a,
  .dropdown > a,
  .dropdown > span {
    padding: 8px 14px;
    background-color: transparent;
    color: #007bff;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 500;
    transition: background-color 0.3s, box-shadow 0.3s, color 0.3s;
    border: 1px solid transparent;
  }

  .navbar a:hover,
  .dropdown > a:hover,
  .dropdown > span:hover {
    background-color: #e9ecef;
    color: #0056b3;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  }

  .dropdown > span {
    cursor: pointer;
    display: inline-block;
  }
</style>

<body>
  <div class="navbar">
    <div class="navbar-left">Code Code Code!</div>

  <div class="navbar-center">
      <div class="dropdown">
        <a>Units</a>
        <div class="dropdown-content">
          <a href="unit-1.html">Unit 1</a>
          <a href="unit-2.html">Unit 2</a>
          <a href="unit-3.html">Unit 3</a>
          <a href="unit-4.html">Unit 4</a>
          <a href="unit-5.html">Unit 5</a>
          <a href="unit-6.html">Unit 6</a>
          <a href="unit-7.html">Unit 7</a>
          <a href="unit-8.html">Unit 8</a>
          <a href="unit-9.html">Unit 9</a>
          <a href="unit-10.html">Unit 10</a>
        </div>
      </div>
  </div>

  <div class="navbar-right">
      <a href="frq-overview.html">FRQ Overview</a>
      <a href="FRQPractice_IPYNB_2_.html">FRQ Practice</a>
      <a href="EnactmentHomework_IPYNB_2_.html">Enactments Homework</a>
    </div>
  </div>

  <input type="text" id="searchInput" placeholder="Search topics..." onkeyup="filterTopics()" />

<div id="checklist">
  <div class="notecard" data-tags="variables expressions primitives">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 1: Primitive Types</div>
    <div class="notecard-body">
      <ul>
        <li>Primitive types: <code>int</code>, <code>double</code>, <code>boolean</code>, <code>char</code></li>
        <li>Integer division truncates: <code>7 / 2</code> → <code>3</code></li>
        <li>Type casting: <code>(int) 5.7</code> → <code>5</code></li>
        <li><code>final</code> = constant: <code>final int MAX = 100;</code></li>
        <li>Use <code>Math</code> class: <code>Math.pow()</code>, <code>Math.abs()</code></li>
        <li>Operator order: <code>*</code>, <code>/</code> before <code>+</code>, <code>-</code></li>
        <li><code>String</code> is not primitive but commonly used</li>
      </ul>
      <a class="see-more-button" href="unit-1.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="methods objects strings math">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 2: Using Objects</div>
    <div class="notecard-body">
      <ul>
        <li>Create objects with <code>new</code>: <code>Scanner sc = new Scanner(System.in);</code></li>
        <li>String methods: <code>.length()</code>, <code>.substring()</code>, <code>.equals()</code></li>
        <li>Use <code>.equals()</code> for string comparison, not <code>==</code></li>
        <li>Autoboxing = convert primitive ↔ wrapper</li>
        <li>Object references can alias</li>
        <li>Common wrappers: <code>Integer</code>, <code>Double</code>, <code>Boolean</code></li>
        <li>Know how to read Java API docs</li>
      </ul>
      <a class="see-more-button" href="unit-2.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="boolean logic conditionals">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 3: Boolean Expressions and If Statements</div>
    <div class="notecard-body">
      <ul>
        <li>Relational ops: <code>==</code>, <code>!=</code>, <code>></code>, <code><</code>, <code>>=</code>, <code><=</code></li>
        <li>Logical ops: <code>&&</code>, <code>||</code>, <code>!</code></li>
        <li>Use parentheses to group logic clearly</li>
        <li><code>if</code>, <code>if-else</code>, <code>else if</code> blocks for control flow</li>
        <li>Order matters in chained <code>if-else</code> blocks</li>
        <li>Use truth tables to break down expressions</li>
        <li>Short-circuit: <code>&&</code> stops if false, <code>||</code> stops if true</li>
      </ul>
      <a class="see-more-button" href="unit-3.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="loops iteration">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 4: Iteration</div>
    <div class="notecard-body">
      <ul>
        <li><code>while</code>, <code>for</code>, <code>do-while</code> loops</li>
        <li>Use loops for repetition with counters or conditions</li>
        <li><code>for (int i = 0; i < n; i++)</code> is standard</li>
        <li>Off-by-one errors are common!</li>
        <li><code>break</code> exits loop, <code>continue</code> skips to next iteration</li>
        <li>Loop tracing is common on AP MCQs</li>
        <li>Nested loops increase time complexity</li>
      </ul>
      <a class="see-more-button" href="unit-4.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="classes objects constructors">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 5: Writing Classes</div>
    <div class="notecard-body">
      <ul>
        <li>Use <code>class ClassName {}</code> structure</li>
        <li>Define fields (variables), constructors, and methods</li>
        <li><code>private</code> = encapsulation; use getters/setters</li>
        <li>Constructor name = class name</li>
        <li><code>this</code> keyword refers to current object</li>
        <li>Good practice: initialize fields in constructor</li>
        <li>Use comments and clarity for method behavior</li>
      </ul>
      <a class="see-more-button" href="unit-5.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="arrays algorithms loops">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 6: Arrays</div>
    <div class="notecard-body">
      <ul>
        <li>Fixed-size, same-type container: <code>int[] arr = new int[5];</code></li>
        <li>Indexing starts at 0</li>
        <li>Use <code>.length</code> (no parentheses) for array length</li>
        <li>Traverse with loops: <code>for</code> or <code>for-each</code></li>
        <li>Watch for <code>IndexOutOfBoundsException</code></li>
        <li>Arrays of objects store references</li>
        <li>Default values: <code>0</code>, <code>false</code>, <code>null</code></li>
      </ul>
      <a class="see-more-button" href="unit-6.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="arrays arraylists loops">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 7: ArrayList</div>
    <div class="notecard-body">
      <ul>
        <li>Resizable version of arrays</li>
        <li>Import with <code>import java.util.ArrayList;</code></li>
        <li>Use methods: <code>.add()</code>, <code>.get()</code>, <code>.set()</code>, <code>.remove()</code></li>
        <li>Use <code>.size()</code> instead of <code>.length</code></li>
        <li>Can only store objects (e.g., <code>Integer</code>, not <code>int</code>)</li>
        <li>Modify while iterating carefully to avoid skips</li>
        <li>ArrayList is generic: <code>ArrayList&lt;Type&gt;</code></li>
      </ul>
      <a class="see-more-button" href="unit-7.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="arrays 2darrays loops">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 8: 2D Arrays</div>
    <div class="notecard-body">
      <ul>
        <li>Array of arrays: <code>int[][] grid = new int[3][4];</code></li>
        <li>Use nested loops to traverse: rows then columns</li>
        <li>Length: <code>arr.length</code> for rows, <code>arr[0].length</code> for columns</li>
        <li>Jagged arrays are allowed (<code>arr[i].length</code> varies)</li>
        <li>Typical patterns: sums, counts, searching</li>
        <li>Common pitfalls: wrong loop bounds or reversed indices</li>
        <li>2D arrays often used in FRQs</li>
      </ul>
      <a class="see-more-button" href="unit-8.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="classes inheritance polymorphism">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 9: Inheritance</div>
    <div class="notecard-body">
      <ul>
        <li><code>extends</code> creates a subclass from superclass</li>
        <li>Subclasses inherit methods/fields from super</li>
        <li>Use <code>super()</code> to call parent constructor</li>
        <li>Override methods with <code>@Override</code> annotation</li>
        <li>Polymorphism: superclass ref → subclass object</li>
        <li>Use casting for subclass-specific behavior</li>
        <li>Only methods in superclass are accessible from superclass ref</li>
      </ul>
      <a class="see-more-button" href="unit-9.html">→ See Full Details</a>
    </div>
  </div>

  <div class="notecard" data-tags="recursion loops basecase">
    <div class="notecard-header" onclick="toggleBody(this)">Unit 10: Recursion</div>
    <div class="notecard-body">
      <ul>
        <li>A method that calls itself</li>
        <li>Must have base case to stop</li>
        <li>Recursive case should move toward base</li>
        <li>Common examples: factorial, sum, search</li>
        <li>Stack overflow if no base or too deep</li>
        <li>Use tracing to follow recursive calls</li>
        <li>Sometimes recursion is easier than loops</li>
      </ul>
      <a class="see-more-button" href="unit-10.html">→ See Full Details</a>
    </div>
  </div>
</div>

  <script>
    function toggleBody(headerElement) {
      const body = headerElement.nextElementSibling;
      const allBodies = document.querySelectorAll('.notecard-body');
      allBodies.forEach(b => {
        if (b !== body) b.style.display = 'none';
      });
      body.style.display = body.style.display === 'block' ? 'none' : 'block';
    }

    function filterTopics() {
      const searchValue = document.getElementById('searchInput').value.toLowerCase();
      document.querySelectorAll('.notecard').forEach(item => {
        const text = item.innerText.toLowerCase();
        item.style.display = text.includes(searchValue) ? '' : 'none';
      });
    }
  </script>

</body>
