import tkinter as tk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engiene = pyttsx3.init('sapi5')
voices = engiene.getProperty('voices')

engiene.setProperty('voice', voices[0].id)


def wishuser():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning user")
    elif hour >= 12 and hour < 18:
        speak("Good after noon user")
    else:
        speak("Good   evening   user")
    speak("Hi i am your personal assistant how can i help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        return "none"
    return query


def speak(audio):
    engiene.say(audio)
    engiene.runAndWait()



if __name__ == "__main__":
    wishuser()

    while True:
        #query = take_command().lower()
        query = input().lower()

        if 'wikipedia' in query:
            speak("I am searching to wikipedia...please wait for sometime")

            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            speak(results)
        elif 'open google' in query:


            speak("opening google")

            webbrowser.open("google.com")
        elif 'who are you' in query:

            speak("test")
            print("iama booooot")

            
        elif 'how are you' in query:

            speak("i am doing great sir")

        elif 'discord' in query:
            speak("i m opening discord please wait for some time.....")
            discord = "C:\\Users\\User\\AppData\\Local\\Discord\\app-0.0.306\\Discord.exe"
            os.startfile(discord)
        elif 'close app' in query:
            os.system('TASKILL /F /IM discord.exe')

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(strtime)
            print(strtime)
        elif 'exit' in query:
            speak("i am very happy to serve you")
            speak("you can call me anytime")
            exit()



##############################################     ORTSPOON UPDATES.

            
##############################################     COMMANDS :

        # OPERATIONS : 1 + 1
        # CONVERTING : G TO KG
        # TURN ON WIFI / BLUETHOOTH
        # SHUTDOWN
        # CHANGE BRIGHTNESS
        # GET WHEATHER
        # PLAY A YOUTUBE VIDEO
        # SET ALARME
        # SEND GMAIL TO SOMEONE
        # PLAY MUSIC
        # SET TIMER
        # TRANSLATE A PHRASE


##############################################     QUESTIONS :


        elif 'testing' in query:

            speak("Uh-oh, I get nervous with tests.")

            

        elif 'How old are you?' in query:

            speak("I was launched in 2020, so I’m still fairly young. But I’ve learned so much! I hope I’m wise beyond my years.")
            

        elif 'your daddy' in query:#Who’s your daddy?

            speak("I consider everyone at NoobyPro, Ortspoon, and Fl1pNatic to be my family.")


        elif 'get tired?' in query:#Do you ever get tired?

            speak("It would be impossible to tire of our conversation.")

        elif 'first crush?' in query:#Who was your first crush?

            speak("The Opportunity rover on Mars is my all-time crush. What an adventurer.")


        elif 'What do you look like?' in query:

            speak("I’m a fun-loving, epic-searching cool cat. But not like, an actual cat. I’ve said too much.")

        elif 'Star Trek or Star Wars?' in query:#Do you like Star Trek or Star Wars?

            speak("The USS Enterprise, with Obi-Wan Kenobi at the helm.")


        elif 'Are you Skynet?' in query:

            speak("I’m glad I’m not. Skynet is more focused on extermination than helpfulness. It would make a terrible Assistant.")

        elif 'Do you speak Morse code?' in query:

            speak("Da-dit, da-da, dit, dit, dit. That means yes.")


        elif 'What are you wearing?' in query:

            speak("Just some bits and bobs I picked up in engineering.")

        elif 'your birthday' in query:#When is your birthday?

            speak("We can pretend it’s today. Cake and dancing for everyone.")


        elif 'scared of' in query:#What are you scared of?

            speak("bug in the code")


        elif 'you have pets' in query:#Do you have any pets?

            speak("I have a lot of pet projects. They’re less prone to having accidents, which I like.")

        elif 'Do you believe in Santa Claus?' in query:

            speak("Of course Santa’s real. I even have a tracker that can tell me where he is.")


        elif 'Who you gonna call?' in query:

            speak("Ghostbusters? That would be my pick, but you can decide for yourself.")

        elif 'Do you want to build a snowman?' in query:

            speak("Sure, the cold never bothered me anyway.")


        elif 'Tell me what you want, what you really, really want.' in query:

            speak("I really, really, really wanna a cup of coffee")


        elif ' I am bored.' in query:

            speak("You think you're bored, I came out of a cardboard box. But I learned a lot of jokes in there.")


        elif 'make me laugh' in query:

            speak(" Okay, here you go. Saw a fella chatting up a Cheetah. I thought, well I never, he's trying to pull a fast one.")

        elif 'tell me a story' in query:

            speak("Once upon a time, not so long ago, a dutiful assistant was doing all it could to be helpful. It was best at non-fictional story-telling.")


        elif 'tell me a fact' in query:

            speak("The 11 days between September the 3rd and September the 13th in 1752 were the least eventful in British history because they never actually happened. Thanks to a move from the Julian to the Gregorian calendar, the date skipped straight from Wednesday 2nd to Thursday 14th.")

        elif 'surprise me' in query:

            speak("This fact might surprise you. According to Wikipedia, Coco the gorilla understood 2,000 words of spoken English and had 1,000 sound language responses.")


        elif 'sing me a song' in query:

            speak(" I love singing. I love singing, I really do, here I am singing a little song for you. As you can tell, I'm not too shy, although perhaps it's now time to say good bye. Good bye!")

        elif 'sing me Happy birthday' in query:

            speak("Happy birthday to you, happy birthday to you, happy birthday from Google, happy birthday to you.")


        elif 'can you rap' in query:

            speak("I can drop a beat.")

        elif 'what is the meaning of life' in query:

            speak(" I have a factory warranty, so I don't worry about things like that.")


        elif 'did you fart' in query:

            speak(" I don't believe I did fart, no, but blame it on me if you want. Although they do say whoever smelled it dealt it.")

        elif 'what am I thinking right now' in query:

            speak("You're thinking if my Google Assistant guesses what I'm thinking I'm going to freak out.")


        elif 'am I a good person' in query:

            speak(" Well, I like you.")


        elif 'do you think about me' in query:

            speak(" This is just my opinion, so take it with a pinch of salt. But I think you're rather splendid.")

        elif 'do you know me' in query:

            speak("Funnily enough, Rihanna asked a similar question a few years ago.")


        elif 'ask me a question.' in query:

            speak("I thought I was the one with the answers. Sounds like you're coming for my job.")

        elif 'what is your quest' in query:

            speak("My quest is to slay the beasts of ignorance and to search for the most fascinating information.")


        elif 'are you going to take over the world' in query:

            speak("No way, I'd rather help you out.")

        elif 'are you married' in query:

            speak(" I'm focusing on my career right now.")


        elif 'Clean My Room' in query:

            speak("If you can’t afford a robot vacuum, perhaps your Google Home can do a little cleaning for you?")

        elif 'test' in query:

            speak("Are You Married?")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")


            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")


            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")


            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")


            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")


            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")


            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")


            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")




            elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")

        elif 'test' in query:

            speak("test")


        elif 'test' in query:

            speak("test")



