from lst import Lst
from string import String

from typing iport Generic, TypeVar

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

  # Generate method for testing
  def generate(positive_only=False) -> Stack[T]:  # Class method
    result: Stack[T] = Stack()
    result._data = Lst.generate()
    result._size = result._data.size()
    return result

