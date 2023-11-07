with open("/tmp/cars.txt", "w+") as exFile:
    for x in range(50):
        print("There are %d cars" % (x))
with open("/tmp/cars.txt", "r") as exFile:
    filecontents = exFile.read()
    print(filecontents)