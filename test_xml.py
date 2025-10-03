import xml.etree.ElementTree as ET

# با دیکشنری

di = {"name":"taha",'surname':"safi",'age':"132"}

root = ET.Element('person')

for i in di:
    sub = ET.SubElement(root,i)
    sub.text = di[i]

data_xml = ET.tostring(root)
print(data_xml)
print(di)

tree = ET.fromstring(data_xml)
for i in tree:
    print(i.tag,i.text)
    
# با لیست

root = ET.Element('personal_info')

titles = ['name','lname','age']
info = ['taha','safi','13']
x=0

for i in titles:
    sub = ET.SubElement(root,i)
    sub.text = info[x]
    x+=1

data_xml = ET.tostring(root)
print(f'data xml : {data_xml}',f'type : {type(data_xml)}')

tree = ET.fromstring(data_xml)
for i in tree:
    print(i.tag,i.text)
print(dir(ET))