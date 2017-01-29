 """ 
    Linear regression to make prediction on life expectancy from body mass index (BMI) from birth
    """

# TODO: Add import statements
import pandas as pd
from sklearn.linear_model import LinearRegression

# TODO: Load the data
bmi_life_data = pd.read_csv('../resource/data/bmi_and_life_expectancy.csv') 

# Assign the dataframe to this variable.
features = pd.DataFrame(bmi_life_data, columns=["BMI"])
labels = pd.DataFrame(bmi_life_data, columns=["Life expectancy"])

# Make and fit the linear regression model
bmi_life_model = LinearRegression()

#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model.fit(features, labels) 

# Mak a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict(21.07931)