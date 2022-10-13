#!/usr/bin/env python
# coding: utf-8

# ### get data

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split


# In[2]:


def get_data():
    data_file = 'quora_duplicate_questions.tsv'
    data = pd.read_csv(data_file, sep='\t', header=None, names=['id','qid1','qid2','question1', 'question2', 'label'],low_memory=False)
    data=data.drop(index=0)
    new_data = data[(data['label']==0) | (data['label']==1)]
    # get data and label
    x = data[['question1', 'question2']].values.tolist()
    y = data['label'].values.tolist()
    # split the data into training set and 5 testing set
    # training set is 10% of the data
    x_train, x_t, y_train, y_t = train_test_split(x, y, test_size=0.95, random_state=123, shuffle=True)
    # testing set devide the remaining into 5 parts
    test_length = int(0.95*len(x)/5)
    x_t, x_test1, y_t, y_test1 = train_test_split(x_t, y_t, test_size=test_length)
    x_t, x_test2, y_t, y_test2 = train_test_split(x_t, y_t, test_size=test_length)
    x_t, x_test3, y_t, y_test3 = train_test_split(x_t, y_t, test_size=test_length)
    x_test5, x_test4, y_test5, y_test4 = train_test_split(x_t, y_t, test_size=test_length)
    return x_train, x_test1, x_test2, x_test3, x_test4, x_test5, y_train, y_test1, y_test2, y_test3, y_test4, y_test5


# In[3]:


if __name__ == '__main__':
    x_train, x_test1, x_test2, x_test3, x_test4, x_test5, y_train, y_test1, y_test2, y_test3, y_test4, y_test5 = get_data()

