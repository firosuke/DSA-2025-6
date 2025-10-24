from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar('T')

####################################
# Link, to be used in linked lists #
####################################
class Link(Generic[T]):
  # Type annotations
  _value: Optional[T]
  _next: Optional[Link[T]]  

  def __init__(self, value: Optional[T]=None, next: Optional[Link[T]]=None):
    self._value = value
    self._next = next

  def set_value(self, value: T) -> None:
    self._value = value

  def get_value(self) -> T:
    return self._value

  def set_next(self, next: Link[T]) -> None:
    self._next = next

  def get_next(self) -> Optional[Link[T]]:
    return self._next

  def __str__(self):
    v = f'"{self._value}"' if isinstance(self._value, str) else str(self._value)
    return f"Link({v}, {str(self._next)})"   # recursively calling str(self._next)

  def __repr__(self):
    return str(self)  


def show_all_links(self):
    result_strings = []
    current = self
    while current != None:
      v = f'"{current._value}"' if isinstance(current._value, str) else str(current._value)

      result_strings.append(f"Link({v}, {'·-' if current._next else None})")
      if current._next:
        result_strings.append("-> ")
      current = current._next

    result_string = "".join(result_strings)
    print(result_string)
