import os
import time
import pyaudio
import speech_recognition as sr
import playsound 
from gtts import gTTS
import openai


openai_api_key = 'YOUR KEY HERE'
elevenlabs_key = 'YOUR KEY HERE'

lang ='en'

openai.api_key = openai_api_key

from elevenlabs import generate, play, set_api_key,save

set_api_key("elevenlabs_key")

guy = ""

print("READY TO GO!!!!!!!!!!!!")

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global guy 
                guy = said
                

                if "Goku" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string) 
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":said}])
                    text = completion.choices[0].message.content
                    audio = generate(
                        text=text,
                        voice="Goku",
                        model='eleven_monolingual_v1'
                    )
                    save(audio,"output2.mp3")
                    # speech = gTTS(text = text, lang=lang, slow=False, tld="com.au")
                    # speech.save("welcome1.mp3")
                    # playsound.playsound("welcome1.mp3")
                    play(audio)
                    
            except Exception:
                print("Exception")


        return said

    if "stop" in guy:
        break


    get_audio()