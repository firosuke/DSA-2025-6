from typing import Optional, Generic, TypeVar
from lst import Lst

T = TypeVar('T')

#################################################
# Queue ADT implementation, using circular list #
#################################################

class QueueC(Generic[T]):

  # Type annotations

  # Whenever changing the data, each of these may have to be updated:
  _data: Lst[Optional[T]] # 1. A list containing the values, and maybe None
  _n: int        # 2. number of elements, equal to end - start + 1
  _start: int    # 3. index of first item
  _end: int      # 4. index of last item (circular list: end can be before start!)
  _capacity: int # 5. size of data list

  # Constructor
  def __init__(self, *vals: T):

    self._data = Lst(*vals)  # 1
    for _ in range(4):
      self._data.append(None)

    self._n = len(vals) # 2
    self._start = 0     # 3
    self._end = self._n - 1   # 4
    self._capacity = self._n + 4    # 5


  # Private methods
  def resize_capacity(self, new_capacity: int) -> None:
    new_data = Lst()

    # Append the existing data into the new list
    for i in full_range(0, self._n - 1):
      v = self._data.read((self._start + i) % self._capacity)
      new_data.append(v)
    # Add extra "empty" slots into the new list if needed
    for _ in full_range(self._n, new_capacity - 1):
      new_data.append(None)
    
    self._data = new_data    # 1
    # No change to self._n   # 2
    self._start = 0          # 3
    self._end = self._n - 1  # 4
    self._capacity = new_capacity # 5


  # Public methods
  def enqueue(self, value: T) -> None:
    if self._n == self._capacity:
      self.resize_capacity(self._capacity * 2)
    
    self._end = (self._end + 1) % self._capacity

    self._data.write(self._end, value)   # 1
    self._n += 1             # 2
    # self._start no change  # 3
    # self._end already changed   # 4
    # self._capacity changed if needed   # 5

  def front(self) -> T:
    return self._data.read(self._start)

  def dequeue(self) -> T:
    front = self.front()

    self._data.write(self._start, None)   # 1
    self._n -= 1        # 2
    self._start = (self._start + 1) % self._capacity   # 3
    # No change to self._end    # 4
    
    # If data list is more than 75% unoccupied, then reduce its size
    if self._n < self._capacity * 0.25:
      self._resize_capacity(self._n + 4)     # 5
    return front

  def size(self) -> int:
    return self._n
  
  # Display methods
  def __str__(self):
    value_strings = []
    for i in full_range(0, self._n - 1):
      value = self._data.read((i + self._start) % self._capacity)
      value_strings.append(str(value))

    values_string = ", ".join(value_strings)
    return f"Queue({values_string})" 
    
  def __repr__(self):
    return str(self)  

  def debug(self):
    print(f"_data: {self._data}")
    print(f"_n: {self._n}")
    print(f"_start: {self._start}")
    print(f"_end: {self._end}")
    print(f"_capacity: {self._capacity}")
