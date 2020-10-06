
def checkLast(url, website):
    latestPropertyFile = openFileRead()

    content = latestPropertyFile.readlines()
    counter = 0
    found = False

    for line in content:
        if website in line:
            if url in line:
                found = True
                break
            else:
                print("not found")
                #updateLast(url, content, latestPropertyFile, counter)

        counter += 1

    closeFile(latestPropertyFile)
    return found


def updateLast(url, website):
    fileRead = openFileRead()

    newFile = []

    for line in fileRead:
        if line.__contains__(website):
            oldURL = line.split(": ")[1]
            newFile.append(line.replace(oldURL, url))
        else:
            newFile.append(line)

        newFile.append("\n")

    fileRead.close()
    fileWrite = openFileWrite()

    print(newFile)

    for line in newFile:
        fileWrite.write(line)

    closeFile(fileWrite)

def openFileRead():
    file = open("latest_recorded_property.txt", "r+")
    return file

def openFileWrite():
    file = open("latest_recorded_property.txt", "w+")
    return file

def closeFile(file):
    file.close()
