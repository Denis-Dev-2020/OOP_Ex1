import json
import csv
########################################################################################
################# Importing Data From Files (json,csv) Into Lists ######################
########################################################################################
def openCSV_Calls(path):
    csv_file = open(path,newline = '')
    CallsInfo = csv.reader(csv_file)
    data = [row for row in CallsInfo]
    #print(data)
    return data
def openJSON_BuildingFile(path):
    json_file = open(path)
    BuildingInfo = json.load(json_file)
    json_file.close()
    return BuildingInfo
########################################################################################
#################### Exporting Data To Output.csv Line By Line #########################
########################################################################################
def ExportOutputCSV(StringLine):
    report = open("temp.csv",'a')
    report.write("% s\n"%(StringLine))
    report.close()
########################################################################################