


'''

Created on 

@author: Raja CSP Raman

source:
    
    
'''

import pandas as pd

def startpy():

    df = pd.read_csv("International Addresses with Premise number.csv")

    # print(df.head())

    df1 = df['Name']

    # df1.rename(columns={'Name': 'Address'}, inplace=True)
    df1.columns = ['Address']

    print(df1.head())

    df1.to_csv('input2.csv', index=False)


if __name__ == '__main__':
    startpy()