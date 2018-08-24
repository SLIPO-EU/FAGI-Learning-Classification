# This module contains helping functions for the project
# Author: Giorgos Kostoulas


import pandas as pd
import numpy as np

# Clean the data 
def transform(Z, b):
    for na in Z.columns:
        if Z[na].dtype== "bool":
            Z[na]= Z[na]*1
        elif Z[na].dtype == "object":
            if b:
                Z= pd.concat([Z, pd.get_dummies(Z[na])], axis=1)       
            Z.pop(na);
    return Z



def transform2(Z, test):
    for na in Z.columns:
        if Z[na].dtype== "bool":
            Z[na]= Z[na]*1
        elif Z[na].dtype == "object":
            #Z= pd.concat([Z, pd.get_dummies(Z[na])], axis=1)       
            test[na]=Z.pop(na);
    return Z


# swap the symetric values to double the data
def swap_symetric(Z):
    Z2=Z.copy(deep=True)
    col_list = list(Z)
    # use this handy way to swap the elements
    col_list[0], col_list[1] = col_list[1], col_list[0]
    col_list[2:5], col_list[5:8] = col_list[5:8], col_list[2:5]
    col_list[8], col_list[9] = col_list[9], col_list[8]
    col_list[10], col_list[11] = col_list[11], col_list[10]
    col_list[12], col_list[13] = col_list[13], col_list[12]
    col_list[14], col_list[15] = col_list[15], col_list[14]
    if ' nameFusionAction' in col_list:
        Z2[' nameFusionAction']=Z2[' nameFusionAction'].map({'Keep Right': 'Keep Left','Keep Left':'Keep Right',
                                                             'Keep longest/more complete value':'Keep longest/more complete value',
                                                             'Keep both as separate attributes/values':'Keep both as separate attributes/values'})   
    # assign back, the order will now be swapped
    Z2.columns = col_list
    Z2=Z2[list(Z)]
    return Z2

def transform_object_pair(Z, col1, col2):
    '''
    This function gets a Dataframe and the name of two colums
    and creates a binary column for each unique label of the columns 
    '''
    dim = Z.shape[0]
    Tmp = pd.get_dummies(pd.concat([Z[col1], Z[col2]], axis=0))  
    return Tmp[0:dim], Tmp[dim:2*dim]
