from FileImporting import openCSV_Calls
#--------------- Elevator Calls Object That Stores Data -------------------------------#
class Calls:
    def __init__(self,CallsListIndexed,index):
        self.CallsDataList = list(openCSV_Calls(CallsListIndexed))
        self.timeCalled = self.CallsDataList[index][1]
        self.OriginFloor = self.CallsDataList[index][2]
        self.DestinationFloor = self.CallsDataList[index][3]
        self.WhichEleAssigned = self.CallsDataList[index][5]
        self.HowManyCalls = len(self.CallsDataList)
        self.iiindex = index
    def __str__(self):
        # print("________________________________________________ Call Number #% s ________________________________________________________\n"
        #       "Time Called : % s  ||  Origin Floor = % s  ||  Destination Floor = % s  ||  "
        #       "Which Elevator ID Assigned = % s\n"
        #       "_________________________________________________________________________________________________________________________" % (self.iiindex, self.timeCalled,
        #                                                       self.OriginFloor,
        #                                                       self.DestinationFloor,
        #                                                       self.WhichEleAssigned))
        #print("Elevator call,% s,% s,% s,0,% s"%(self.timeCalled,self.OriginFloor,self.DestinationFloor,self.WhichEleAssigned))
        #self.CallsDataList.pop(self.iiindex)
        return "Elevator call,% s,% s,% s,0,% s"%(self.timeCalled,self.OriginFloor,self.DestinationFloor,self.WhichEleAssigned)