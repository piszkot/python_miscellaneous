import sys

# range() is a lazy sequence - it stores only start, stop and step, regardless of how many numbers it represents.
# list() materializes every element in memory at once.
r = range(1_000_000)
l = list(range(1_000_000))

print("--- range vs list: ---")
print("range(1_000_000):", sys.getsizeof(r), "bytes")
# ~48 bytes
print("list(range(1_000_000):",  sys.getsizeof(l), "bytes")
# ~8 000 056 bytes (8 MB)

print("--- other examples: ---")
print("sys.getsizeof([]) - empty list:", sys.getsizeof([]), "bytes")
# 56 bytes — empty list
print("sys.getsizeof([1, 2, 3]) - 3 elements:",
      sys.getsizeof([1, 2, 3]), "bytes")
# 88 bytes — 3 elements
print("sys.getsizeof(list(range(1_000_000))):",
      sys.getsizeof(list(range(1_000_000))), "bytes")
# ~8 000 056 bytes
