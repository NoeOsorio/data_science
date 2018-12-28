import pandas as pd

df = pd.read_csv('data.csv')

def get_data():
    print(df.head())

if __name__ = "__main__":
    get_data()
