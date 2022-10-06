from operator import index
import numpy as np
import matplotlib.pyplot as plt
import torch
import pandas as pd
import os
import sys
import re


A = torch.arange(6, dtype=torch.float32).reshape(2, 3)
B = torch.arange(6, dtype=torch.float32).reshape(3, 2)
x = torch.arange(3, dtype=torch.float32)

print(A)
print(x)
print(A@x)
