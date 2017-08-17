import pandas as pd
from sklearn import preprocessing

"""
MultiColumnLabelEncoder class can be used to label all categorical colomns in a pandas data-frame
via preprocessing.LabelEncoder. After this transformation the colomns data-types will remain the same
as the original ones (e.g. categorical colomns will be still categorical). The object created here 
(after fitting) can be saved and later be used for other pandas data-frames with the same categorical 
colomns.
"""

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