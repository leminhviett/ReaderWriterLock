# ReaderWriterLock

This Python package addresses the reader-writer problems. It supports both multithreading and multiprocessing environment in Python.

The package is implemented based on a [RLock](https://docs.python.org/3/library/threading.html#rlock-objects) and 2 [Condition Variables](https://docs.python.org/3/library/threading.html#condition-objects)

Refer to [Wikipedia](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock) for full detail about reader-writer lock.


## Installation
`pip install reader-writer-locks`

## Usage
1. Choose between the following `option`

| Priority Policies | option |
|-------------------|--------|
| Not specified     | 0      |
| Reader priority   | 1      |
| Writer priority   | 2      |

2. Instantiate locks based on the chosen `option`

```
# in case of multithreading usage

from reader_writer_lock import MultithreadingFactory
rw = MultithreadingFactory(option)
r_lock = rw.get_read_lock()
w_lock = rw.get_write_lock()

# in case of multiprocessing usage

from reader_writer_lock import MultiprocessingFactory 
# same as multi threading cases
```

3. Use the generated lock to protect critical sections Pythonic usage

```
with r_lock:
    # Read
with w_lock:
    # Write
```

## Future work

1. To avoid starvation problem. (As the [Condition Object](https://docs.python.org/3/library/threading.html#condition-objects) in Python does not work in FIFO manner)
2. To add blocking & timeout interface, which follows the [RLock](https://docs.python.org/3/library/threading.html#rlock-objects) interface
