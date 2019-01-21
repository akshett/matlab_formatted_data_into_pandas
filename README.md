# Loading Matlab formatted data (.mat) into pandas

There are many instances where we may have to switch between languages while working with data. One of the situations I came across recently was having to deal with data presented in matlab formatted (.mat) file while working in python. Thanks to denizens of the internet this was not much of an issue for me. However, I thought of presenting how to go over the data set if you are ever in this situation.

Firstly, Matlab formatted data refers to data stored in a .mat extension file which is binary data container designed by Matlab. For more information on this data format refer to: [Matlab Formatted Data](https://www.loc.gov/preservation/digital/formats/fdd/fdd000440.shtml)

For this exercise I am going to use `loadmat` function from `scipy` library to load the matlab data set and `pandas DataFrame` to store data in python. Let's say your matlab data is in a file named "data_set.mat".

In order to load data, we use the following lines of code:
```python
from scipy.io import loadmat

data_set = loadmat("data_set.mat")

```

Now the data is loaded into `data_set` variable which is essentially a dictionary. The level and complexity of encoding in the dictionary will depend upon the nature of your .mat file. Therefore, it is best to go over the dictionary to understand it.
```python
print(data_set.keys())
```

One of the keys of the dictionary will indicate labels which corresponds to column names in a pandas dataframe. In my file it is called `rows`. This data will mostly be stored in a list of 2d arrays consisting of column name and data type. There will another key refering to the actual data stored which will be list in the same order as the column names.

The following code will extract the data and store it in a dictionary
```python
rows = data_set['rows']
dataVal = data_set['data']
data_dict = {}

for i,v in enumerate(rows):
    data_dict[v[0][0]] = dataVal[i]
```

You must look at the `rows` variable above before extracting data from it. Once you have the data loaded in the dictionary, you create a pandas dataframe using that dictionary
```python
df = pd.DataFrame(data=data_dict)
```

Note: This is the simplest way to create dataframe in pandas. You can encode more information in the dataframe using options like `index`, `columns`

Reference: <https://stackoverflow.com/questions/38197449/matlab-data-file-to-pandas-dataframe>
