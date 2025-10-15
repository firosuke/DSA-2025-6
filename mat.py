from lst import Lst

from typing import TypeVar, Generic

T = TypeVar('T')

###############################################
# Matrix implementation using a list of lists #
###############################################

class Mat(Generic[T]):

  # Type annotations
  height: int
  width: int
  _lofl: Lst[Lst[T]]  # List of lists of "T"s

  # Constructor
  def __init__(self, h: int, w: int, *vs: T):
    self.height = h
    self.width = w
    self._lofl = Lst()
    vs = list(vs)
    for i in range(h):
      new_row = Lst()
      for j in range(w):
        if len(vs) == 1:
          new_row.append(vs[0])
        else:
          new_row.append(vs[i * w + j])
      self._lofl.append(new_row)
  
  # Public methods
  def read(self, i: int, j: int) -> T:
    return self._lofl.read(i).read(j)
  
  def write(self, i: int, j: int, v: T) -> None:
    self._lofl.read(i).write(j, v)

  # Display methods
  def __str__(self) -> str:
      return ("Mat(" + f"{self.height}, {self.width},\n    "
          + (",\n    ".join(
                ", ".join(
                  str(self._lofl.read(i).read(j)) for j in range(self.width)) 
              for i in range(self.height))) 
          + ")")

  def __repr__(self) -> str:
    return str(self)

  # TODO: __eq__, __hash__ ?
