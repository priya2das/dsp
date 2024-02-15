import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
iris_data = sns.load_dataset("iris") 

sns.scatterplot(data=iris_data, x="sepal_length", y="sepal_width", hue="species")