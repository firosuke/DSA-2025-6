###############################################################################################
# String wrapper(!) to prevent you from doing fancy Python stuff that I don't want you to use #
###############################################################################################

def String:
  _s: str
  def __init__(self, s: str):
    self._s = s
  def read(self, i) -> str:
    return self._s[i]
  def size(self) -> int:
    return len(self._s)
  def __str__(self) -> str: # The irony of this method
    return self._s
  def __repr__(self) -> str:
    return str(self)
  def __eq__(self, other) -> bool:
    if not isinstance(other, String):
      return False
    return other._s == this._s
