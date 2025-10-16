# FREEZE CODE BEGIN

from queue import Queue
from random import random, randint

##############################################################################
# Task class and related functions used in week 3 exercise on task scheduler #
##############################################################################

class Task:
  # Type annotations
  _name: str
  _is_high_priority: bool
  _remaining_time: int
  # The task is considered "completed" if the remaining time is zero

  # Constructor
  def __init__(self, name, is_high_priority, duration):
    self._name = name
    self.is_high_priority = is_high_priority
    self._remaining_time = duration

  # Public methods
  def run(self, period: int) -> None:
    run_duration = min(period, self._remaining_time)
    print("Running task", self.name, "for", run_duration, "clock cycles")
    self._remaining_time = max(0, self._remaining_time - period)
    if self._remaining_time == 0:
      print("Task", self.name, "completed")

  def is_complete(self) -> bool:
    return self._remaining_time == 0  

  # Display methods
  def __str__(self) -> str:
    return f"Task({self.name}, {self.is_high_priority}, {self._remaining_time})"

  def __repr__(self) -> str:
    return str(self)


# Other functions for generating random (queues) of tasks

def generate(can_be_completed=False) -> Task:
  name = chr(ord("A") + i)
  is_high_priority = True if random() > 0.6 else False    
  remaining_time = 0 if (can_be_completed and random() > 0.6) else randint(50, 400)
  return Task(name, is_high_priority, remaining_time)

# FREEZE CODE END
