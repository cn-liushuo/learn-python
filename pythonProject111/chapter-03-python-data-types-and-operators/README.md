# Chapter 3: Python Data Types and Operators

**Language / 语言:** English | [中文](./README.zh.md)

Section 01 of this chapter is written. Sections 02–07 are placeholders for now; their practice scripts will sit next to
this file, like Chapter 2.

## 01 Getting to know Python keywords

**Definition and role**  
**What a keyword is**  
A keyword is a word with a fixed meaning in Python: it has a reserved grammatical role and reserved usage context.

**Why keywords matter**  
Keywords are a core part of Python's syntax rules. They implement conditionals, loop control, function definitions,
class declarations, and other core programming logic.

**Usage restriction**  
Never use a keyword as the name of a variable, function, class, module, or other object — that raises a syntax error.

**Keyword categories and list**

| Category | Keywords | Notes |
|----------|----------|-------|
| Logic / boolean | `True`, `False`, `None`, `and`, `or`, `not` | `True`/`False` are booleans, `None` is the null value, `and`/`or`/`not` are logical operators |
| Conditionals | `if`, `elif`, `else` | `else` is also used with loops and exception handling |
| Pattern matching (3.10+) | `match`, `case` | Soft keywords, active only inside `match` statements |
| Loop control | `for`, `while`, `break`, `continue` | `break` exits a loop, `continue` skips an iteration |
| Exception handling | `try`, `except`, `finally`, `raise`, `assert` | `assert` asserts a condition, `raise` throws an exception |
| Functions and classes | `def`, `class`, `lambda`, `return`, `yield` | `yield` is used in generator functions |
| Scope and naming | `global`, `nonlocal`, `del` | `global`/`nonlocal` declare scope, `del` removes a reference |
| Modules and aliases | `import`, `from`, `as` | `as` aliases a module and also appears in `with ... as ...` |
| Context management | `with` | Manages resources (such as files) automatically |
| Async programming (3.5+) | `async`, `await` | `async def` defines a coroutine, `await` waits for it |
| Membership and identity | `in`, `is` | `in` tests membership, `is` tests object identity |
| Placeholder statement | `pass` | An empty statement that fills a syntax slot and does nothing |

**All keywords (35 in total)**  
`False`, `None`, `True`, `and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`,
`else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`,
`pass`, `raise`, `return`, `try`, `while`, `with`, `yield`

**Soft keywords (4 in total)**  
`_`, `case`, `match`, `type`  
Soft keywords only act as keywords in specific syntax, so they can still be used as identifiers such as variable or
function names.

**How to inspect keywords**  
**Using the `keyword` module**  
Python ships a built-in `keyword` module that lists the current version's keywords and related information — a handy
tool for learning and verifying them.

**List the keywords**  
`import keyword; print(keyword.kwlist)` prints every keyword in Python; a Python 3.x version has 35 of them (the exact
count varies slightly by version).

**Count the keywords**  
`print(len(keyword.kwlist))` returns the total number of keywords so you can gauge the size of the keyword system.

**Case sensitivity**  
Keywords are case sensitive: `True` is a keyword while `true` is an ordinary variable name, and `None` is a keyword
while `none` is not.

## 02 Defining and using variables in Python

> To be written.

## 03 Python basic data types

> To be written.

## 04 Converting between data types

> To be written.

## 05 The eval() function

> To be written.

## 06 Python operators

> To be written.

## 07 Operator precedence

> To be written.
