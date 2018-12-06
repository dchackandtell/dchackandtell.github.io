'''
Hello DC Hack && Tell editors! This is a simple regex to INLINE replace
urls in a file with a markdown style. Eg. url becomes [url](url). This
was written to help clean the Google Doc notes to markdown. This is a python3
program.
'''

import sys, re
f = sys.argv[1]

with open(f) as FIN:
    raw = FIN.read()

PAT = re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')

#for line in raw.split('\n'):
#    print (line)
#    print (PAT.sub(r"[\1](\1)", line))

parsed = PAT.sub(r"[\1](\1)", raw)

with open(f, 'w') as FIN:
    FIN.write(parsed)

print("Output written to %s"%f)

# Notes copied from the [hackpad]([https://docs.google.com/document/d/1DM_qVHEGPNP-UzSGKNlee8lmroNqap4Fg4RgERxxTiY/edit#](https://docs.google.com/document/d/1DM_qVHEGPNP-UzSGKNlee8lmroNqap4Fg4RgERxxTiY/edit#))!
