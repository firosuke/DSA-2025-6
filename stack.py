from lst import Lst
from typing iport Generic, TypeVar

T = TypeVar('T')

################################################
# Stack ADT implementation, using Lst class    #
################################################

class Stack(Generic[T]):

  # Type annotations
  _data: Lst[T]
  _size: int

  # Constructor
  def __init__(self, *vals: T):
    self._data = Lst(*vals)
    self._size = len(vals)

  # Public methods
  def push(self, value: T) -> None:
    self._data.append(value)
    self._size += 1

  def top(self) -> T:
    return self._data.read(self._size - 1)

  def pop(self) -> T:
    top = self.top()
    self._data.remove(self._size - 1)
    self._size -= 1
    return top

  def size(self) -> int:
    return self._size
  
  # Display methods
  def __str__(self):
    # Remove the "Lst()" part of the data string
    return f"Stack({str(self._data)[4:-1]})" 
    
  def __repr__(self):
    return str(self)  
