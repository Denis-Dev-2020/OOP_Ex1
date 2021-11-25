import unittest
from Elevator import Elevator
from FileImporting import openJSON_BuildingFile

data = openJSON_BuildingFile("Ex1_Buildings/B1.json")
example1 = data["_elevators"][0]
example2 = {
      "_id": 0,
      "_speed": 0.5,
      "_minFloor": -2,
      "_maxFloor": 10,
      "_closeTime": 2.0,
      "_openTime": 2.0,
      "_startTime": 3.0,
      "_stopTime": 3.0
    }

class TestElevator(unittest.TestCase):
    def testArea(self):
        ###   Checks if elevator receives the right inputs and can actually create an object  ###
        self.assertGreaterEqual(Elevator(example1,100,1,1).ID_,0)
        self.assertGreater(Elevator(example1,100,1,1).Speed_,0)
        self.assertGreater(Elevator(example1,100,1,1).CloseTime_,0)
        self.assertGreater(Elevator(example1,100,1,1).OpenTime_,0)
        self.assertGreater(Elevator(example1,100,1,1).StartTime_,0)
        self.assertGreater(Elevator(example1,100,1,1).StopTime_,0)
        self.assertTrue(int(Elevator(example1,100,1,1).MinFloor_),int)
        self.assertTrue(int(Elevator(example1,100,1,1).MaxFloor_),int)
        self.assertGreaterEqual(Elevator(example2,100,1,1).ID_,0)
        self.assertGreater(Elevator(example2,100,1,1).Speed_,0)
        self.assertGreater(Elevator(example2,100,1,1).CloseTime_,0)
        self.assertGreater(Elevator(example2,100,1,1).OpenTime_,0)
        self.assertGreater(Elevator(example2,100,1,1).StartTime_,0)
        self.assertGreater(Elevator(example2,100,1,1).StopTime_,0)
        self.assertTrue(int(Elevator(example2,100,1,1).MinFloor_),int)
        self.assertTrue(int(Elevator(example2,100,1,1).MaxFloor_),int)
