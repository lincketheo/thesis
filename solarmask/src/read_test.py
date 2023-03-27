from solarmask.data import read_mask
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


mask = read_mask(3344, datetime(2013, 11, 3, 3, 0, 0), "/srv/data/thli2739")


print(mask)
print(np.count_nonzero(mask))
print(mask.shape)
