# Python Functions Exercises

This folder contains small examples demonstrating how to define and use functions in Python, including positional/keyword arguments, variable-length arguments, and returning multiple values.

## Structure

- `010_Functions/`

  - `func.py` — basic function definitions and calls.

- `011_KeywordArgs/`

  - `keyw.py` — examples using keyword arguments.

- `012_VariableLengthArguments/`

  - `vari.py` — functions accepting a variable number of positional arguments (`*args`).

- `013_VariableLengthKeywordArguments/`

  - `vkwargs.py` — functions accepting a variable number of keyword arguments (`**kwargs`).

- `014_MultipleReturnValue/`
  - `mreturn.py` — functions that return multiple values (tuples) and how to unpack them.

## Quick start (PowerShell)

From this `Functions` directory run any example like this:

```powershell
# From repository root
python .\Functions\010_Functions\func.py

# Or from this folder
python .\010_Functions\func.py
```

## Requirements

- Python 3.8+ (no special external dependencies required).

## Examples overview

- `func.py`: shows how to define functions, call them, and use return values.
- `keyw.py`: demonstrates calling functions with keyword arguments and default values.
- `vari.py`: demonstrates `*args` for variable positional arguments.
- `vkwargs.py`: demonstrates `**kwargs` for variable keyword arguments.
- `mreturn.py`: shows returning multiple values (tuple) and unpacking them into variables.
