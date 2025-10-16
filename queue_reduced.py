from lst import Lst
from typing import Generic, TypeVar

T = TypeVar('T')

#############################################
# Queue ADT implementation, using Lst class #
#############################################

class Queue(Generic[T]):

  # Type annotations for fields 
  # (-- optional, like all types in Python)
  _data: Lst[T]
  _size: int

  # Constructor
  def __init__(self):
    self._data = Lst()
    self._size = 0
  
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
  def __str__(self) -> str:
    values_string: str = str(self._data)    # E.g  "Lst(1, 2, 3)"
    values_string = values_string.removeprefix("Lst")  # Remove the "Lst" at the start
    return "Queue" + values_string  # ... and put "Queue" in front instead :-)

  def __repr__(self) -> str:
    return str(self) 

