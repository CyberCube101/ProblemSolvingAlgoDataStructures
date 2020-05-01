'''
AND
OR
NOT


We will use inheritance. From a Logic Gate class, we will have either
a Binary Gate( And OR) or we have a Unary Gate (Not)
'''


class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()  # here we are implementing functionality thats doesnt yet exist
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def pinA(self):
        return int(input("Enter Pin A input for gate" + self.getLabel() + "-->"))

    def pinB(self):
        return int(input("Enter Pin B input for gate" + self.getLabel() + "-->"))


class UnaryGate(LogicGate):
    def __int__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))




