# Pandas-Multi-Colomn-Processor

1- MultiColumnLabelEncoder can be used to label all categorical colomns in a pandas data-frame
via preprocessing.LabelEncoder. After this transformation the colomns data-types will remain the same
as the original ones (e.g. categorical colomns will be still categorical). The object created here 
(after fitting) can be saved and later be used for other pandas data-frames with the same categorical 
colomns.

2- MultiColumnOneHotEncoder can be used to apply preprocessing.OneHotEncoder for multiple colomns in a pandas data-frame.
