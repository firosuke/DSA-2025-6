# FREEZE CODE BEGIN
from __future__ import annotations

from typing import TypeVar, Generic, List
from random import random, randint

T = TypeVar('T')

##############################################
# Wrapping the built-in list class in an ADT #
##############################################

# This is not an "implementation" of lists, but simply packaging ("wrapping") 
# a built-in Python list (self._data) in a simpler interface (the ADT for lists, called Lst).

# A true implementation would use either an arraylist (see week 1 "Implementing lists") or a linked list.
# I will provide an arraylist implementation when time permits.
# By contrast, linked lists are easier to implement, but less efficient. We may see this in week 3.

class Lst(Generic[T]):

  # Type annotations
  _data: List[T] # A built-in Python list
  _size: int # Keep track of the size here

  # Constructor
  def __init__(self, *args: T) -> None:
    self._data: List[T] = list(args)
    self._size = len(self._data)

  # Public methods
  def size(self) -> int:
    return self._size

  def append(self, v: T) -> None:
    self._data.append(v)
    self._size += 1

  def insert(self, i: int, v: T) -> None:
    if i >= self._size:
      raise IndexError(f"Cannot insert at index {i}")
    else:
      self._data.insert(i, v)
      self._size += 1

  def remove(self, i: int) -> None:
    if 0 <= i < self._size:
      v: T = self._data[i]
      del self._data[i]      # (Can combine both steps using built-in 'pop' method on lists.)
      self._size -= 1
    else:
      raise IndexError(f"Cannot remove from item {i}")

  def read(self, i: int) -> T:
    if 0 <= i < self._size:
      v: T = self._data[i]
      return v
    else:
      raise IndexError(f"Cannot read from index {i}")

  def get(self, i: int) -> T: # synonym
    return self.read(i)
  
  def write(self, i: int, v: T) -> None:
    if 0 <= i < self._size:
      self._data[i] = v
    else:
      raise IndexError(f"Cannot write to index {i}")

  def set(self, i: int, v: T) -> None: # synonym
    return self.write(i, v)
  
  # Display methods
  def __str__(self) -> str:
    return "Lst(" + ", ".join((f"\"{str(v)}\"" if isinstance(v, str) else str(v)) for v in self._data) + ")"

  def __repr__(self) -> str:
    return str(self)

  def __eq__(self, other) -> bool:
    if not isinstance(other, Lst):
      return False
    if self._size != other._size:
      return False
    return self._data == other._data

  # Generate method for testing (ints only)
  def generate(S: type, **params) -> Lst:  # Class method
    data: Lst[S] = Lst()
    if S == int:
      p = ("positive_only" in params and params["positive_only"])
      data.append(randint(3 if p else -9, 9))
      for i in range(randint(3, 10)):
        if random() < 0.3:
          data.append(int(data.read(data.size() - 1)))
        else:
          x = int(data.read(data.size() - 1) * (0.6 + 0.4 * random()) + randint(-5, 5))
          data.append(abs(x) if p else x)
    else:
      for _ in range(randint(0, 10)):
        data.append(S.generate(), **params)
    return data

# FREEZE CODE END
