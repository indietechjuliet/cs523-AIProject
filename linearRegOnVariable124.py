#!usr/bin/python

"""
  Author: Adam Tutko
  Description: This program checks applicants to Moogle against a set of criterion
               and if they pass all of them accepts them as an applicant to consider

  Date: 08-30-2021
"""

import pandas as pd
from sklearn.linear_model import LinearRegression


def main():
  
  data = pd.read_csv('dataWithHeaders.csv')
  print(data)


if __name__ == "__main__":
    main()
