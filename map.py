from typing import Dict as dict, TypeVar, Generic
from lst import Lst

K = TypeVar('K')
V = TypeVar('V')

class Map(Generic[K, V]):
  _data: dict[K, V]
  def __init__(self, *kvpairs):
    self._data = {}
    if kvpairs:
      for l in kvpairs:
        k, v = l.read(0), l.read(1)
        self._data[k] = v
  def set(self, k, v):
    self._data[k] = v
  def get(self, k):
    return self._data[k] if k in self._data else None
  def remove(self, k):
    if k in self._data:
      del self._data[k]
  def size(self):
    return len(self._data)
  def keys(self):
    return Lst(*list(self._data.keys()))
  def __str__(self):
    return "Map(Lst(" + str(list(Lst(k, v) for k, v in self._data.items()))[1:-1] + "))"
  def __repr__(self):
    return str(self)
