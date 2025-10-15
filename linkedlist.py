from typing import Generic, Optional, TypeVar
from link import Link

T = TypeVar('T')

#############################################
# Lst ADT implementation, using linked list #
#############################################

class LLst(Generic[T]):
  # Type annotations
  _sentinel: Link[Optional[T]] # A link to the start of the list
  # There is always an initial link containing no data -- whether or not the list has any data.
  # This is called a "sentinel" link.
  # It makes inserting and removing (at the front) easier to implement.
  # If there is any data in the list, it comes *after* the sentinel link.
  _size: int
  _end: Link[Optional[T]] # A reference to the last link,
  # just to make appending quicker.

  # Constructor
  def __init__(self, *args):
    self._sentinel = Link(None, None)
    if args:
      current = self._sentinel
      # for each value provided (in the arguments), add a further link
      # This loop may be hard to understand without a diagram
      for i in full_range(0, len(args) - 1):
        next = Link(args[i], None) # make a new link
        current._next = next # connect the last link to the new one
        current = next # now move on to the new link
    else:
      self._head = None
    # "current" is now the end link
    self._end = current
    self._size = len(args)

  # Public methods
  def size(self) -> int:
    return self._size

  def append(self, v: T) -> None:
    # These steps are a bit hard to understand without a diagram
    # Create a new link, connect the current end to the new one,
    # and update "end" to refer to the new link (instead of the old end)
    new = Link(v, None)
    self._end._next = new
    self._end = new
    self._size += 1

  def remove(self, remove_i: int) -> None:
    current = self._sentinel
    # Follow remove_i links, taking us to the link before the one to be removed 
    for i in full_range(1, remove_i):
      if current == None:
        raise IndexError(f"Reached end of list before reaching index {remove_i}")
      current = current._next
    # Check if we are trying to "remove" beyond the end
    if current == None or current._next == None:
      raise IndexError(f"Reached end of list before reaching index {remove_i}")
    # Now remove the link after the current link
    # These steps may be hard to understand without a diagram
    # Connect the link before the removal point to the link after the removal point
    # And if we happen to be removing the end, update "end" to refer to the link before the end
    # (otherwise the "end" reference does not need to change -- as the same link is still at the end)
    if current._next == self._end:
      self._end = current
    current._next = current._next._next
    self._size -= 1

  def insert(self, insert_i: int, v: T) -> None:
    current = self._sentinel
    # Follow insert_i links, taking us to the link before where we should insert
    for i in full_range(1, insert_i):
      if current == None:
        raise IndexError(f"Reached end of list before reaching index {insert_i}")
      current = current._next
    # Check if we are trying to "insert" beyond the end
    if current == None:
      raise IndexError(f"Reached end of list before reaching index {insert_i}")
    # Now insert the value after current link
    # These steps may be hard to understand without a diagram
    # Create a new link, connect it to the link at the insertion point,
    # and connect the current link to the new one      
    new = Link(v, None)
    new._next = current._next
    current._next = new
    # And if we are inserting a new end, then update "end" to refer to it
    if current == self._end:
      self._end = current._next
    self._size += 1

  def read(self, i: int) -> T:
    current = self._sentinel
    # Follow (i + 1) links, taking us to the link containing the value to be read
    for _ in full_range(1, i + 1):
      if current == None:
        raise IndexError(f"Reached end of list before reaching index {i}")
      current = current._next
    # Check if we are trying to read beyond the end
    if current == None:
      raise IndexError(f"Reached end of list before reaching index {i}")
    return current._value

  def write(self, i: int, v: T) -> None:
    current = self._sentinel
    # Follow (i + 1) links, taking us to the link containing the value to be replaced 
    for _ in full_range(1, i + 1):
      if current == None:
        raise IndexError(f"Reached end of list before reaching index {i}")
      current = current._next
    # Check if we are trying to write beyond the end
    if current == None:
      raise IndexError(f"Reached end of list before reaching index {i}")
    current._value = v

  # Display methods
  def __str__(self) -> str:
    value_strings = []
    current = self._sentinel._next
    while current != None:
      value_strings.append(f"{current._value}")
      current = current._next

    values_string = ", ".join(value_strings)
    return f"LLst({values_string})"

  def __repr__(self) -> str:
    return str(self)

  def debug(self):
    self._sentinel.show_all_links()
    print("_size:", self._size, "(not including sentinel)")
    print("_end._value:", self._end._value)
