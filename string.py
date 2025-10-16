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
    return self._s.find(c)
  def __str__(self) -> str: # The irony of this method
    return f"String({self._s})"
  def __repr__(self) -> str:
    return str(self)
  def __eq__(self, other) -> bool:
    if not isinstance(other, String):
      return False
    return other._s == this._s

  # Generate method for testing
  def generate(matched=None) -> String:  # Class method
    # matched=None: don't care about bracketing.
    # matched=True/False: result must (not) be matched.
    o = "({[<"
    c = ")}]>"
    s = []
    # Crude approach: keep generating until we get something
    # that is/is not matched appropriately.
    while True:
      this_one_matched = True
      for _ in range(randint(0, 8)):
        i = randint(0, len(s))
        r = random() 
        if r > 0.6:
          # Insert matched bracket pair
          b = randint(0, len(o) - 1) 
          s.insert(i, c[b])
          s.insert(i, o[b])
        elif r > 0.08:
          # Insert random letter
          s.insert(i, sample("abcdefgh", 1)[0])
        else:
          # Insert unmatched bracket
          this_one_matched = False
          b = randint(0, len(o) - 1)
          s.insert(i, c[b] if random() > 0.5 else o[b])
      if matched==None or this_one_matched == matched:
        break
    return String("".join(s))

# FREEZE CODE END
