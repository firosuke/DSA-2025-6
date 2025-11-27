from __future__ import annotations

from typing import Generic, Optional, TypeVar

K = TypeVar('K')
V = TypeVar('V')

####################################
# Node, to be used in binary trees #
####################################
class BSTNode(Generic[K], Generic[V]):
  # Type annotations
  _key: Optional[K]
  _value: Optional[V]
  _left: Optional[Node[K, V]]
  _right: Optional[Node[K, V]]

  def __init__(self, key: Optional[K]=None, value: Optional[V]=None, left: Optional[Node[K, V]]=None, right: Optional[Node[K, V]]=None):
    self._key = key
    self._value = value
    self._left = left
    self._right = right

  def set_value(self, value: V) -> None:
    self._value = value

  def get_value(self) -> V:
    return self._value
  
  def set_key(self, key: K) -> None:
    self._key = key

  def get_key(self) -> K:
    return self._value

  def set_left(self, left: Node[K, V]) -> None:
    self._left = left

  def get_left(self) -> Optional[Node[K, V]]:
    return self._left

  def set_right(self, right: Node[K, V]) -> None:
    self._right = right

  def get_right(self) -> Optional[Node[K, V]]:
    return self._right
  
  def __str__(self):
    v = self._value
    v = f'"{v}"' if isinstance(v, str) else str(v)
    k = self._key
    if k == None:
      # For backwards compatibility with previous exercises
      return f"Node({v}, {str(self._left)}, {str(self._right)})"
    elif v == None:
      return f"Node({k}, {str(self._left)}, {str(self._right)})"
    else:
      return f"Node({k}, {v}, {str(self._left)}, {str(self._right)})"

  def __repr__(self):
    return str(self)

def show_all_nodes(node: Optional[Node], prefix: str = "", is_left: bool = True, is_first: bool = True) -> None:
    if node is None:
        return
    if node._right:
        new_prefix = prefix + ("    " if is_first else "│   " if is_left else "    ")
        show_all_nodes(node._right, new_prefix, False, False)
    connector = "    " if is_first else "└── " if is_left else "┌── "
    if node._key == None:
      kv_part = str(node._value)
    elif node._value == None:
      kv_part = str(node._key)
    else:
      kv_part = str(node._key) + ":" + str(node._value)
    print(prefix + connector + kv_part)
    if node._left:
        new_prefix = prefix + ("    " if is_left else "│   ")
        show_all_nodes(node._left, new_prefix, True, False)
