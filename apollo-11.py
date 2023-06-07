import plotly
import pandas as pd
import numpy as np

def command():
	print("We have touchdown")

list = [1]

for n in list:
	print(f"This is the {n} element")
	n = n + 1
	if n > 10:
		break
	else:
		list.append(n)
