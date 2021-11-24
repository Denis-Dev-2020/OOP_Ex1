import operator
import sys
from Calls import Calls
from FileImporting import openJSON_BuildingFile
from FileImporting import ExportOutputCSV
from Elevator import Elevator
import csv
CallListFixed = list([])
for i in range(0, Calls("Ex1_Calls/" + sys.argv[2], 0).HowManyCalls):
    CallListFixed.append(Calls("Ex1_Calls/" + sys.argv[2], i))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ELEVATOR OBJECT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class ElevatorCount:
    Num = 1
########################################################################################
################################## Building Object #####################################
########################################################################################
class Building:
    def __init__(self,Building_strPath):
        #~~~~~~~~~~~~~~~~~~~~ basic data of the building ~~~~~~~~~~~~~~~~~~~~~~#
        self.data = openJSON_BuildingFile(Building_strPath)
        self.mostUsedFloor = 0
        self.minFloor = self.data["_minFloor"]
        self.maxFloor = self.data["_maxFloor"]
        self.ElevatorList = self.data["_elevators"]
        self.TotalFloors = self.maxFloor - self.minFloor
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #~~~~~~~~~~~~~~~~~~ elevators data of the building ~~~~~~~~~~~~~~~~~~~~#
        self.NumberOfElevators = len(self.ElevatorList)
        self.ElevatorObjectList = []
        for i in range(0,self.NumberOfElevators):
            self.ElevatorObjectList.append(Elevator(self.ElevatorList[i],self.TotalFloors,self.NumberOfElevators,i))
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Organize (self):
        j = 1
        FloorJumps = int(self.TotalFloors/self.NumberOfElevators)
        ElevatorCount.Num = ElevatorCount.Num +1
        #####______________________ Iteration Over Calls With Index To Each Call  ______________________________#####
        #####_______________________ Also Taking The Calls File From Argument #3  ______________________________#####
        #_Assignment Algorithm Should Be Here So Not All Calls Assigned To Every Elevator But Only The Closest Ones_#
        #______the algorithm runs on each elevator from general call list and substruct each call as it provided____#
        #___ the data structure for the call list built like a stack and every call that served the stack got poped_#
        ###_______________________________________________________________________________________________________###
        print(self.NumberOfElevators)
        print(CallListFixed)
        while len(CallListFixed)!=0 and self.NumberOfElevators > 1:
            for i in range(0,self.NumberOfElevators):
                CallListFixed[0].WhichEleAssigned = i
                self.ElevatorObjectList[i].TotalTimeCount = (int(self.ElevatorObjectList[i].TotalTimeCount)) + int(self.ElevatorObjectList[i].StartTime_) + int(self.ElevatorObjectList[i].CloseTime_) + (abs(int(CallListFixed[0].OriginFloor) - int(CallListFixed[0].DestinationFloor)) / int(self.ElevatorObjectList[i].Speed_)) + int(self.ElevatorObjectList[i].StopTime_) + int(self.ElevatorObjectList[i].OpenTime_)
                self.ElevatorObjectList[i].AddCall2Elevator(CallListFixed.pop(0),0)
        if self.NumberOfElevators == 1:
            while len(CallListFixed)!=0:
                CallListFixed[0].WhichEleAssigned = 0
                self.ElevatorObjectList[0].TotalTimeCount = (int(self.ElevatorObjectList[0].TotalTimeCount)) + int(
                    self.ElevatorObjectList[0].StartTime_) + int(self.ElevatorObjectList[0].CloseTime_) + (
                                                                        abs(int(CallListFixed[0].OriginFloor) - int(
                                                                            CallListFixed[0].DestinationFloor)) / (
                                                                    self.ElevatorObjectList[0].Speed_)) + int(
                    self.ElevatorObjectList[0].StopTime_) + int(self.ElevatorObjectList[0].OpenTime_)
                self.ElevatorObjectList[0].AddCall2Elevator(CallListFixed.pop(0), 0)
        #####______________________________________________________________________________________________________#####
    def OutputData(self):
        for i in range(0,self.NumberOfElevators):
            for j in range(1,len(self.ElevatorObjectList[i].SetMemory)):
                ExportOutputCSV(list(self.ElevatorObjectList[i].SetMemory)[j])
        data2sort = csv.reader(open('temp.csv',newline = ''))
        data2sort = sorted(data2sort, key=operator.itemgetter(1))
        with open('OutputFinal.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data2sort)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ print override ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def __str__(self):
        print("####################################### Building ###############################################\n" \
                "minFloor : % s\nmaxFloor : % s\nNumberOfElevators : % s\n" \
                "mostUsedFloor : % s\n" 
                "################################################################################################\n" % (self.minFloor,
                                                                self.maxFloor,
                                                                self.NumberOfElevators,
                                                                self.mostUsedFloor))
        for i in range(0,self.NumberOfElevators):
            print(self.ElevatorObjectList[i])
        return ""
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#########################################################################################
############################## MAIN FUNCTION ############################################
if __name__ == '__main__':
    a1 = Building("Ex1_Buildings/"+sys.argv[1])
    a1.Organize()
    print(a1)
    a1.OutputData()
########################################################################################