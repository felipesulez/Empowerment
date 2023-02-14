import pandas as pd
from collections import Counter


# Path of data

path1 = '/Users/felipesulez/Documents/Emporwerment/DataSets/news.csv'

# Transforming Excel file to CSV format
"""
# Raw Data
#data = pd.read_excel('/Users/felipesulez/Documents/Emporwerment/DataSets/news(1).xlsx') 
# Transforming Data to the CSV format
#data.to_csv('/Users/felipesulez/Documents/Emporwerment/DataSets/news.csv',sep = ',', header=True, index=False) 

"""
# load the data

def read_to_csv(path):

    dataframe = pd.read_csv(path)
    data = dataframe.loc[:,['content','classification']] # Select the interesting columns
    label = {'economy':1, 'sports':2, 'science':3, 'entertainment':4, 'culture':5}
    categorical_label = {'classification': {1:'economy', 2:'sports', 3:'science', 4:'entertaiment', 5:'culture'}}

    # Mapping the data into the ordered classification
    data['classification'] = data['classification'].map(label)
    newdata = data.sort_values('classification',ascending=True, ignore_index=True) # Organize the ordered values index
    newdata['classification'] = newdata['classification'].map(categorical_label['classification'])
    return newdata

data_csv = read_to_csv(path1)

# Create the function 

def repetead_words(dataframes, number_words):
    datos = dataframes
    c = datos['content']
    l = datos['classification']
    colum_l = []
    subcoluml = []
    my_list = []
    sublist = []
    for i in range(len(c)):
        my_list = c[i].split()
        sublist.append(my_list)
        colum_l = l[i].split()
        subcoluml.extend(colum_l)
        list_words = []
        repetead_words = []
        new_list = []
        for k in range(len(sublist)):
            words = sublist[k]
            for word in words[k]:
                list_words.append(words[k].count(word))
                repetead_words = words[max(list_words)]
                new_list.append(repetead_words)
                unique_words = []
                for j in new_list:
                    if j not in unique_words:
                        unique_words.append(j)
                        
    return print(f' The most repeat words are: {unique_words[0:number_words]} \n and its classification are: {subcoluml[0:number_words]}')
   
    
b = repetead_words(data_csv,6)
