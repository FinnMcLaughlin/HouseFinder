
def checkLast(url, website):
    latestPropertyFile = openFile()

    content = latestPropertyFile.readlines()

    for line in content:
        if website in line:
            if url in line:
                break
            else:
                break
                #updateLast(url, website, line, latestPropertyFile)

    closeFile(latestPropertyFile)


def updateLast(url, website, content, file):
    return 0
    #oldURL = content.split(": ")[1]
    #print(oldURL)
    #print(url)
    #updatedFile = content.replace(oldURL, url)
    #print(updatedFile)
    #file.write(updatedFile)


def openFile():
    file = open("latest_recorded_property.txt", "r+")
    return file

def closeFile(file):
    file.close()
