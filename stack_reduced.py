# FREEZE CODE BEGIN

from lst import Lst
from typing import Generic, TypeVar

T = TypeVar('T')

################################################
# Stack ADT implementation, using Lst class    #
################################################

class Stack(Generic[T]):

  # Type annotations for fields 
  # (-- optional, like all types in Python)
  _data: Lst[T]
  _size: int

  # Constructor
  def __init__(self):
    self._data = Lst()
    self._size = 0

  # Public methods
  def push(self, value: T) -> None:
    self._data.append(value)
    self._size += 1

  def top(self) -> T:
    return self._data.read(self._size - 1)

  def pop(self) -> T:
    top: T = self.top()
    self._data.remove(self._size - 1)
    self._size -= 1
    return top

  def size(self) -> int:
    return self._size
  
  # Display methods
  def __str__(self) -> str:
    values_string: str = str(self._data)    # E.g  "Lst(1, 2, 3)"
    values_string = values_string.removeprefix("Lst")  # Remove the "Lst" at the start
    return "Stack" + values_string  # ... and put "Stack" in front instead :-)

  def __repr__(self) -> str:
    return str(self) 

# FREEZE CODE END

