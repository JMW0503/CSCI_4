
import sys

def main():
    class KeyLocation:
        
        def __init__(self):
            self.name = None
            self.hasKey = None


    location1 = KeyLocation()
    location2 = KeyLocation()
    location3 = KeyLocation()
    location1.recentlyAccessed = True

    location1.name = "pocket"
    location2.hasKey = False
    location2.recentlyAccessed = False

    location3.name = "office"
    location3.hasKey = False
    location3.recentlyAccessed = True


    #look for the keys
    if (location1.recentlyAccessed == True and location1.hasKey == True ):
        print("Found key in", location1.name)
    elif (location2.recentlyAccessed == True and location2.hasKey == True):
        print("Found key in", location2.name)
    elif (location3.recentlyAccessed == True and location3.hasKey == True):
        print("Found key in", location3.name)
    else:
         print("Ask spouse!")
     
    return 0

if __name__ == '__main__':
    sys.exit(main())

"""
     if (myVar <5):
         print("less than 5")
    else:
        print("greater than or equal to 5")
    return 0

main()
"""

"""
import sys

def main():
    class KeyLocation:
        
        def __init__(self):
            self.name = None
            self.hasKey = None


    location1 = KeyLocation()
    location2 = KeyLocation()
    location3 = KeyLocation()

    location1.name = "pocket"
    location2.hasKey = True

    location3.name = "office"
    location3.hasKey = False


    #look for the keys
    if (location1.hasKey == True):
        print("Found key in", location1.name)
    elif (location2.hasKey ==True):
        print("Found key in", location2.name)
    elif (location3.hasKey == True):
        print("Found key in", location3.name)
    else:
         print("Ask spouse!")
     
    return 0

if __name__ == '__main__':
    sys.exit(main())
    """

