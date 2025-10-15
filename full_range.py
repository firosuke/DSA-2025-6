from typing import Iterable

def full_range(start: int, end: int, step: int=1) -> Iterable[int]:
  return range(start, end + step, step)
