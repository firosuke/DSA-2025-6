from typing import Dict as dict, TypeVar, Generic
from lst import Lst

K = TypeVar('K')
V = TypeVar('V')

class Map(Generic[K, V]):
  _data: dict[K, V]
  def __init__(self, *kvpairs):
    self._data = {}
    if kvpairs:
      this_is_a_key = True
      k = None
      v = None
      for thing in kvpairs:
        if this_is_a_key:
          k = thing
          this_is_a_key = False
        else:
          v = thing
          self._data[k] = v
          this_is_a_key = True
      if this_is_a_key == False:
        print(f"*** Warning: Last key had no matching value: {k}")
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
    return "Map(" + str(list(Lst(k, v) for k, v in self._data.items()))[1:-1] + ")"
  def __repr__(self):
    return str(self)
