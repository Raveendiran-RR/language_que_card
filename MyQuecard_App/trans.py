from googletrans import Translator
from gtts import gTTS
import os ,time

def calltrans():
    # portion to convert from englist to kannada
    translator=Translator()
    blabber= ("always me")
    translation=translator.translate(blabber,src='en',dest='kn')
    #print(translation.origin,'->',translation.text)
    translated_output=''
    translated_output= translation.text
    print(translated_output)

    #TranslatedText= translation.text
    language="kn"
    output=gTTS(text=translated_output,lang=language,slow=True)
    #os.system("powershell kill -name 'wmplayer'")
    prefix= time.strftime("%Y%m%d-%H%M%S")
    output.save('static/audio/output.mp3')
    
    #os.system("start output.mp3")
