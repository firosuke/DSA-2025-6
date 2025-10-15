from random import random, randint

##############################################################################
# Task class and related functions used in week 3 exercise on task scheduler #
##############################################################################

class Task:
  def __init__(self, name, is_high_priority, duration):
    self.name = name
    self.is_high_priority = is_high_priority
    self._remaining_time = duration

  def run(self, period: int) -> None:
    run_duration = min(period, self._remaining_time)
    print("Running task", self.name, "for", run_duration, "clock cycles")
    self._remaining_time = max(0, self._remaining_time - period)
    if self._remaining_time == 0:
      print("Task", self.name, "completed")

  def is_complete(self) -> bool:
    return self._remaining_time == 0  

  def __str__(self) -> str:
    return f"Task({self.name}, {self.is_high_priority}, {self._remaining_time})"

  def __repr__(self) -> str:
    return str(self)
    

def new_task() -> Task:
  name = chr(ord("A") + i)
  is_high_priority = True if random() > 0.6 else False
  remaining_time = randint(50, 400)
  return Task(name, is_high_priority, remaining_time)

def new_tasks(n: int) -> Queue[Task]:
  result = Queue()
  for _ in full_range(1, n):
    result.enqueue(new_task())
  return result
