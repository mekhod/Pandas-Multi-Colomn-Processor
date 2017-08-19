import pandas as pd
import numpy as np
from sklearn import preprocessing

##
class MultiColumnOneHotEncoder:
    ##
    def __init__(self):
        self.__catColumns = []
        self.__MultiOHE = {}

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
            self.__MultiOHE[col] = OneHotEncoder
        ##
        return self

    def transform(self, data):

        ##
        catData = data[self.__catColumns]
        data = data.drop(self.__catColumns, axis=1)

        ##
        def Transform_Rec(dta=catData):
            ##
            nCol = dta.shape[1]
            ##
            if nCol == 1:
                ##
                col = dta.columns[0]
                OneHotEncoder = self.__MultiOHE[col]
                transformed = OneHotEncoder.transform(np.array(dta.loc[:, col]).reshape(-1, 1))
                transformed = pd.DataFrame(transformed)
                transformed.columns = [str(col) + '_' + str(c) for c in transformed.columns]
                ##
                return transformed

            else:
                ##
                if (nCol % 2 == 0):
                    middle_index = int(nCol / 2)
                else:
                    middle_index = int(nCol / 2 - 0.5)
                ##
                left = dta.iloc[:, :middle_index]
                right = dta.iloc[:, middle_index:]
                ##
                return pd.concat([Transform_Rec(dta=left), Transform_Rec(dta=right)], axis=1)

        ##
        transformedCatData = Transform_Rec(dta=catData)
        transformedCatData.set_index(data.index, inplace=True)

        ##
        return pd.concat([data, transformedCatData], axis=1)