from constants import s
from sys import argv
from json import load
from traceback import format_exc, print_exc
a, b, *c = argv
try:
  exec(open(a).read())
except Exception as e:
  print(s[0])
  raise e
try:
  with open(b, "r") as d:
    e = load(d)
  f = e[s[1]]
  ts = e[s[2]]
  h = {}
  i = c if c else f
  for f in i:
    h[f] = [0, 0]
  for t in ts:
    for f in t[s[3]]:
      h[f][1] += 1
  j = 0
  for k, l in f.items():
    for t in ts:
      m = t[s[4]]
      n = []
      for o in l:
        n.append(m[o])
      t = f"{k}({', '.join(l)})"
      fcall = f"{k}({', '.join(n)})"
      if k in t[s[3]]:
        r = t[s[3]][k]
        try:
          p = str(eval(fcall))
        except Exception as e:
          p = s[8] + str("".join(("  File" + format_exc().split("File", 3)[-1]).split(s[5])).replace(s[6], s[7]).removesuffix("\n"))
        if p != r:
          if j == 4:
            print(s[9])
            j += 1
          elif j < 4:
            print(s[10])
            for o in l:
              print(f"{o} = {m[o]}")
            print(str(t), s[11] + str(p), s[12] + str(r), "", sep="\n")
            j += 1
        else:
          h[k][0] += 1
  if j == 0:
    print(s[13])
  else:
    print(s[14])
    for f, r in h.items():
      print(f"{f}: {r[0]}/{r[1]}")
except Exception as e:
  print(s[15])
  print_exc()


