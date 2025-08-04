# Translate the UTF-8 text files to their corresponding code pages.
# Jason Hood, 2 August, 2025.

# Python 2, as I don't think there's a 3 for DOS, in case someone wants to run
# this natively (not that I tested it).


cp = {
  "de": "cp437",
  "en": "cp437",
  "es": "cp437",
  "fr": "cp850",
  "ja": "cp932",
  "ru": "cp866",
  "tr": "cp857",
  "zh": "cp936"
}


def tocp(name, page):
  try:
    f = open(name, "rb")
  except:
    # print "Ignoring ", name
    return
  utf8 = f.read()
  f.close()
  uc = utf8.decode("utf8")
  dos = uc.encode(page)
  cpname = name[:4] + "DOSLFN." + name[4:6].upper()
  if name.startswith("doc"):
    cpname = cpname.lower()
  f = open(cpname, "wb")
  f.write(dos)
  f.close()
  print "Converted", name, "to", cpname

for lang in cp:
    tocp("doc/" + lang + ".txt", cp[lang])
    tocp("NLS/" + lang + ".txt", cp[lang])
