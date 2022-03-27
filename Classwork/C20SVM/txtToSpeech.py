import os as OS
from gtts import gTTS
from bs4 import BeautifulSoup as BS

def removeTags(html) -> str :
    soup = BS(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
    return ' '.join( soup.stripped_strings )

def writeFile(path, data, mode='w') -> None:
    sanitizedFile = open( path, mode )
    sanitizedFile.write( data )
    sanitizedFile.close()
    return sanitizedFile

def main() -> None:
    path = 'E:\\articles'
    fileName = '2022-03-26-18-trading-rules-by-martin-pring-to-beat-market-fetch-big-returns.txt'

    with open(
        f'{path}\\{fileName}'
        , 'r'
    ) as myFile:
        #myText = 'Welcome to my program'
        myText = myFile.read()
        sanetizedText = removeTags( myText )
        #print("FileText : ", myText)
        writeFile(f'{path}\\sanitized\\{fileName}', sanetizedText, 'w')

        language = 'en'
        TTS : gTTS = gTTS( text = sanetizedText, lang = language, slow = False )
        TTS.save( f'{path}\\audio\\{fileName}.mp3' )

        OS.system(f'start {path}\\audio\\{fileName}.mp3')
        myFile.close()

if __name__ == '__main__':
    main()

