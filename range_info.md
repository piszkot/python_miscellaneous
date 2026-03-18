# 💡 Range

#### Range is a lazy, immutable sequence of integers defined by a start, stop, and step. Rather than storing each element in memory, it computes values on demand — making it equally lightweight whether it represents 10 or 10 billion numbers.

Every Python object carries a fixed overhead (`ob_refcnt`, `ob_type`), followed by the actual payload. 
For `range`, the payload is exactly 4 integers (`start`, `stop`, `step`, `length`) — hence 6 × 8 = 48 bytes, regardless of how large the range is.

64 bits = 8 bytes — the size of one memory slot on a modern computer. Every pointer and every basic integer in CPython is aligned to this size.

| Field        | Size         | Description                             |
|--------------|--------------|-----------------------------------------|
| `ob_refcnt`  | 8 bytes      | reference counter used by GC            |
| `ob_type`    | 8 bytes      | pointer to the type object (`range`)    |
| `start`      | 8 bytes      | first value of the sequence             |
| `stop`       | 8 bytes      | upper bound (exclusive)                 |
| `step`       | 8 bytes      | increment between each element          |
| `length`     | 8 bytes      | precomputed number of elements          |
| **Total**    | **48 bytes** | always, for any `range` object          |