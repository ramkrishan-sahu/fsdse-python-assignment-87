#Create a one-dimensional array-like object containing an array of data
# https://app.commit.live/lesson/fsdse-python-assignment-87
import numpy as np
import pandas as pd

Lis = [2, 4, 6, 8, 10]

def solution(li):
    fin = pd.Series(li)
    print fin
    type (fin)
    return fin

solution(Lis)
