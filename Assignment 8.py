#Standard Library Power‑Ups----------------------------------------------------------------------

# datetime
# Maths and
# Random

from datetime import datetime, timedelta
from math import sqrt
import random


print(datetime.now(), sqrt(49), random.choice(["yes", "no"]))


#Collections--------------------------------------------------------------------------------------------

from collections import Counter, defaultdict, deque


print(Counter("abracadabra"))
d = defaultdict(int)
d["x"] += 1
q = deque([1,2,3]); q.appendleft(0); print(q)

# itertools------------------------------------------------------------------------------------------
from itertools import permutations, combinations
print(list(permutations([1,2,3], 2)))
print(list(combinations([1,2,3], 2)))


#re (regex)---------------------------------------------------------------------------------
import re
text = "Email me at hello@example.com"
print(re.findall(r"[\w\.-]+@[\w\.-]+", text))

#subprocess,-------------------------------------------------------------------- 
# argparse, 
# logging

import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is a log message")


# Testing & Quality-------------------------------------------------------

#A) unittest
    
    # file: calc.py

def add(a, b):
 return a + b


# file: test_calc.py

import unittest

class TestCalc(unittest.TestCase):
 def test_add(self):
  self.assertEqual(add(2, 3), 5)

class TestCalc(unittest.TestCase):
 def test_add(self):
  self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
 unittest.main()