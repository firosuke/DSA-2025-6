# FREEZE CODE BEGIN

from mat import Mat
from lst import Lst

#################################################
# Graph ADT implementation using adjacency matrix
#################################################

class Graph:

  # Type annotations
  V: Lst[str] # Names of vertices. Shouldn't really be public but... nevermind.
  _adjMat: Mat[bool]
  _n: int # Count of vertices

  # Constructor
  def __init__(self, V, *vals):
    self.V = V
    self._n = V.size()
    vals = list(vals)
    if vals:
      self._adjMat = Mat(self._n, self._n, *vals)
    else:
      self._adjMat = Mat(self._n, self._n, False)

  # "Private" helper methods
  def _get_index(self, v) -> int:
    for i in full_range(0, self._n - 1):
      if self.V.read(i) == v:
        return i
    raise IndexError(f"Could not find vertex: {v}")
    
  def _get_indices(self, v1, v2) -> Lst[int]:
    i1: int = self._get_index(v1)
    i2: int = self._get_index(v2)
    return Lst(i1, i2)

  def _set_edge(self, v1: str, v2: str, b: bool) -> None:
    indices = self._get_indices(v1, v2)
    i1 = indices.read(0)
    i2 = indices.read(1)
    self._adjMat.write(i1, i2, True)

  # Public methods
  def has_edge(self, v1: str, v2: str) -> bool:
    indices = self._get_indices(v1, v2)
    i1 = indices.read(0)
    i2 = indices.read(1)
    return self._adjMat.read(i1, i2)

  def add_edge(self, v1: str, v2: str) -> None:
    if self.has_edge(v1, v2):
      return ValueError(f"add_edge: There is already an edge from {v1} to {v2}")
    self._set_edge(v1, v2, True)

  def remove_edge(self, v1: str, v2: str) -> None:
    if not self.has_edge(v1, v2):
      return ValueError(f"remove_edge: There is no edge from {v1} to {v2}")
    self._set_edge(v1, v2, False)

  # Display methods
  def __str__(self) -> str:
      return ("Graph(" + f"{self.V},\n      "
          + (",\n      ".join(
                ", ".join(
                  str(self._adjMat.read(i, j)) for j in full_range(0, self._n - 1)) 
              for i in full_range(0, self._n - 1))) 
          + ")")

  def __repr__(self) -> str:
    return str(self)  

  # Randomly generate a graph
  def generate() -> Graph:  # Class method
    n = randint(2, 6)
    V = [chr(ord("A") + i) for i in range(n)]
    G = Graph(Lst(*V))
    for i in range(n):
      for j in range(n):
        if i != j and random() > 0.5:
          G.add_edge(V[i], V[j])
    return G
  
# FREEZE CODE END
