# FREEZE CODE BEGIN

from __future__ import annotations

from lst import Lst
from typing import Generic, TypeVar

T = TypeVar('T')

################################################
# Stack ADT implementation, using Lst class    #
################################################

class Stack(Generic[T]):

  # Type annotations
  _data: Lst[T]
  _size: int
  _show_every_step: bool # For explanations

  # Constructor
  def __init__(self, *vals: T, show_every_step=False):
    self._data = Lst(*vals)
    self._size = len(vals)
    self._show_every_step = show_every_step
    if self._show_every_step and vals:
      print(str(self))


  # Public methods
  def push(self, value: T) -> None:
    self._data.append(value)
    self._size += 1
    if self._show_every_step:
      print(str(self))

  def top(self) -> T:
    return self._data.read(self._size - 1)

  def pop(self) -> T:
    top = self.top()
    self._data.remove(self._size - 1)
    self._size -= 1
    if self._show_every_step:
      print(str(self))
    return top

  def size(self) -> int:
    return self._size
  
  # Display methods
  def __str__(self):
    # Remove the "Lst()" part of the data string
    return f"Stack({str(self._data)[4:-1]})" 
    
  def __repr__(self):
    return str(self) 

  # Generate method for testing (experimental)
  def generate(S: type, **params) -> Stack:  # Class method
    result: Stack[S] = Stack()
    for _ in randint(0, 10):
      result.push(S.generate(**params))
    return result

# FREEZE CODE END
