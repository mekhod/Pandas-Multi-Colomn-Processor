import pandas as pd
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
        catData = data[self.__catColumns]
        data = data.drop(self.__catColumns, axis=1)

        ##
        def Transform_Rec(dta=catData):
            ##
            nCol = dta.shape[1]
            ##
            if nCol == 1:
                col = dta.columns[0]
                le = self.__MultiLE[col]
                transformed = le.transform(dta.iloc[:, 0])
                transformed = pd.DataFrame({col: transformed})
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
        catData = Transform_Rec(dta=catData)
        catData.set_index(data.index, inplace=True)

        ##
        data = pd.concat([data, catData], axis=1)

        ##
        for i, j in self.dataTypes.items():
            try:
                data[i] = data[i].astype(j)
            except:
                pass
        ##
        return data