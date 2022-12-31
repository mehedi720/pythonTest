
# this script will read file from the input folder and output all 
# the formated file in the output folder
# 

import glob
import json

#specifying a path or directory
path = "input\\"
#getting all files in that directory
files = glob.glob(path+"*.json")

#iterating over all the json files for formating 
for file in files:
    fileName = file.replace("input\\", "")

    #opening each file and parsing 
    jsonFile = open(file)
    jsonData = json.load(jsonFile)

    # formated data structure 
    fmData = {
        "dataset_name": fileName,
        "image_link": "",
        "annotation_type": "image",
        "annotation_objects": {
                "vehicle": {
                    "presence": 0,
                    "bbox": []
                },
                "license_plate": {
                    "presence": 0,
                    "bbox": []
                }
            },
        "annotation_attributes": {
                "vehicle": {
                    "Type": None,
                    "Pose": None,
                    "Model": None,
                    "Make": None,
                    "Color": None
                },
                "license_plate": {
                    "Difficulty Score": None,
                    "Value": None,
                    "Occlusion": None
                }
            }
    }

    def addValueAbout(x, y):
        aObj = fmData["annotation_objects"][x]
        aAtr = fmData["annotation_attributes"][x]
        aObj["presence"] = 1
        for box in y["points"]["exterior"]:
            aObj["bbox"] += box

        for atrType in y["tags"]:
            aAtr[atrType["name"]] = atrType["value"]

#add values by checking classTitle 
    def sepObj(x):
        if(obj["classTitle"] == "Vehicle"):
            return addValueAbout("vehicle", x)
        
        elif (obj["classTitle"] == "License Plate"):
            # not sure about occlusion
            fmData["annotation_attributes"]["license_plate"]["Occlusion"] = 0
            return addValueAbout("license_plate", x)

#iterating over all the objects on each file
    if len(jsonData["objects"]) > 0: 
        for obj in jsonData["objects"]:
                sepObj(obj)



    #writing data to files 
    print(json.dumps([fmData], indent=4))
    try: 
        file = open("output\\formated_"+fileName, "x") 
        file.write(json.dumps([fmData], indent=4))  
    except:
        print("This is an erron in file name: "+file)
   

