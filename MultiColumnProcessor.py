import pandas as pd
import numpy as np
from sklearn import preprocessing

##
class MultiColumnLabelEncoder:
    ##
    def __init__(self):
        self.dataTypes = {}
        self.__catColumns = []
        self.__MultiLE = {}

    ## Later, self.dataTypes will be used to convert dtypes to the original ones.
    def __Get_Dtypes(self, data=pd.DataFrame()):
        ##to get original data datatypes
        for colomn in data.columns:
            self.dataTypes[colomn] = data[colomn].dtypes
        return self

    ##
    def fit(self, data):
        ##
        self.__Get_Dtypes(data)
        ##
        self.__catColumns = [cat for cat in self.dataTypes.keys()
                             if (self.dataTypes[cat].name == 'category')]
        ##
        for col in self.__catColumns:
            le = preprocessing.LabelEncoder()
            le.fit(data.loc[:, col])
            self.__MultiLE[col] = le
        ##
        return self

    ##
    def transform(self, data):
        ##
        transformedCols = data.drop(self.__catColumns, axis=1)
        ##
        for col in self.__catColumns:
            le = self.__MultiLE[col]
            transformed = le.transform(data.loc[:, col])
            transformed = pd.DataFrame(transformed)
            transformed.columns = [col]
            transformed.set_index(transformedCols.index, inplace=True)
            transformedCols = pd.concat([transformedCols, transformed], axis=1)
        ##
        for i, j in self.dataTypes.items():
            try:
                transformedCols[i] = transformedCols[i].astype(j)
            except:
                pass
        ##
        return transformedCols

##
class MultiColumnOneHotEncoder:
    ##
    def __init__(self):
        self.__catColumns = []
        self.OneHotEncoder = {}

    ##
    def __getCategoryColomns(self, data=pd.DataFrame()):
        catColumns = []
        for i, j in enumerate(data):
            if (data.dtypes[i].name == 'category'):
                catColumns.append(j)
            else:
                continue
        ##
        self.__catColumns = catColumns
        ##
        return

    ##
    def fit(self, data):
        ##
        self.__getCategoryColomns(data)
        ##
        for col in self.__catColumns:
            OneHotEncoder = preprocessing.OneHotEncoder(sparse=False)
            OneHotEncoder.fit(np.array(data.loc[:, col]).reshape(-1, 1))
            self.OneHotEncoder[col] = OneHotEncoder
        ##
        return self

    def transform(self, data):
        ##
        transformedCols = data.drop(self.__catColumns, axis=1)
        ##
        for col in self.__catColumns:
            OneHotEncoder = self.OneHotEncoder[col]
            transformed = OneHotEncoder.transform(np.array(data.loc[:, col]).reshape(-1, 1))
            transformed = pd.DataFrame(transformed)
            transformed.columns = [str(col) + '_' + str(c) for c in transformed.columns]
            transformed.set_index(transformedCols.index, inplace=True)
            transformedCols = pd.concat([transformedCols, transformed], axis=1)
        ##
        return transformedCols
