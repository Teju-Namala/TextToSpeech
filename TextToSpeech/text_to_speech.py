from gtts import gTTS
import os 

fh=open("test.txt","r")
text=fh.read().replace("\n"," ")
lang='en'
op=gTTS(text=text,lang=lang,slow=False)
op.save("output.mp3")
fh.close()
os.system("start output.mp3")