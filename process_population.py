#get just 1 column 
column = "S2901_C01_001E"

#get max and min
import csv
import json
import os

layers = ["city.csv",
"congress.csv",
"county.csv",
"countySubdivision.csv",
"places.csv",
"schoolDistrict.csv"]

def getMaxMin(fileName):
    with open("voters/"+fileName,"r")as inputFile:
        csvReader = csv.reader(inputFile)
    
        outputFileName = fileName.replace(".csv","")+"_s.csv"
        with open(outputFileName,"w")as outputFile:
            csvWriter = csv.writer(outputFile)
            csvWriter.writerow(["geoid","name","pop"])
            minPop = 99999999999
            maxPop = 0
    
            for row in csvReader:
                header = row
               # print (row)
                break
            for row in csvReader:
                #print (row)
                break
            for row in csvReader:
                #print (row)
                geoid = row[header.index("GEO_ID")]
                name = row[header.index("NAME")]
                value = int(row[header.index("S2901_C01_001E")])
                if value>maxPop:
                    maxPop = value
                if value<minPop:
                    minPop = value
                csvWriter.writerow([geoid,name, value])
            print("max:",maxPop,"min:",minPop)

for l in layers:
    print (l)
    getMaxMin(l)