# FREEZE CODE BEGIN

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

def generate(S: type, **params) -> Mat: # Class method
  rows = randint(2, 4)
  cols = randint(2, 4)
  data = []
  if S == int: # Special case: Somewhat-smoothly varying integers
    p = "positive_only" in params and params["positive_only"]
    data.append([randint(3, 9)])
    for _ in range(1, cols):
      v = data[0][-1] + 0 * int(data[0][-1] * (0.6 + 0.4 * random())) + randint(-3, 3)
      v = abs(v) if p else v
      data[0].append(v)
    for _ in range(1, rows):
      v = data[-1][0] + 0 * int(data[-1][0] * (0.6 + 0.4 * random())) + randint(-3, 3)
      v = abs(v) if p else v
      data.append([v])
    for i in range(1, rows):
      for j in range(1, cols):
        v = int((c := random()) * data[i][-1] + (1 - c) * data[i - 1][j]) + randint(-3, 3)
        v = abs(v) if p else v
        data[i].append(v)
  else:
    data = []
    for _ in range(rows):
      row = []
      for _ in range(cols):
        row.append(S.generate(**params))
      data.append(row)
  M = Mat(rows, cols, 0)
  for i in range(rows):
    for j in range(cols):
      M._lofl.read(i).write(j, data[i][j])
  return M

  # TODO: __eq__, __hash__ ?

# FREEZE CODE END
