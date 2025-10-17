# FREEZE CODE BEGIN

from __future__ import annotations

from random import randint, random, sample

###############################################################################################
# String wrapper(!) to prevent you from doing fancy Python stuff that I don't want you to use #
###############################################################################################

class String:
  _s: str
  def __init__(self, s: str):
    self._s = s
  def read(self, i) -> str:
    return String(self._s[i])
  def size(self) -> int:
    return len(self._s)
  def find(self, c) -> int:
    return self._s.find(c._s)
  def __str__(self) -> str: # The irony of this method
    return f"String(\"{self._s}\")"
  def __repr__(self) -> str:
    return str(self)
  def __eq__(self, other) -> bool:
    if not isinstance(other, String):
      return False
    return other._s == self._s

  # Generate method for testing
  def generate() -> String:  # Class method
    o = "({[<"
    c = ")}]>"
    s = []
    # Basically a context-free grammar of insertions:
    for _ in range(randint(0, 12)):
      i = randint(0, len(s))
      r = random() 
      if r > 0.6:
        # Insert matched bracket pair
        b = randint(0, len(o) - 1) 
        s.insert(i, c[b])
        s.insert(i, o[b])
      elif r > 0.09:
        # Insert random letter
        s.insert(i, sample("abcdefgh", 1)[0])
      else:
        # Insert unmatched bracket
        b = randint(0, len(o) - 1)
        s.insert(i, c[b] if random() > 0.5 else o[b])
    return String(f"\"{''.join(s)}\"")

# FREEZE CODE END
