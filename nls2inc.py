# Convert an NLS file to an include file.
# Jason Hood, 4 & 5 July, 2025.

# Python 2, as I don't think there's a 3 for DOS, in case someone wants to run
# this natively (not that I tested it).

import sys

ErrorNrs = range(35, 35+5)
ProfileNr = 42

def convert(lang):
  nlsName = "NLS/DOSLFN." + lang
  try:
    with open(nlsName) as f:
      nls = f.readlines()
    inc = open("text.inc", "w")
  except:
    return
  # Copy the assumed language and code page comment.
  print >>inc, ";" + nls[0][1:],
  # Always starts with NL.
  print >>inc, " dz\t10\t\t\t\t\t\t\t;0"
  incond = inquote = firstquote = lastquote = False
  nr = 1
  for i, line in enumerate(nls):
    if not inquote and line[0] in ("#", "\n"):
      continue
    line = line.rstrip()
    if line[0] == '"':
      inquote = not inquote
      if inquote:
	firstquote = True
    elif line[0] == '?':
      if incond:
	print >>inc, "endif"
	incond = False
      else:
	incond = True
	print >>inc, (line[1] == 'P' and "ifdef " or "if ") + line[1:]
    else:
      if inquote:
	lastquote = nls[i+1] == '"\n'
	build = [lastquote and "  dz" or firstquote and " db " or "  db"]
      else:
	build = [" dz "]
      if line.startswith("\\n"):
	build.append("10,")
	line = line[2:]
      else:
	build.append("   ")
      nl = line.endswith("\\n")
      if nl:
	line = line[:-2]
      elif inquote and not lastquote:
	nl = True
      build.append('"')
      build.append(line.replace("\\s", " "))
      build.append('"')
      if nl:
	build.append(",10")
      built = "".join(build)
      if not inquote or firstquote:
	width = len(built.expandtabs())
	if width < 65:
	  built += "\t" * ((71 - width) / 8)
	if nr in ErrorNrs:
	  if nr == ErrorNrs[0]:
	    built += ";" + str(nr) + "  =   0"
	  else:
	    built += "\t;" + str(nr - ErrorNrs[0])
	elif nr == ProfileNr:
	  built += ";ProfileNr"
	elif nr >= ProfileNr:
	  built += ";+" + str(nr - ProfileNr)
	else:
	  built += ";" + str(nr)
	firstquote = False
      print >>inc, built
      if lastquote:
	print >>inc
      if not inquote or lastquote:
	nr += 1
	lastquote = False

  inc.close()

convert(sys.argv[1])
