import pandas as pd
import matplotlib.pyplot as plt

DatasetAddress = 'E:\data analysis\s2\AirQualityUCI.csv'
df = pd.read_csv(DatasetAddress,sep=';')

print(f'At first,there were {(df['CO(GT)'] == '-200').sum()} None datas')

df = df.replace('-200',pd.NA)
df = df.replace('-200.0',pd.NA)
df = df.dropna(subset=['CO(GT)','T'])

print(f'Then there are {(df['CO(GT)'] == '-200').sum()} None datas')

df.to_csv('new dataset.csv')

co_float_li = [float(num.replace(',','.'))for num in list(df['CO(GT)'])]
temp_float_li = [float(num.replace(',','.'))for num in list(df['T'])]

print(f'The tempreture of the coldest day : {min(temp_float_li)} ')
print(f'The tempreture of the warmest day : {max(temp_float_li)} ')

plt.scatter(co_float_li[0:20],temp_float_li[0:20])
plt.title('')
plt.xlabel('CO')
plt.ylabel('Tempreture')
plt.show()

plt.bar(['CO','Temp'],[sum(co_float_li)//len(co_float_li),sum(temp_float_li)/len(temp_float_li)])
plt.show()

plt.plot(df['T'].iloc[:120])
plt.title('Tempreture Chart')
plt.show()

plt.scatter(list(df['Time'][6:16]),temp_float_li[6:16])
plt.xlabel('Time')
plt.ylabel('Tempreture')

plt.show()
