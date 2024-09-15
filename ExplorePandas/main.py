import pandas as pd

#DataFrame
data = {
    'Name' : ['Steve','Bree'],
    'Age' : [21,20],
    'Course' : ['CyberSecurity','CS']
}
index= ['Student1','Student2']

df =pd.DataFrame(data,index= index)
print(df)
print("\n")

#Series
data1 = {
    'Sugar': '3 kgs',
    'Butter': '1 kg',
    'Flour': '2 kgs'
}

# Create a Pandas Series with the data and index
data1 = pd.Series(data1)
data1.name = 'List'

# Display the Series
print(data1)