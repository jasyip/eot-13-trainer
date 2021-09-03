#!/usr/bin/env python3

import sys
import codecs

for line in sys.stdin:
    words = line.split(' ')
    converted = [codecs.encode(w[0], 'rot_13') + w[1:] for w in words]
    print(' '.join(converted), end='')
