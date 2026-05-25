import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
data = pd.DataFrame({
 'Outlook': 
['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunn
y','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
 'Temperature': 
['Hot','Hot','Hot','Mild','Cool','Cool','Mild','Hot','Cool','Mild','
Mild','Mild','Hot','Mild'],
 'Humidity': 
['High','High','High','High','Normal','Normal','Normal','High','
Normal','Normal','Normal','High','Normal','High'],
 'Wind': 
['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','
Weak','Weak','Strong','Strong','Weak','Strong']
 'PlayTennis': 
['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','
Yes','No']
})
le = LabelEncoder()
encoded_data = data.copy()
for col in encoded_data.columns:
 encoded_data[col] = le.fit_transform(encoded_data[col])
 X = encoded_data.drop('PlayTennis', axis=1)
y = encoded_data['PlayTennis']
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)
sample = pd.DataFrame({
 'Outlook': ['Sunny'],
 'Temperature': ['Cool'],
 'Humidity': ['High'],
 'Wind': ['Strong']
})
for col in sample.columns:
 sample[col] = le.fit_transform(sample[col])
prediction = model.predict(sample)
print("Prediction (0=No, 1=Yes):", prediction[0])
