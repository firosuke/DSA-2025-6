from typing import Dict as dict, TypeVar, generic
from lst import Lst

K = TypeVar('K')
V = TypeVar('V')

class Map(Generic[K, V]):
  _data: dict[T]
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
      self._data.remove(k)
  def size(self):
    return len(self._data)
  def keys(self):
    return Lst(*list(self._data.keys()))
  def __str__(self):
    return "Map(" + str(list(Lst(k, (f'"{v}"' if isinstance(v, str) else str(v))) for k, v in self._data.items())) + ")"
  def __repr__(self):
    return str(self)
