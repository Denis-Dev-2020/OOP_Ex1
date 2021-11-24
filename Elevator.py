class Elevator:
    #----- Status : 0 - Standing , 1 - Moving Up , 2 - Moving Down -----#
    Status = 0
    DoorIsOpen = False
    #-------------------------------------------------------------------#
    #------------ basic elevator data took from indexed list -----------#
    def __init__(self,ElevatorListIndexed,TotalFloorsFromBuildingObj,NumberOfElevatorsFromBuildingObject,ElevNum__):
        self.ID_ = ElevatorListIndexed["_id"]
        self.Speed_ = ElevatorListIndexed["_speed"]
        self.MinFloor_ = ElevatorListIndexed["_minFloor"]
        self.MaxFloor_ = ElevatorListIndexed["_maxFloor"]
        self.CloseTime_ = ElevatorListIndexed["_closeTime"]
        self.OpenTime_ = ElevatorListIndexed["_openTime"]
        self.StartTime_ = ElevatorListIndexed["_startTime"]
        self.StopTime_ = ElevatorListIndexed["_stopTime"]
        self.SetMemory = {''}
        self.TotalTimeCount = 0
        self._FloorJumps = int(TotalFloorsFromBuildingObj/NumberOfElevatorsFromBuildingObject)
        self.CurrentFloor = self.MinFloor_+((ElevNum__)*self._FloorJumps)+int(NumberOfElevatorsFromBuildingObject/2)
        self._EleNum_ = ElevNum__+1
    #-------------------------------------------------------------------#
    def AddCall2Elevator(self,eCall ,_CurrentFloor_):
        self.SetMemory.add(eCall)
    #------------------------------------------ print override --------------------------------------------------------#
    def __str__(self):
        print("----------------------- Elevator #% s ------------------------\n :::- Core Values -:::\nID = % s\n" \
               "Speed = % s\nMinFloor = % s\nMaxFloor = % s\n" \
               "CloseTime = % s\nOpenTime = % s\nStartTime = % s\nStopTime = % s\n" \
               " :::- Dynamic Values -:::\nStatus = % s\nDoorIsOpen = % s\n" \
               "CurrentFloor = % s\nNumber Of Calls = % s\nTotal Time Spent On Calls = % s\n" \
               "---------------------------------------------------------------" % (self._EleNum_,self.ID_, self.Speed_, self.MinFloor_, self.MaxFloor_,
                     self.CloseTime_, self.OpenTime_, self.StartTime_, self.StopTime_,
                                                     self.Status,self.DoorIsOpen,
                                                     self.CurrentFloor,len(self.SetMemory),self.TotalTimeCount))
        # for i in range(0,len(self.SetMemory)):   #  <----- Shows the calls to each elevator
        #      print(list(self.SetMemory)[i])
        return " "
    #------------------------------------------------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
