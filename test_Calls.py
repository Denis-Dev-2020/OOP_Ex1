import unittest
from Calls import Calls

CallListFixed = list([])
for i in range(0, Calls("Ex1_Calls/Calls_a.csv", 0).HowManyCalls):
    CallListFixed.append(Calls("Ex1_Calls/Calls_a.csv", i))

class TestCalls(unittest.TestCase):
    def testArea(self):
        ###   Checks if calls receives the right inputs   ###
        self.assertGreaterEqual(len(CallListFixed),1)
        self.assertGreaterEqual(int(CallListFixed[0].HowManyCalls),1)
        self.assertGreaterEqual(float(CallListFixed[0].timeCalled),0.0)
        self.assertTrue(int(CallListFixed[0].WhichEleAssigned)>=-1)
        self.assertTrue(isinstance(int(CallListFixed[0].OriginFloor),int))
        self.assertTrue(isinstance(int(CallListFixed[0].DestinationFloor),int))
