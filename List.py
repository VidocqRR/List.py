

                                                    
myUniqueList  = []
myLeftovers = []

def AddTest(args):
    if args not in myUniqueList:
        myUniqueList.append(args)
        return True
    else:
        myLeftovers.append(args)

        return False




AddTest(1)
AddTest(2)
AddTest(3)
AddTest(4)
AddTest(5)
AddTest(2)
AddTest(4)
AddTest('Hello')
AddTest(1)


print(myUniqueList)
print(myLeftovers)
