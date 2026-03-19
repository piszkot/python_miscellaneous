print("\n*** NUMBER FORMATTING ***\n")

print(f"{255:b}")    # → 11111111  (binary)
print(f"{255:o}")    # → 377       (octal)
print(f"{255:x}")    # → ff        (hex lowercase)
print(f"{255:X}")    # → FF        (hex uppercase)
print(f"{255:#x}")   # → 0xff      (hex z prefixem)
print(f"{1234.5:e}")  # → 1.234500e+03  (notacja naukowa)
print(f"{1234.5:E}")  # → 1.234500E+03

print("\n*** SEPARATORS ***\n")

print(f"{1234567:_}")     # → 1_234_567   (underscore zamiast przecinka)
print(f"{1234.56:_.2f}")  # → 1_234.56

print("\n*** STRINGS ***\n")

name = "hello"
print(f"{name:>10}")   # → "     hello"  (right)
print(f"{name:<10}", "John")   # → "hello     John"  (left)
print(f"{name:^10}")   # → "  hello   "  (center)
print(f"{name:*^10}")  # → "**hello***"  (fill character)
print(f"{name:.3}")    # → "hel"          (truncation)

print("\n*** MISC ***\n")

# PERCENTAGES:
print(f"{0.25:%}")      # → 25.000000%   (percentage)
print(f"{0.25:.1%}")    # → 25.0%

# RAW STRINGS:
print(f"{'line1\nline2   '!r}")  # → 'line1\\nline2   ', spaces visible
print(f"{'line1\nline2'!s}")   # → tekst         (str(), default)

# ASCII:
print(f"{'za\u017c\xf3\u0142\u0107'!a}")   # → 'tekst'       (ascii())
print(f"{'za\u017c\xf3\u0142\u0107'}\n")   # → 'tekst'       (ascii())
