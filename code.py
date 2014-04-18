import os, subprocess

def changeCharacters(fileRead):
    ins = open(fileRead, 'r', encoding='utf-8')

    changes = ''

    content = ''
    for line in ins:
        content += line

    text = ''
    for character in content:
        if character == chr(350):
            text += chr(536)
            changes += 'S '
        elif character == chr(351):
            text += chr(537)
            changes += 's '
        elif character == chr(354):
            text += chr(538)
            changes += 'T '
        elif character == chr(355):
            text += chr(539)
            changes += 'T '
        elif character == chr(173):
            text += chr(45)
            changes += '- '
        else:
            text += character
    #print (character)

    fileWrite = open(fileRead, 'w', encoding='utf-8')
    fileWrite.write(text)
    fileWrite.close()

    if (changes):
        print ('File modified: (' + changes[:-1] + ') ' + fileRead)
    else:
        print ('File: ' + fileRead)


def unzip(filename, path):
    temp = path + filename + ".temp/"
    subprocess.call(["unzip", path + filename, "-d", temp])
    changeCharacters(temp + "content.xml")
    subprocess.call(["pwd"])
    os.chdir(temp)
    subprocess.call(["pwd"])
    print(["zip", "-0", "-X", "../"+ filename + ".odt", "mimetype"])
    subprocess.call(["zip", "-0", "-X", "../"+ filename + ".odt", "mimetype"])
    print(["zip -r ../" + filename + ".zip * -x mimetype"])
    subprocess.call(["zip -r ../" + filename + ".odt * -x mimetype"], shell=True)


#path = './';
path = '/Users/z/Desktop/pyt/test/'

list = os.listdir(path)

for file in list:
    fileAddress = path + file
    unzip(file, path)

#break
#changeCharacters(path + file)


#./soffice --convert-to odt --outdir /Users/z/Desktop/pyt/test/ /Users/z/Desktop/pyt/test/*