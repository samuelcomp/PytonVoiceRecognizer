import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something this is Sami !!!')
    audio = r.listen(source)
    print ('Done!!!')
    
text = r.recognize_google(audio)
print (text)