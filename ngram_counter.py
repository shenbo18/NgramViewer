''' 
This module provides model needed for ngram_viewer.
It contains function:
1. ngramCounter

Bo Shen
11/26/2017
'''

from os import listdir
from os import getcwd
from os import path
import pandas as pd
from collections import deque
from os import listdir
from os import makedirs

# Function: ngramCounter 
# This function first try to read the csv file associated with ngram
# if the csv file does not exist, it will iterate through all text folder 
# and read all text files to create a pandas dataframe of ngram frequencies
def ngramCounter(n):
    cwd = getcwd() 
    folders = listdir(cwd)
    if 'output' not in folders:
        makedirs('output')

    ngramCSV = 'output/' + str(n) + 'gram.csv'
    # if ngramCounter has been run and result has been saved to a csv file
    if path.isfile(ngramCSV):
        return pd.read_csv(ngramCSV, index_col = 0)

    # if ngramCounter has not been run before
    df = pd.DataFrame()

    # obtain folders contain text files
    candidate_folders = set([str(year) for year in range(1912, 2018)])
    text_folders = [folder for folder in folders if folder in candidate_folders]
    
    # folder contains text files from specific year
    for folder in text_folders:
        counter = {}
        # read all files from the folder of specific year
        for fileName in listdir(folder):
            with open( folder + '/' + fileName) as f:
                ngram_temp = deque()
                for word in f.read().split():
                    #print word
                    ngram_temp.append(word)
                    if len(ngram_temp) == n:
                        #print ngram_temp
                        ngram = ' '.join(ngram_temp)
                        ngram_temp.popleft()
                        if ngram in counter:
                            counter[ngram] += 1
                        else:
                            counter[ngram] = 1
        
        # each folder create a column in the dataframe
        s = pd.Series(counter)
        s.name = folder
        df = df.join(s, how = 'outer')

    # fill missing values with 0    
    df.fillna(value = 0, inplace = True)
    # save the dataframe as csv 
    df.to_csv(ngramCSV)

    return df