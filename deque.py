from lst import Lst
from typing import TypeVar, Generic, List

T = TypeVar('T')


################################################
# Simple Deque ADT implementation, using Lst   #
################################################

class Deque(Generic[T]):

  # Type annotations
  _data: Lst[T]
  _n: int

  # Constructor
  def __init__(self, *vals: T):
    self._data = Lst(*vals)
    self._n = len(vals)

  # Public methods
  def enqueue_back(self, value: T) -> None:
    self._data.append(value)

  def enqueue_front(self, value: T) -> None:
    self._data.insert(0, value)

  def front(self) -> T:
    return self._data.read(0)

  def back(self) -> T:
    return self._data.read(self._n - 1)

  def dequeue_front(self) -> T:
    front = self.front()
    self._data.remove(0)
    return front

  def dequeue_back(self) -> T:
    back = self.back()
    self._data.remove(self._n - 1)
    return back

  def size(self) -> int:
    return self._n
  
  # Display methods
  def __str__(self):
    # Remove the "Lst()" part of the data
    return f"Deque({str(self._data)[4:-1]})" 
    
  def __repr__(self):
    return str(self) 
