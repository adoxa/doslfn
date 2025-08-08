# Translate the UTF-8 text files to their corresponding code pages.
# Jason Hood, 2 August, 2025.

# Python 2, as I don't think there's a 3 for DOS, in case someone wants to run
# this natively (not that I tested it).

import sys


cp = {
  "cz": "CP852",
  "de": "CP437",
  "dk": "CP865",
  "en": "CP437",
  "es": "CP850",
  "fi": "CP850",
  "fr": "CP850",
  "hu": "CP852",
  "it": "CP850",
  "ja": "CP932",
  "lv": "CP775",
  "nl": "CP850",
  "no": "CP865",
  "pl": "CP852",
  "pt": "CP860",
  "ru": "CP866",
  "sl": "CP852",
  "sv": "CP850",
  "tr": "CP857",
  "zh": "CP936"
}


def tocp(name, page):
  try:
    f = open(name, "rb")
  except:
    # print "Ignoring ", name
    return None
  utf8 = f.read()
  f.close()
  uc = utf8.decode("utf8")
  try:
    dos = uc.encode(page)
  except UnicodeEncodeError as e:
    print "Failed to encode", repr(e.object[e.start-5 : e.end+5]), "using", page + "."
    return False
  cpname = name[:4] + "DOSLFN." + name[4:6].upper()
  if name.startswith("doc"):
    cpname = cpname.lower()
  f = open(cpname, "wb")
  f.write(dos)
  f.close()
  print "Converted", name, "to", cpname
  return True


if len(sys.argv) == 1:
  for lang in cp:
    tocp("doc/" + lang + ".txt", cp[lang])
    tocp("NLS/" + lang + ".txt", cp[lang])
else:
  for arg in sys.argv[1:]:
    lang = arg[4:6]
    if lang in cp:
      tocp(arg, cp[lang])
    else:
      print arg, "has unknown lang:", lang
