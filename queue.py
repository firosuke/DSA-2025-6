from lst import Lst
from typing iport Generic, TypeVar

T = TypeVar('T')

################################################
# Simple Queue ADT implementation, using Lst   #
################################################

class Queue(Generic[T]):

  # Type annotations
  _data: Lst[T]
  _size: int

  # Constructor
  def __init__(self, *vals: T):
    self._data = Lst(*vals)
    self._size = len(vals)

  # Public methods
  def enqueue(self, value: T) -> None:
    self._data.append(value)
    self._size += 1

  def front(self) -> T:
    return self._data.read(0)

  def dequeue(self) -> T:
    front = self.front()
    self._data.remove(0)
    self._size -= 1
    return front

  def size(self) -> int:
    return self._size
  
  # Display methods
  def __str__(self):
    # Remove the "Lst()" part of the data string
    return f"Queue({str(self._data)[4:-1]})" 
    
  def __repr__(self):
    return str(self) 
