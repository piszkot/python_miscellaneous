# Python Implementations Comparison

| Implementation | Based on | Speed | Main Use Case |
|----------------|----------|-------|---------------|
| **CPython** | C | baseline | Default, general purpose |
| **PyPy** | RPython | faster (JIT) | Long-running programs, loops |
| **Cython** | C/C++ | very fast | Performance-critical extensions |
| **Jython** | Java | slower | Java integration |
| **IronPython** | .NET/C# | moderate | .NET/C# integration |
| **MicroPython** | C | limited | Microcontrollers, IoT |
| **Stackless Python** | CPython | similar | Concurrency, many threads |
| **GraalPy** | GraalVM | varies | Polyglot (Python + JS + Ruby...) |

## Short descriptions

- **CPython** – the standard and most widely used implementation, written in C. All others are measured against it.
- **PyPy** – uses Just-In-Time (JIT) compilation, which makes loops and long-running code significantly faster. Not always a drop-in replacement.
- **Cython** – lets you write Python-like code that compiles to C. Used to build fast extensions or speed up bottlenecks.
- **Jython** – runs Python on the JVM. Gives access to Java libraries, but lags behind in Python version support.
- **IronPython** – Python on the .NET runtime. Useful for scripting inside .NET applications.
- **MicroPython** – a lean implementation designed for microcontrollers (e.g. Raspberry Pi Pico, ESP32).
- **Stackless Python** – a fork of CPython that removes the call stack limit and supports microthreads (tasklets).
- **GraalPy** – runs Python on GraalVM, enabling interoperability with JavaScript, Ruby, and other languages on the same runtime.
