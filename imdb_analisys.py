import pandas as pd
import matplotlib.pyplot as plt

dataset_address = 'E:\data analysis\s4\imdb_top_250.csv'

df = pd.read_csv(dataset_address)

count_by_genre = df['Genre'].value_counts() 
count_by_genre_top20 = count_by_genre.head(20)
plt.bar(df['Genre'].head(20),count_by_genre_top20)
plt.ylabel('Number of films')
plt.xlabel('Geners')
plt.show()
  
plt.bar(df['Title'].head(10),df['Rating count'].head(10))
plt.show()

rc_li = []
title_li = []
li = list(df['Rating count'])
for i in range (5):
    x = max(li)
    x_index = df[df['Rating count'] == x].index
    title = str(df.iloc[x_index]['Title'])
    rc_li.append(x)
    title_li.append(title)
    li.remove(x)

plt.bar(title_li,rc_li,width=0.1)
plt.show()

print(df[df['Year'] == 1999])

count_by_years = df['Year'].value_counts()
plt.bar(df['Year'].head(80),count_by_years.head(80))
plt.xlabel('The year')
plt.ylabel('Number of films')
plt.show()

print(f'the oldest film is built in {min(df['Year'])}')
film_index = (df[df['Year'] == min(df['Year']) ].index)
print(f'The name of film is {str(df.iloc[film_index]['Title'])}')

print(df.head(50)[df['Genre'] == 'Action' ])
print('===============================================================================================================================================================')
print(df.head(50)[df['Genre'] == 'Western' ])

count_by_directors = df.head(50)['Director'].value_counts()
print((count_by_directors))