from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar('T')

####################################
# Link, to be used in linked lists #
####################################
class Link(Generic[T]):
  # Type annotations
  _value: T
  _next: Optional[Link[T]]  

  def __init__(self, value: T, next: Optional[Link[T]]):
    self._value = value
    self._next = next

  def set_value(selt, value: T) -> None:
    self._value = value

  def get_value(selt) -> T:
    return self._value

  def set_next(selt, next: Link[T]) -> None:
    self._next = next

  def get_next(selt) -> Optional[Link[T]]:
    return self._next

  def __str__(self):
    return f"Link({self._value}, {str(self._next)})"   # recursively calling str(self._next)

  def __repr__(self):
    return str(self)  

  def show_all_links(self):
    result_strings = []
    current = self
    while current != None:
      result_strings.append(f"Link({current._value}, {'·-' if current._next else None})")
      if current._next:
        result_strings.append("-> ")
      current = current._next

    result_string = "".join(result_strings)
    print(result_string)
