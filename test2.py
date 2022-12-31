import glob
import json

#specifying a path or directory
path = "input\\"
#getting all files in that directory
files = glob.glob(path+"*.json")

#all data will be stored here
allData = []

#combining all file data into one file
for file in files:
    loadFile = open(file)
    loadFileData = json.load(loadFile)
    allData.append(loadFileData)
    
#changing class name for all
for data in allData:
    for obj in data["objects"]:
        if obj["classTitle"] == "Vehicle":
            obj["classTitle"] = "car"
        elif obj["classTitle"] == "License Plate":
            obj["classTitle"] = "number"


#it will create "combined_files.json" which one will contain all the test json file data
try:
    newFile = open("combined_files.json", "x")
    newFile.write(json.dumps(allData, indent=4))

except:
    print("There is an error creating new combined file")