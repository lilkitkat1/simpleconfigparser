# Simple Config Parser
A very simple config file parser written in Python. It supports strings and integers.

## How to use
1. Add `scp.py` to your project folder, and import it to your Python file.
2. Create a `Parse` object and pass the raw text as an argument. In this example I am using the example file.
```python
with open("example", "r") as f:
    raw = f.read()
config = scp.Parse(raw)
```
3. Call `parse()` to parse the raw text.
```python
config.parse()
```
4. The data is now available in a dict called `variables`. You can now copy the data to Python variables.
```python
ex_string = config.variables["ex_string"]
ex_int = config.variables["ex_int"]
```

## To do
- [ ] Add float support
- [ ] Add boolean support
- [ ] Add lists?