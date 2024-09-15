import pandas as pd

data = {
    'Name' : ['Steve','Bree'],
    'Age' : [21,20],
    'Course' : ['CyberSecurity','CS']
}
index= ['Student1','Student2']

df =pd.DataFrame(data,index= index)
print(df)
