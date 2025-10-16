# For Codio
try:
  from sys import argv
  import subprocess
  keywords = {"exercise", "example", "solution", "coursework", "practise", "test", "revision"}
  if not any(x in argv[-1] for x in keywords):
    from colortext import printc
    printc("To carry out this action, please click on a suitable Python file (e.g. examples, exercises, solutions, or coursework) to be the target, and then try again.", "light-red")
    printc("Press Enter to close this tab", "light-green")
  else:
    subprocess.run(argv[1:])
  input()
except KeyboardInterrupt:
  pass
