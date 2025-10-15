from mat import Mat
from lst import Lst

################################################
# Weighted graph ADT implementation (as above) #
################################################

# As mentioned in week 2 notes, for simplicity we assume all weights are positive integers.
# Internally, in the adjacency matrix, a weight of 0 means "there is no edge here".

# Notice how similar this is to the unweighted version. A lot of code is repeated.
# This suggests it would be good OOP design to have a *superclass* that both
# graph classes can inherit code from. But that is not the topic of this course.
# I may provide code showing this separately.

class WGraph:

  # Type annotations
  V: Lst[str] # Names of vertices
  _adjMat: Mat[int] # Matrix of *edge weights* (not booleans)
  _n: int # Count of vertices

  # Constructor
  def __init__(self, V, *vals):
    self.V = V
    self._n = V.size()
    vals = list(vals)
    if vals:
      self._adjMat = Mat(self._n, self._n, *vals)
    else:
      self._adjMat = Mat(self._n, self._n, 0)


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

  def _set_adj(self, v1: str, v2: str, w: int) -> None:
    indices = self._get_indices(v1, v2)
    i1 = indices.read(0)
    i2 = indices.read(1)
    self._adjMat.write(i1, i2, w)

  def _get_adj(self, v1: str, v2: str) -> int:
    indices = self._get_indices(v1, v2)
    i1 = indices.read(0)
    i2 = indices.read(1)
    return self._adjMat.read(i1, i2)


  # Public methods
  def has_edge(self, v1: str, v2: str) -> bool:
    return self._get_adj(v1, v2) > 0

  def add_edge(self, v1: str, v2: str, w: int) -> None:
    if self.has_edge(v1, v2):
      return ValueError(f"add_edge: There is already an edge from {v1} to {v2}")
    if w < 1:
      return ValueError(f"add_edge: The weight {w} should be a positive integer")
    self._set_adj(v1, v2, w)

  def remove_edge(self, v1: str, v2: str) -> None:
    if not self.has_edge(v1, v2):
      return ValueError(f"remove_edge: There is no edge from {v1} to {v2}")
    self._set_adj(v1, v2, 0)
  
  def get_weight(self, v1: str, v2: str) -> int:
    if not self.has_edge(v1, v2):
      return ValueError(f"get_weight: There is no edge from {v1} to {v2}")
    return self._get_adj(v1, v2)

  def set_weight(self, v1: str, v2: str, w: int) -> None:
    if not self.has_edge(v1, v2):
      return ValueError(f"set_weight: There is no edge from {v1} to {v2}")
    if w < 1:
      return ValueError(f"set_weight: The weight {w} should be a positive integer")
    self._set_adj(v1, v2, w)


  # Display methods
  def __str__(self) -> str:
      return ("WGraph(" + f"{self.V},\n       "
          + (",\n       ".join(
                ", ".join(
                  str(self._adjMat.read(i, j)) for j in full_range(0, self._n - 1)) 
              for i in full_range(0, self._n - 1))) 
          + ")")

  def __repr__(self) -> str:
    return str(self)  
