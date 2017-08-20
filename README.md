# Pandas-Multi-Colomn-Processor

1. *MultiColomnLabelEncoder* can be used to label all categorical colomns in a pandas data-frame via preprocessing.LabelEncoder (in scikit-learn). After this transformation the colomns data-types will remain the same as the original ones (e.g. categorical colomns will be still categorical). The object created here (after fitting) can be saved and later be used to transform other pandas data-frames with the same categorical colomns.

2. *MultiColomnOneHotEncoder* can be used to apply preprocessing.OneHotEncoder (in scikit-learn) on multiple categorical colomns in a pandas data-frame; this method will be applied only on categorical colomns. The object created here (after fitting) can be saved and later be used to transform other pandas data-frames with the same categorical colomns.

3. *MultiColumnScaler* is the same as preprocessing.MinMaxScaler in scikit-learn. The created object can be saved for transforming new data-frames with the same categorical colomns.


### How to install:
Type the following command in the terminal:

~$ pip install MultiColProcessor

### Example:
from MultiColProcessor import MultiColProcessor as mcp

MultiColumnLabelEncoder = mcp.MultiColomnLabelEncoder()
MultiColumnLabelEncoder.fit(data=aDataFrame)
transformed1 = MultiColumnLabelEncoder.transform(data=aDataFrame)
 
MultiColumnOneHotEncoder = mcp.MultiColomnOneHotEncoder()
MultiColumnOneHotEncoder.fit(data=transformed1)
transformed2 = MultiColumnOneHotEncoder.transform(data=transformed1)
 
MultiColumnScaler = mcp.MultiColomnScaler()
MultiColumnScaler.fit(data=transformed2)
finalDataFrame = MultiColumnScaler.transform(data=transformed2)

**note: MultiColumnLabelEncoder, MultiColumnOneHotEncoder and/or MultiColumnScaler can be saved and later be used for new data-frames with the same categorical colomns.**

