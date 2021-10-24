import json

j = None
with open("lang_en.json", "r") as f:
    j = json.load(f)

out = open("hyperlink_blocked.txt", "w")

for txtc, txt in j.items():
    txtl = txt.lower
    if "hyperlink" in txtl or "blocked" in txtl:
        out.write("%s\n%s\n\n" % txtc, txt)

out.close()
