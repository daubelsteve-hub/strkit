# strkit

A tiny collection of string utility functions.

## Functions

- `reverse_string(s)` — returns the input string reversed.
- `is_palindrome(s)` — returns `True` if the string reads the same forwards and backwards (case-insensitive, ignores spaces).

## Usage

```python
from strkit import reverse_string, is_palindrome

reverse_string("hello")      # "olleh"
is_palindrome("Race car")    # True
```

## Testing

```bash
python -m unittest test_strkit.py
```
