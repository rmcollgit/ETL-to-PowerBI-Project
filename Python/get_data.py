import kagglehub
import pandas as pd

# Downloading data
path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
#
print("Path to dataset files:", path)

#finding file name
import os
print("File name:")
for root, dirs, files in os.walk(path):
    for name in files:
        print(os.path.join(root, name))


