#!/usr/bin/env python3

import re 

#define the story
concert = 'Katherine went to the concert to see Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out.'

#find all the 'katherine'
all = re.findall('[KkCc]ath.[a-z]*', concert, re.I)

#print name, start. end, and length in a tab format
for match in all:
    name = re.search(match, concert, re.I)
    length = len(name.group())
    iter = re.finditer(name.group(), concert, re.I)
    for att in iter:
        start = att.start()
        end = att.end()
    print(name.group(), '\t', start, '\t', end, '\t', length)