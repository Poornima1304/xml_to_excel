import xml.etree.ElementTree as ET
import os
import pandas as pd
import sys
file = sys.argv[1]

def readFile(filename):
    if not os.path.exists(filename):
        return
    tree = ET.parse(filename)
    root = tree.getroot()
    key_list = []
    for child in root:
        temp = []
        temp.append(child.tag)  
        temp.append(child.attrib)  
        key_list.append(temp)
    print(key_list)
    print(key_list[0][0])
    x = len(key_list)
    print(x)



    for a in range(0,x):
        a_tags = []
        a_attributes = []
        b_tags = []
        b_attributes = []
        c_tags = []
        c_attributes = []
        for child in root.iter(key_list[a][0]):
            temp1 = []
            temp2 = []
            for Connector in child.find('x'):
                temp1.append(Connector.tag)
                temp2.append(Connector.attrib)
            a_tags = temp1
            a_attributes = temp2
            temp3 = []
            temp4 = []
            for ECU in child.find('y'):
                temp3.append(ECU.tag)
                temp4.append(ECU.attrib)
            b_tags = temp3    
            b_attributes = temp4
            temp5 = []
            temp6 = []
            for Sensor in child.find('z'):
                temp5.append(Sensor.tag)
                temp6.append(Sensor.attrib)
            c_tags = temp5    
            c_attributes = temp6
        print(a_tags)
        print(a_attributes)
        print(b_tags)
        print(c_tags)
        filename_1 = r"path/to/destination_excel"
        df = pd.DataFrame({'Key_name': [key_list[a][0]]})


        df.to_excel(filename_1, sheet_name='Sheet1', index=False)


        df2 = pd.DataFrame({'x': a_tags}) 
        with pd.ExcelWriter(filename_1, engine="openpyxl", mode="a",if_sheet_exists='overlay') as writer:
            df2.to_excel(writer, sheet_name='Sheet1',startcol=1,index=False)
        df3 = pd.DataFrame.from_dict(a_attributes) 
        with pd.ExcelWriter(filename_1, engine="openpyxl", mode="a",if_sheet_exists='overlay') as writer:
            df3.to_excel(writer, sheet_name='Sheet1',startcol=2,index=False)
        df2 = pd.DataFrame({'y': b_tags}) 
        with pd.ExcelWriter(filename_1, engine="openpyxl", mode="a",if_sheet_exists='overlay') as writer:
            df2.to_excel(writer, sheet_name='Sheet1',startcol=6,index=False)
        df3 = pd.DataFrame.from_dict(b_attributes) 
        with pd.ExcelWriter(filename_1, engine="openpyxl", mode="a",if_sheet_exists='overlay') as writer:
            df3.to_excel(writer, sheet_name='Sheet1',startcol=7,index=False)
        df2 = pd.DataFrame({'z': c_tags}) 
        with pd.ExcelWriter(filename_1, engine="openpyxl", mode="a",if_sheet_exists='overlay') as writer:
            df2.to_excel(writer, sheet_name='Sheet1',startcol=8,index=False)
        df3 = pd.DataFrame.from_dict(c_attributes) 
        with pd.ExcelWriter(filename_1, engine="openpyxl", mode="a",if_sheet_exists='overlay') as writer:
            df3.to_excel(writer, sheet_name='Sheet1',startcol=9,index=False)

    



readFile(file)


