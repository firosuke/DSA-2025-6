from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar('T')

####################################
# Node, to be used in binary trees #
####################################
class Node(Generic[T]):
  # Type annotations
  _value: Optional[T]
  _left: Optional[Link[T]]
  _right: Optional[Link[T]]

  def __init__(self, value: Optional[T]=None, left: Optional[Node[T]]=None, right: Optional[Node[T]]=None):
    self._value = value
    self._left = left
    self._right = right

  def set_value(self, value: T) -> None:
    self._value = value

  def get_value(self) -> T:
    return self._value

  def set_left(self, left: Node[T]) -> None:
    self._left = left

  def get_left(self) -> Optional[Node[T]]:
    return self._left

  def set_right(self, right: Node[T]) -> None:
    self._right = right

  def get_right(self) -> Optional[Node[T]]:
    return self._right
  
  def __str__(self):
    v = self._value
    v = f'"{v}"' if isinstance(v, str) else str(v)
    return f"Node({v}, {str(self._left)}, {str(self._right)})"

  def __repr__(self):
    return str(self)

def show_all_nodes(node: Optional[Node], prefix: str = "", is_left: bool = True) -> None:
    if node is None:
        return
    if node._right:
        new_prefix = prefix + ("│   " if is_left else "    ")
        show_all_nodes(node._right, new_prefix, False)
    connector = "└── " if is_left else "┌── "
    print(prefix + connector + str(node._value))
    if node._left:
        new_prefix = prefix + ("    " if is_left else "│   ")
        show_all_nodes(node._left, new_prefix, True)
