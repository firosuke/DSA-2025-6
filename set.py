from typing import TypeVar, Generic
from lst import Lst

T = TypeVar('T')

class Set(Generic[T]):
  def __init__(self, *vargs):
    self._data = set(vargs)
  def add(self, v):
    self._data.add(v)
  def contains(self, v):
    return v in self._data
  def remove(self, v):
    self._data.remove(v)
  def size(self):
    return len(self._data)
  def list(self):
    return Lst(*self._data)
  def __str__(self):
    return ("Set(" + str(self._data)[1:-1] + ")") if len(self._data) > 0 else "Set()"
  def __repr__(self):
    return str(self)
