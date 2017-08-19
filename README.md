# Pandas-Multi-Colomn-Processor

1- MultiColumnLabelEncoder can be used to label all categorical colomns in a pandas data-frame via preprocessing.LabelEncoder (in scikit-learn). After this transformation the colomns data-types will remain the same as the original ones (e.g. categorical colomns will be still categorical). The object created here (after fitting) can be saved and later be used for other pandas data-frames with the same categorical colomns.

2- MultiColumnOneHotEncoder can be used to apply preprocessing.OneHotEncoder (in scikit-learn) on multiple categorical colomns in a pandas data-frame; this method will be applied only on categorical colomns. The object created here (after fitting) can be saved and later be used for other pandas data-frames with the same categorical colomns.

3- MultiColumnScaler is the same as preprocessing.MinMaxScaler in scikit-learn. The created object can be saved for future uses.


## How to clone this repository via the command line in Linux:
1- First, install git if it is not already installed by typing the following command in the terminal:
sudo apt-get install git

2- Intsall the package by typing the following command in the terminal:
git clone https://github.com/mekhod/Pandas-Multi-Colomn-Processor.git
