# Decorator to show call stack.

# When calling a decorated function, pass an optional argument line=n 
# to show the line number in the call stack. This argument will not
# be passed to the decorated function. Therefore, the decorated function 
# must not rely on an optional argument called "line",
# otherwise the decorator will not work properly.

from stack import Stack

calls: Stack[str] = Stack()

def call_stack(f):
  def g(*x, **y):
    pre = ""
    if "line" in y:
      if y['line'] != None:
        pre = f"Line {y['line']}: "
      del y["line"]
    xs = [str(v) for v in x]
    ys = [f"{k}={v}" for k, v in y.items()]
    argsstr = ", ".join(xs + ys)
    s = pre + f"{f.__name__}({argsstr})"
    calls.push(s)
    print(calls)
    v = f(*x, **y)
    calls.pop()
    calls.push(pre + f"Returned: {v}")
    print(calls)
    calls.pop()
    return v
  return g
