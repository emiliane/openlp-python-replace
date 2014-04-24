import os, subprocess
import xml.etree.ElementTree as ET

ET.register_namespace('', 'http://openlyrics.info/namespace/2009/song')

def authorNumberFive(string, filename):
    parts = string.split('authors', 3)

    authors = parts[1].split('<author>1</author>', 2)

    authorNumber = '0'
    try:
        authorNumber = authors[1].split('<')[1].split('>')[1]
    except:
        print ('Introduceti manual numarul: \n')
        print (filename + "\n")
        authorNumber = input()

    result = parts[0] + 'authors>\n      <author>' + authorNumber + '</author>\n    </authors' + parts[2]

    return result

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

def changeCharacters2(fileRead):
    ins = open(fileRead, 'r', encoding='utf-8')

    lyrics = ''
    for line in ins:
        lyrics += line

    lyrics = re.sub('\.{3,}', "…", lyrics)

    punctuation_mark = [".", ",", ";", ":", "!", "?", "…"]
    for punctuation in punctuation_mark:
        lyrics = lyrics.replace(punctuation, punctuation + " ")

    lyrics = lyrics.replace("\t", " ")
    lyrics = re.sub(' {2,}', " ", lyrics)

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
    
def addSongBookAndNumber(songXML):
    root = ET.fromstring(songXML)
    numberOfSongBook = list(root.iter('{http://openlyrics.info/namespace/2009/song}songbook'))[0].get('entry')

    for child in root.iter('{http://openlyrics.info/namespace/2009/song}title'):
        child.text = child.text + ' ' + numberOfSongBook
        print('Title edited: ' + child.text)

    a = ET.tostring(root, encoding='utf-8', method='xml')
    return a.decode('utf-8')


#path = './';
path = '/Users/z/Desktop/pyt/test/'

list = os.listdir(path)

for file in list:
    fileAddress = path + file
    unzip(file, path)

#break
#changeCharacters(path + file)


#./soffice --convert-to odt --outdir /Users/z/Desktop/pyt/test/ /Users/z/Desktop/pyt/test/*