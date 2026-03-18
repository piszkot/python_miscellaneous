# =============================================================================
# Python String Search Methods: find(), rfind(), index()
# All three search for a substring and return its position (index).
# Key difference: find/rfind return -1 on failure, index raises ValueError.
# =============================================================================

text = "the cat sat on the mat"

# --- find() ------------------------------------------------------------------
# Returns the index of the FIRST occurrence, or -1 if not found.

print(text.find("at"))        # → 5  (first "at" in "cat")
print(text.find("xyz"))       # → -1 (not found — no exception)

# Optional start/end arguments narrow the search range.
print(text.find("at", 6))     # → 9  (skips "cat", finds "sat")
print(text.find("at", 6, 10))  # → 9  (found within range 6–9)
print(text.find("at", 6, 9))  # → -1 (end is exclusive, "at" at 9 is outside)

# --- rfind() -----------------------------------------------------------------
# Like find(), but returns the LAST occurrence instead of the first.

print(text.rfind("at"))       # → 20 (last "at" in "mat")
print(text.rfind("xyz"))      # → -1 (not found — no exception)

# Also supports start/end range.
print(text.rfind("at", 0, 15))  # → 9 (last "at" before index 15)

# --- index() -----------------------------------------------------------------
# Identical to find(), but raises ValueError instead of returning -1.
# Use it when the substring MUST be present (fail fast is the right behavior).

print(text.index("cat"))      # → 4
print(text.index("at", 6))    # → 9  (also supports start/end)

# Raises ValueError — always guard with try/except when unsure.
try:
    text.index("xyz")
except ValueError as e:
    print(f"index() raised: {e}")  # → substring not found

# --- Edge cases --------------------------------------------------------------

# Empty string is always "found" at position 0 (or at start of range).
print(text.find(""))          # → 0
print(text.find("", 5))       # → 5
print(text.index(""))         # → 0

# Search is case-sensitive.
print(text.find("Cat"))       # → -1  ("cat" exists but "Cat" does not)

# The substring can be longer than the string — never matches.
print("hi".find("hello"))     # → -1

# --- Silent bug vs fail-fast -------------------------------------------------

line = "helloworld"  # missing ":" — simulates malformed input

# find() — easy to miss the error
pos = line.find(":")          # → -1  (not found)
# same as line[:-1] — silently cuts the last character!
key = line[:pos]
print(key)                    # → "helloworl"  (wrong, but no error raised)

# index() — fails immediately, exactly where the problem is
try:
    pos = line.index(":")     # → raises ValueError right here
    key = line[:pos]          # this line never executes
except ValueError as e:
    print(f"index() raised: {e}")  # → substring not found
