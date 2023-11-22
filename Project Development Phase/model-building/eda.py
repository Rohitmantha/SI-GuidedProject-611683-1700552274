import pandas as pd
from ydata_profiling import ProfileReport


# Load the dataset
df = pd.read_csv('loan_prediction.csv')

prof = ProfileReport(df)
prof.to_file(output_file='output.html')