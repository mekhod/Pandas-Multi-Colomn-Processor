import pandas as pd
from sklearn import preprocessing

##
class MultiColumnScaler:
        ##
        def __init__(self):
            self.scaler = object()

        ##
        def fit(self, data):
            ##
            self.scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
            self.scaler.fit(data)
            ##
            return self

        ##
        def transform(self, data):
            ##
            columns = data.columns.tolist()
            ##
            data = pd.DataFrame(self.scaler.transform(data.as_matrix()))
            ##
            data.columns = columns
            ##
            return data