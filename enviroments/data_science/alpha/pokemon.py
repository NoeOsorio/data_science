
import pandas as pd

data = pd.read_csv('Pokemon.csv', index_col='#')

def get_data():
    print(data.head())


if __name__ == '__main__':
    get_data()

