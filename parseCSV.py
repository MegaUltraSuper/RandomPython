#file io practice
import os.path
import random

def fillData(c=1,r=10):
    """fill data.csv file with random data
    c = # of sets of data(Columns)
    r = # of items in each set(Rows)"""
    with open("data.csv", mode='w') as data:
        #clear old data
        data.truncate(0)
        #create column titles 
        for num in range(c):
            
            s = str(num)
            data.write("Set"+s)
            if num == c-1:
                data.write('\n')
            else:
                data.write(',')
        for row in range(r):
            for col in range(c):
                num = random.randrange(1000)
                s = str(num)
                data.write(s)
                if col == c-1:
                    data.write('\n')
                else:
                    data.write(',')
    return

def parseCSV(file, ColumnNames=True):
    """parses csv file
    if first row is assumed to be Titles, data is stored into corresponding variables
    rest of data is per column basis"""
    DataSets = list()
    #open file
    with open(file, mode='r') as data:
        #get Titles
        Titles = data.readline()
        if Titles == "":
            return DataSets
        Titles = Titles.split(',')
        for title in Titles:
            DataSets.append(list())
        #get rest of data
        rows = data.readlines()
        for row in rows:
            nums = row.split(',')
            for index in range(len(nums)):
                n = int(nums[index].strip())
                DataSets[index].append(n)
    return DataSets
                    
        
