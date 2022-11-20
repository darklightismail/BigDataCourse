#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re, sys
for line in sys.stdin:
        line = line.strip()
        #line = re.sub(r"[^\z\s]",'',line.lower())
        words=line.split()
        for word in words:
                print '%s\t%s' % (word,1)