# MiniLang Compiler

This is a small compiler project I built to understand how compilers work internally.
The goal was to go step by step from source code to generated output.

## What this compiler does

The compiler processes MiniLang programs in multiple stages:
Source Code  
→ Lexer  
→ Parser (AST)  
→ Semantic Analysis  
→ Optimizer  
→ Code Generation

## Features

- Custom language with `LET` and `PRINT`
- Lexer and recursive-descent parser
- AST-based expression handling
- Basic semantic checks (undefined variables, redefinition warnings)
- Simple compile-time optimizations (constant folding)
- Generates:
  - Python code
  - Stack-machine instructions

## Example

### Input
```text
LET x = 10 + 5 * 2;
### Output (Python)
```text
x = 20
### Output (Stack)
```text
PUSH 20
STORE x


## How to run

1. Put a MiniLang program inside the `tests/` folder
2. Run:
```bash
python src/main.py


## Notes

This project is intentionally simple.
Some errors are reported as warnings so the compiler can continue and show output.
The focus was on learning compiler stages rather than building a full language.

## Why I built this

I wanted a hands-on way to understand parsing, AST traversal, and code generation
instead of only studying theory.

