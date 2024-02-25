import matplotlib.pyplot as pt
import numpy as np
import pandas as pd


dataSetPath = 'dataset.csv'
columns = [
    "Number of times pregnant",
    "Plasma glucose concentration a 2 hours in an oral glucose tolerance test",
    "Diastolic blood pressure (mm Hg)",
    "Triceps skin fold thickness (mm)",
    "2-Hour serum insulin (mu U/ml)",
    "Body mass index (weight in kg/(height in m)^2)",
    "Diabetes pedigree function",
    "Age (years)",
    "Class variable (0 or 1)"
]
df = pd.read_csv(dataSetPath, header=None,names=columns )
df = df.astype(float)
meanValues = df.mean()
varianceValues = df.var() 
stdDeviationValues = df.std()


pt.figure(figsize=(12,12))
pt.subplot(3, 1, 1)
meanValues.plot(kind='barh', color='skyblue')
pt.title('Середнє арифметичне')
pt.tight_layout()

pt.subplot(3, 1, 2)
varianceValues.plot(kind='barh', color='skyblue')
pt.title('Дисперсія')
pt.tight_layout()
pt.subplot(3, 1, 3)
stdDeviationValues.plot(kind='barh', color='skyblue')
pt.title('Середнє квадратичне відхилення')
pt.tight_layout()
pt.show()