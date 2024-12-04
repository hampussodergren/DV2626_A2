from ucimlrepo import fetch_ucirepo 
import pandas as pd

# fetch dataset 
spambase = fetch_ucirepo(id=94) 
  
# data (as pandas dataframes) 
X = spambase.data.features 
y = spambase.data.targets 
  
# metadata 
#print(spambase.metadata) 
  
# variable information 
#print(spambase.variables) 

data = pd.concat([X, y], axis = 1)

print(data.head())