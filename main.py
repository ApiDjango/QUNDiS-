import xml.etree.ElementTree as ET
import csv
tree = ET.parse("1.xml")
root = tree.getroot()

f = open('out.csv', 'w')

csvwriter = csv.writer(f)

count = 0

head = ['Показание, Дата, Номер счетчика']

csvwriter.writerow(head)

for measuredev in root.findall('network/measuredev'):
        row = [] 
        for datapoint in measuredev.findall('datapoint'): 
            if datapoint.find('storagenr').text == '1':
                value = datapoint.find('value').text
                row.append(value)
                #csvwriter.writerow(row)
                #print(row)
        for fixeddataheader in measuredev.findall('fixeddataheader'):
            identnr = fixeddataheader.find('identnr').text
            row.append(identnr)
        csvwriter.writerow(row)
f.close()