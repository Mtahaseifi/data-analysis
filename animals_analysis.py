import pandas as pd
import matplotlib.pyplot as plt

FileAddress = 'E:\data analysis\s3\zoo.csv'
df = pd.read_csv(FileAddress)

li1 = 0
li2 = 0
li3 = 0
li4 = 0
li5 = 0
li6 = 0
li7 = 0

type_li = list(df['class_type'])
for i in type_li:
    match i:
        case 1:
            li1 += 1
        case 2:
            li2 += 1
        case 3:
            li3 += 1
        case 4:
            li4 += 1
        case 5:
            li5 += 1
        case 6:
            li6 += 1
        case 7:
            li7 += 1
animal_types = ['Mamals','Birds','Reptiles','Fishes','Amphibianc','Bugs','Invertebrates']

print(f'Mamals : {li1}')
print(f'Birds : {li2}')
print(f'Reptiles : {li3}')
print(f'Fishes : {li4}')
print(f'Amphibianc : {li5}')
print(f'Bugs: {li6}')
print(f'Invertebrates : {li7}')

plt.bar(animal_types,[li1,li2,li3,li4,li5,li6,li7])
plt.ylabel('Number of animals')
plt.xlabel('Name of animals')
plt.show()

# دیتافریم پستانداران
mamals_df = df[df['class_type'] == 1]
print('mamals common features :')
for i in range(3):
    for c in mamals_df.columns:
        if (mamals_df[c] == i).all():
            print(c)

# دیتافریم ابزیان
fishes_df = df[df['class_type'] == 4]
print('fishes common features :')
for i in range(3):
    for c in fishes_df.columns:
        if (fishes_df[c] == i).all():
            print(c)

# دیتاست پرندگان
birds_df = df[df['class_type'] == 2]
print('birds common features :')
for i in range(3):
    for c in birds_df.columns:
        if (birds_df[c] == i).all():
            print(c)
birds_df.to_csv('birds_only.csv',index=False)

# دیتافریم حیواناتی که اهلی اند و پستاندار نیستند
domestic_df = df[df['domestic'] == 1]
domestic_df = domestic_df[domestic_df['class_type'] !=1]
print(domestic_df)
print('__________________________________________________________________________________________')

# حیوان اهلی سمی
venomous_df = df[df['venomous'] == 1]
venomous_df = venomous_df[venomous_df['domestic'] == 1]
print(f'{venomous_df['animal_name'].to_string()} is domestic, but venomous ')
print('__________________________________________________________________________________________')

# دیتافریم حیواناتی که هم سایز گربه اند و دم دارند
catsize_df = df[df['catsize'] == 1]
catsize_df = catsize_df[catsize_df['tail'] == 1]
print(catsize_df['animal_name'].to_list()) 