import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
mydata = pd.read_csv("/melb_data.csv")
#mydata.head()
#mydata.columns

#defining the predictive feature
y = mydata.Price #storing the prices of houses in y
#mydata.columns

#defining the classification features
features=["Rooms","Landsize","Bathroom",'BuildingArea', 'YearBuilt', 'Lattitude',
       'Longtitude']
x =mydata[features]
#x.head()

#define the model
model = DecisionTreeRegressor(random_state=1)

#splitting the data
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,train_size=0.90)


#fitting model
model.fit(x_train,y_train)

#predicting
predictions=model.predict(x_test.head())

#evaluating the model
mae=mean_absolute_error(y_test.head(),predictions)
print(mae)