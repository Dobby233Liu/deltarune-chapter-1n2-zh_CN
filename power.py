import json

j = None
with open("lang_en.json", "r") as f:
    j = json.load(f)

out = open("hyperlink_blocked.txt", "w")

for txtc, txt in j.items():
    txtl = txt.lower()
    if "hyperlink" in txtl or "blocked" in txtl:
        o = ("%s\n%s\n\n" % (txtc, txt))
        print(o)
        out.write(o)

out.close()
