# Speech to Text
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Please Say something")
    audio=r.listen(source)
    try:     
        cfs=r.recognize_google(audio)
        print("you said... "+cfs)
    except Exception as e:
        print ("Error :"+str(e))
