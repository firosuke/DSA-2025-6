from typing import Set as set, TypeVar, generic
from lst import Lst

T = TypeVar('T')

class Set(Generic[T]):
  _data: set[T]
  def __init__(self):
    self._data = set()
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
    return str(self._data).capitalize()
  def __repr__(self):
    return str(self)
