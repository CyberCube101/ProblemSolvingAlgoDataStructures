'''
AND
OR
NOT


We will use inheritance. From a Logic Gate class, we will have either
a Binary Gate( And OR) or we have a Unary Gate (Not)
'''


class LogicGate:
    def __init__(self, n):
        self.label = n  # label the gate
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()  # here we are implementing functionality that doesnt yet exist
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate" + self.getLabel() + "-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate" + self.getLabel() + "-->"))


class UnaryGate(LogicGate):
    def __int__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            print(1)
        else:
            print(0)


# g1 = AndGate("G1")
# print(g1.getLabel())
# g1.getOutput()


class OrGate(BinaryGate):
    def __int__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            print(0)
        else:
            print(1)


# g2 = OrGate("G2")
# print(g2.getLabel())
# g2.getOutput()


class NotGate(UnaryGate):
    def __int__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 0:
            print(1)
        elif a == 1:
            print(0)


# Now we can create our connector class...this will take an
# input from 1 gate and pass to another


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

    def setNextPin(self, source):
        if self.pinA == None:  # Pin A is default is both available
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate  " + self.getLabel() + " -->")
        else:
            return self.pinA.getFrom().getOutput()


'''
Now it is possible to get input from two places: externally, as before, 
and from the output of a gate that is connected to that input line. 
This requires a change to the getPinA and getPinB methods
If the input line is not connected to anything (None), then ask the user externally
 as before. However, if there is a connection, the connection is accessed
and fromgate’s output value is retrieved. 
This in turn causes that gate to process its logic. 
This continues until all input is available and the final output value b
ecomes the required input for the gate in question. 
In a sense, the circuit works backwards to find the input necessary to 
finally produce output.


'''
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
