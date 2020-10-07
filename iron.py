from win32com.client import Dispatch # pip install -m pip install pywin32
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install SpeechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser # pip install webbrowser
import os
import random
import smtplib # pip install smtplib
import pytz # pip install pytz
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes # pip install pyjokes
import sys
import pyaudio
import wolframalpha
import cv2 # pip install opencv-python
import pywhatkit as kit # pip install pywhatkit
from requests import get
import weathercom
import action as a

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def hello():
    speak('hello sir.. how are you ?')
    reply = takeCommand().lower()
    if 'fine' in reply :
        speak('ok! thats great!.. ')
    elif 'not good' in reply or 'not well' in reply or 'ill' in reply:
        speak('please take care sir.. and please have some rest..')
    speak('do u need anything from me.. ?')
    reply3 = takeCommand()
    if 'yes' in reply3 :
        speak('how can i help you ?')
    elif 'no' in reply3 :
        speak('ok sir.. no problem.. remind me.. if you need anything from me.. thank you..')
        sys.exit()
    else:
        speak ('sir  please tell me.. how may i help you?  ')

# to know the current time
def time():
    t_now = datetime.datetime.now().strftime('%I:%M:%S')
    speak("sir. the current time is")
    print(t_now)
    speak(t_now)
    speak('what should i do next sir?')

# to greet or welcome the user
def greet():
    t_hour = datetime.datetime.now().hour
    battery = psutil.sensors_battery()
    if 24 > t_hour < 4:
        speak("hello sir.. pleasant night sir!")
        if battery.percent < 20 :
            speak('sir! battery! is about to die! please charge the battery')   
        speak("thursday at your service sir")
        speak('command me! sir!')
    elif 4 <= t_hour < 12 :
        speak("hello sir! good morning.. have a nice day")
        if battery.percent < 20 :
            speak('sir! battery! is about to die! please charge the battery')
        speak("thursday at your service sir")
        speak('command me! sir!')
    elif 12 <= t_hour < 17 :
        speak("hello sir! good afternoon.. hope you are enjoying your day!")
        if battery.percent < 20 :
            speak('sir! battery! is about to die! please charge the battery')
        speak("thursday at your service sir")
        speak('command me! sir!')
    elif 17 <= t_hour < 19:
        speak('hello sir! good evening.. hope you were enjoyed your day!')
        if battery.percent < 20 :
            speak('sir! battery! is about to die! please charge the battery')
        speak("thursday at your service sir")
        speak('command me! sir!')
    else :
        speak('hello sir! good night.. hope you were enjoyed your day!')
        if battery.percent < 20 :
            speak('sir! battery! is about to die! please charge the battery')
        speak("thursday at your service sir")   
        speak('command me! sir!')

# to know the today's date
def date():
    t_date = datetime.datetime.now( tz = pytz.timezone('Asia/Kolkata'))
    speak('todays date is')
    print(t_date.strftime('%d %B, of %Y'))
    speak(t_date.strftime('%d %B, of %Y'))
    speak('Next Command! Sir!')

# to note the special content said by the user
def note():
    speak ('what should i note down ?')
    content = takeCommand()
    speak('okay')
    file = open("notes.txt",'w')
    speak('sir! should i include date and time ?')
    reply = takeCommand()
    if 'yes' in reply or 'sure' in reply or 'why not' in reply or 'yeah' in reply or 'ok' in reply or 'okay' in reply or 'please' in reply:
        speak('okay')
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        t_date = datetime.datetime.now( tz = pytz.timezone('Asia/Kolkata'))
        file.write('date : ')
        file.write(t_date.strftime('%d %B, of %Y'))
        file.write(f'\ntime : {strTime}')
        file.write(f'\nmain content : {content}')
        file.close()
        speak('sir! i have taken a note! please check it out!')
        speak('next command! sir!')   
    elif 'no' in reply or 'never' in reply or 'not now' in reply :
        speak('okay sir! no prblem!')
        file.write(f'\nmain content : {content}')
        speak('sir! i have taken a note! please check it out!')
        speak('next command! sir!')  
    else :
        speak("sorry sir! i do not understand your command! please tell me! should i include date and time ?")
        guru = takeCommand().lower()
        if 'yes' in guru or 'sure' in guru or 'why not' in guru or 'yeah' in guru or 'ok' in guru or 'okay' in guru or 'please' in guru:
            speak('okay')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            t_date = datetime.datetime.now( tz = pytz.timezone('Asia/Kolkata'))
            file.write('date : ')
            file.write(t_date.strftime('%d %B, of %Y'))
            file.write(f'\ntime : {strTime}')
            file.write(f'\nmain content : {content}')
            file.close()
            speak('sir! i have taken a note! please check it out!')
            speak('next command! sir!')
        elif 'no' in guru or 'never' in guru or 'not now' in guru :
            speak('okay sir! no prblem!')
            file.write(f'\nmain content : {content}')
            speak('sir! i have taken a note! please check it out!')
            speak('next command! sir!')  
        else :
            speak("sorry sir! i do not understand your command again! i am going to include date and time in notes for extra details")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            t_date = datetime.datetime.now( tz = pytz.timezone('Asia/Kolkata'))
            file.write('date : ')
            file.write(t_date.strftime('%d %B, of %Y'))
            file.write(f'\ntime : {strTime}')
            file.write(f'\nmain content : {content}')
            file.close()
            speak('sir! i have taken a note! please check it out!')
            speak('next command! sir!')
            
# to show the user's special content
def show_notes():
    speak('okay')
    file = open('notes.txt', 'r')
    speak('sir! i printed the notes! please check out!')
    n = file.read()
    print(n)
    speak("sir! May I read the notes?")
    reply = takeCommand().lower()
    if 'yes' in reply or 'sure' in reply or 'why not' in reply or 'yeah' in reply or 'please' in reply or 'ok' in reply or 'okay' in reply:
        speak(n)
        speak('next command! sir!') 
    elif 'no' in reply or 'never' in reply or 'not now' in reply:
        speak('okay sir! no problem!')
        speak('next command! sir!')          
    else :
        speak("sir! i do not understand your command! please tell me! may i read the notes ?")
        guru = takeCommand().lower()
        if 'yes' in guru or 'sure' in guru or 'why not' in guru or 'yeah' in guru or 'ok' in guru or 'okay' in guru:
            speak('okay')
            speak(n)
            speak('next command! sir!')
        elif 'no' in guru or 'never' in guru or 'not now' in guru :
            speak('okay sir! no problem!')
            speak('next command! sir!')   
        else :
            speak("sir! i do not understand your command again! i am not going to read the notes ")
            speak('next command! sir!')

# to get user required result on chrome 
def chrome():
    speak("what should i search ?")
    search = takeCommand().lower()
    speak('okay! searching! ')
    chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    webbrowser.get(chromepath).open_new_tab('www.google.com/#q='+search)
    speak('Next Command! Sir!')

# to get screenshot
def screenshot():
    speak('okay')
    img = pyautogui.screenshot()
    img.save('C:\\Users\\user\\Desktop\\jarvis\\screenshots\\ss.png')
    speak('i have taken screenshot')
    speak('Next Command! Sir!')
    
# to listen random jokes
def jokes():
    speak('okay i am telling a joke! ')
    my_joke = pyjokes.get_joke('en',category='neutral')
    print(my_joke)
    speak(my_joke)
    speak('Next Command! Sir!')
    
# to know the battery status    
def battery():
    battery = psutil.sensors_battery()
    print(battery.percent)
    speak(f'sir! battery! is at!{battery.percent} percent! ')
    if battery.percent < 20 :
        speak('sir! battery! is about to die! please charge the battery')
    speak('next command! sir!')
    
# to play user required video on youtube
def youtube():
    chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    speak('sir! what should i play on youtube!')
    reply = takeCommand().lower()
    if 'open youtube' in reply or 'launch youtube' in reply :
        speak('launching')
        webbrowser.get(chromepath).open_new_tab("www.youtube.com")
    else :
        speak(f'here we go to the {reply}')
        kit.playonyt(reply)
    speak('Next Command! Sir!')
        
# to get user required result on google  
def open_google():
    chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    speak('sir! what should i search on google!')
    reply = takeCommand().lower()
    if 'open google' in reply or 'open chrome' in reply :
        speak('launching')
        webbrowser.get(chromepath).open_new_tab("google.com")
    else :
        speak(f'sir! here is what i found for {reply}')
        webbrowser.get(chromepath).open_new_tab('www.google.com/#q='+reply)
    speak('Next Command! Sir!')
    
# shopping at amazon
def amazon():
    speak('sir! what should i search on amazon')
    reply = takeCommand().lower()
    if 'open amazon' in reply or'launch amazon' in reply:
        speak('launching..')
        webbrowser.open_new_tab('www.amazon.com')
    else :
        speak(f'sir! here is what i found for {reply}')
        webbrowser.open_new_tab(f'https://www.amazon.com/s?k={reply}&ref=nb_sb_noss_2')
    speak('Next Command! Sir!')

# shopping at flikart
def flipkart():
    speak('sir! what should i search on flipkart ')
    reply = takeCommand().lower()
    if 'open flipkart' in reply or'launch flipkart' in reply:
        speak('launching..')
        webbrowser.open_new_tab('www.flipkart.com')
    else :
        speak(f'sir! here is what i found for {reply}')
        webbrowser.open_new_tab(f'https://www.flipkart.com/search?q={reply}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
    speak('Next Command! Sir!')
    
# shopping at myntra
def myntra():
    speak('sir! what should i search on myntra')
    reply = takeCommand().lower()
    if 'open myntra' in reply or 'launch myntra' in reply:
        speak('launching..')
        webbrowser.open_new_tab('www.myntra.com')
    else :
        speak(f'sir! here is what i found for {reply}')
        webbrowser.open_new_tab(f'https://www.myntra.com/{reply}')
    speak('Next Command! Sir!')

#to search required result on stackoverflow.com
def stackoverflow():
    speak('sir! what should i search on stackoverflow')
    reply = takeCommand().lower()
    if 'open stack overflow' in reply or 'launch stack overflow' in reply:
        speak('launching..')
        webbrowser.open_new_tab('www.stackoverflow.com')
    else :
        speak(f'sir! here is what i found for {reply}')
        webbrowser.open_new_tab(f'https://stackoverflow.com/search?q={reply}')
    speak('Next Command! Sir!')
    
# just to open gmail
def open_gmail():
    speak('launching')
    webbrowser.open_new_tab('www.gmail.com')
    speak('Next Command! Sir!')
    
# for getting user's ip address
def my_ip():
    ip = get("https://api.ipify.org").text
    print(f"sir! your ip address is {ip}")
    speak(f"sir! your ip address is!{ip}")
    speak('Next Command! Sir!')
    
# to open facebook
def open_facebook():
    speak('launching')
    webbrowser.open_new_tab('www.facebook.com')
    speak('Next Command! Sir!')

# to open instagram
def open_instagram():
    speak('launching')
    webbrowser.open_new_tab('www.instagram.com')
    speak('Next Command! Sir!')
    
# to search required result on github.com
def github():
    speak('sir! what should i search on github')
    reply = takeCommand().lower()
    if 'open github' in reply or 'launch github' in reply:
        speak('launching..')
        webbrowser.open_new_tab('www.github.com')              
    else :
        speak(f'sir! here is what i found for {reply}')
        webbrowser.open_new_tab(f'https://github.com/search?q={reply}')
    speak('Next Command! Sir!')
        
# to know the location of user required place
def maps():
    speak('sir! which place should i search on maps')
    reply = takeCommand().lower()
    if 'open maps' in reply or 'open google map' in reply or 'launch google map' in reply or 'launch maps' in reply or 'open google maps' in reply or 'launch google maps' in reply or 'open map' in reply or 'launch map' in reply :
        speak('launching..')
        webbrowser.open_new_tab('https://www.google.nl/maps')                
    else :
        speak(f'sir! here is what i found for {reply}')
        speak('sir! sometimes right results cannot be given due to wrong pronunciation!s')
        webbrowser.open_new_tab(f'https://www.google.nl/maps/place/{reply}/&amp;')
        speak('sir! if you are not getting the right result! please search out place whichever you want on map! I have opened google map for you')
    speak('Next Command! Sir!')
    
# to shutdown user's system
def shut_down():
    speak('sir! do u really want to shutdown ?')
    reply = takeCommand()
    if 'yes' in reply or 'sure' in reply or 'ok' in reply or 'okay' in reply:
        speak('okay')
        speak(' bye sir.. i am shutting down the system.. take care sir.. thank you..')
        os.system('shutdown /s /t 1')
    elif 'no' in reply or 'not now' in reply or'never' in reply:
        speak('ok sir! no problem. please proceed ur work')
        speak('tell me sir! what can i do for u next?  ')
    else :
        speak('sorry sir! i do not understand your command!')
        speak('please tell me.. may i shutdown the system!')
        shut = takeCommand().lower()
        if 'yes' in shut or 'sure' in shut or 'ok' in shut or 'okay' in shut:
            speak('okay')
            speak(' bye sir.. i am shutting down the system.. take care sir.. thank you..')
            os.system('shutdown /s /t 1')
        elif 'no' in shut or 'not now' in shut or'never' in shut:
            speak('ok sir! no problem. please proceed ur work')
            speak('tell me sir! what can i do for u next?  ')
        else :
            speak('sorry sir! i do not understand your command again')
            speak(' i am not going to shutdown the system!')
            speak('next command! sir!')
    
    
# to restart user's system
def re_start():
    speak('sir! do u really want to restart ?')
    reply = takeCommand()
    if 'yes' in reply or 'sure' in reply or 'ok' in reply or 'okay' in reply:
        speak('okay')
        speak(' bye sir.. i am restarting the system.. take care sir.. thank you..')
        os.system('shutdown /r /t 1')
    elif 'no' in reply or 'not now' in reply or'never' in reply:
        speak('ok sir! no problem. please proceed ur work')
        speak('tell me sir! what can i do for u next?  ')
    else :
        speak('sorry sir! i do not understand your command!')
        speak('please tell me.. may i restart the system!')
        shut = takeCommand().lower()
        if 'yes' in shut or 'sure' in shut or 'ok' in shut or 'okay' in shut:
            speak('okay')
            speak('sir.. i am restarting down the system.. take care sir.. thank you..')
            os.system('shutdown /r /t 1')
        elif 'no' in shut or 'not now' in shut or'never' in shut:
            speak('ok sir! no problem. please proceed ur work')
            speak('tell me sir! what can i do for u next?  ')
        else :
            speak('sorry sir! i do not understand your command again')
            speak(' i am not going to restarting the system!')
            speak('next command! sir!')
            
# to get user's result according to google
def according_to_google():
    speak('searching! ')
    chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    speak(f'sir! here is what i found out on google')
    webbrowser.get(chromepath).open_new_tab('www.google.com/#q='+query.replace('according to google',''))
    speak('Next Command! Sir!')
    
# to get user's result according to chrome
def according_to_chrome():
    speak('searching! ')
    chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    speak(f'sir! here is what i found out on chrome')
    webbrowser.get(chromepath).open_new_tab('www.google.com/#q='+query.replace('according to chrome',''))
    speak('Next Command! Sir!')
    
# to get user's result according to wikipedia
def according_to_wikipedia():
    speak('searching! ')
    chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    result = wikipedia.summary(query.replace('according to wikipedia',''), sentences=2)
    speak('sir! wikipedia says!')
    print(result)
    speak(result)
    webbrowser.get(chromepath).open_new_tab(f"https://en.wikipedia.org/wiki/{query.replace('according to wikipedia','')}")
    speak(f'sir! i also opened required result on wikipedia! if you want to get some extra detais! please check out there!')
    speak('Next Command! Sir!')
    
def how_are_you():
    stMsgs = ['Just doing my thing sir..!  ', 'I am fine and full of energy!', 'I am nice and full of energy']
    speak(random.choice(stMsgs))
    speak(' how are you? ')
    reply = takeCommand()
    if 'fine' in reply :
        speak('ok! thats great! ')
        speak('sir! please tell me how can i help you! ')
    elif 'not good' in reply or 'not well' in reply or 'ill' in reply:
        speak('please take care sir.. and please have some rest..')
        speak('sir! please tell me how can i help you! ')
        
def who_are_you():
    speak('hello sir! i am thursday! your personal assistant! i am here to make your life easier! you can command me to perform various tasks!')
    speak('sir! do u need anything from me.. ?')
    reply3 = takeCommand()
    if 'yes' in reply3 :
        speak('how can i help you ?')
    elif 'no' in reply3 :
        speak('ok sir.. no problem.. remind me.. if you need anything from me.. thank you  ')
        sys.exit()
    else:
        speak ('sir  please tell me.. how may i help you?  ')
        
# to open notepad
def open_notepad():
    speak('launching..')
    f_path = "C:\\windows\\system32\\notepad.exe"
    os.startfile(f_path)
    speak('Next Command! Sir!')

# to open downloads folder
def open_downloads():
    speak('launching..')
    d_path = "D:\\Downloads"
    os.startfile(d_path)
    speak('Next Command! Sir!')
    
# to open music folder
def open_music():
    speak('launching..')
    m_path = "D:\\Music"
    os.startfile(m_path)
    speak('Next Command! Sir!')
    
# to play music
def play_music():
    speak('playing..')
    music_dir = "D:\\Music"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    s = os.path.join(music_dir, rd)
    os.startfile(s)
    speak('Next Command! Sir!')
    
# to open documents
def open_documents():
    speak('launching..')
    m_path = "D:\\Documents"
    os.startfile(m_path)
    speak('Next Command! Sir!')

# to open pictures
def open_pictures():
    speak('launching..')
    p_path = "C:\\Users\\user\\OneDrive\\Pictures"
    os.startfile(p_path)
    speak('Next Command! Sir!')
    
# to open videos
def open_videos():
    speak('launching..')
    v_path = "D:\\Videos"
    os.startfile(v_path)
    speak('Next Command! Sir!')
    
# to open favourite items
def open_favourites():
    speak('launching..')
    v_path = "D:\\Favorites"
    os.startfile(v_path)
    speak('Next Command! Sir!')
    
# to select and play movies
def play_movies():
    speak('sir! What language would you like to watch?')
    speak('english hollywood!  hindi bollywood! marathi mollywood! or!  tamil  tollywood!')
    reply = takeCommand().lower()
    if 'english' in reply or 'hollywood' in reply :
        speak('launching..')
        m_path = "D:\\movies\\hollywood"
        os.startfile(m_path)
        speak('sir! i have opened the folder! please select and play movie whichever you want! ')
        speak('Next Command! Sir!')
    elif 'hindi' in reply or 'bollywood' in reply :
        speak('launching..')
        m_path = "D:\\movies\\bollywood"
        os.startfile(m_path)
        speak('sir! i have opened the folder! please select and play movie whichever you want! ')
        speak('Next Command! Sir!') 
    elif 'south' in reply or 'tamil' in reply or 'tollywood' in reply :
        speak('launching..')
        m_path = "D:\\movies\\tollywood"
        os.startfile(m_path)
        speak('sir! i have opened the folder! please select and play movie whichever you want! ')
        speak('Next Command! Sir!')
    elif 'marathi' in reply or 'mollywood' in reply :
        speak('launching..')
        m_path = "D:\\movies\\marathi"
        os.startfile(m_path)
        speak('sir! i have opened the folder! please select and play movie whichever you want! ')
        speak('Next Command! Sir!')
    else :
        speak('sorry sir! we dont have movies like this! ')
        m_path = "D:\\movies"
        os.startfile(m_path)
        speak('sir! i have opened the movies folder! please select and play movie whichever you want to watch!')
        speak('Next Command! Sir!')
        
# to open virtual box
def virtualbox():
    speak('launching virtual box!..')
    v_path = "D:\\virtual box\\VirtualBox.exe"
    os.startfile(v_path)
    speak('Next Command! Sir!')
    
# to open visual studio
def visual_studio():
    speak('launching..')
    f_path = "D:\\Microsoft VS Code\\Code.exe"
    os.startfile(f_path)
    speak('Next Command! Sir!')
    
# to open command prompt
def cmd():
    speak('launching..')
    os.system('start')
    speak('Next Command! Sir!')
    
# to open ms word
def word():
    speak('launching..')
    f_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
    os.startfile(f_path)
    speak('Next Command! Sir!')
    
# to open powerpoint
def powerpoint():
    speak('launching..')
    f_path = "C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
    os.startfile('PowerPoint')
    speak('Next Command! Sir!')
    
# to open ms wordpad
def wordpad():
    speak('launching..')
    os.startfile('wordpad')
    speak('Next Command! Sir!')
    
# to open webcam
def open_camera():
    speak('launching..')
    cap = cv2.VideoCapture(0)
    speak('sir! hit enter key! to get out of the webcam!..')
    while True :
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        if cv2.waitKey(1) == 13:
            break
    cap.release()
    cv2.destroyAllWindows()
    speak('Next Command! Sir!')
    
# to open calculator
def open_calci():
    speak('launching..')
    os.system('calc')
    speak('Next Command! Sir!')
    
# to open control panel
def control_panel():
    speak('launching..')
    os.system('c:\Windows\System32\control')
    speak('Next Command! Sir!')

# to get input from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        return "None"
    return query

if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()
        
        if 'open youtube' in query or 'launch youtube' in query or 'search on youtube' in query or 'start youtube' in query:
            youtube()
            
        elif 'open google' in query or 'launch google' in query or 'launch chrome' in query or 'open chrome' in query or 'start google' in query or 'google search' in query or 'chrome search' in query or 'search on google' in query or 'search on chrome' in query:
            open_google()
            
        elif 'open gmail' in query or 'launch gmail' in query or 'start gmail' in query:
            open_gmail()
                
        elif 'open facebook' in query or 'launch facebook' in query or 'start facebook' in query:
            open_facebook()
            
        elif 'open instagram' in query or 'launch instagram' in query or 'start instagram' in query:
            open_instagram()
                
        elif 'open amazon' in query or 'launch amazon' in query or 'search on amazon' in query or 'start amazon' in query:
            amazon()
                
        elif 'open flipkart' in query or 'launch flipkart' in query or 'search on flipkart' in query or 'start flipkart' in query:
            flipkart()
                
        elif 'open myntra' in query or 'launch myntra' in query or 'search on myntra' in query or 'start myntra' in query:
            myntra()
            
        elif 'open stack overflow' in query or 'launch stack overflow' in query or 'search stack overflow' in query or 'start satck overflow' in query:
            stackoverflow()
               
        elif 'open github' in query or 'launch github' in query or 'search on github' in query:
            github()
                
        elif 'open maps' in query or 'open google map' in query or 'launch google map' in query or 'launch maps' in query or 'open google maps' in query or 'launch google maps' in query or 'open map' in query or 'launch map' in query or 'search on map' in query or 'search on google map' in query or 'search on google maps' in query or 'search on maps' in query:
            maps()
        
        elif 'time' in query:
            time() 
            
        elif 'date' in query :
            date()
        
        elif 'shutdown' in query :
            shut_down()
                
        elif 'restart' in query :
            re_start()
                
        elif 'joke' in query:
            jokes()
            
        elif 'according to google' in query :
            according_to_google()
            
        elif 'according to chrome' in query :
            according_to_chrome()
            
        elif 'according to wikipedia' in query:
            according_to_wikipedia()
            
        elif 'exit' in query or 'quit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'no thanks' in query or 'no commands' in query or 'no commands' in query or 'offline' in query:
            speak('bye sir. have a good day! thank you..')
            break
            
        elif 'hello' in query or 'hi' in query or 'hey' in query:
            hello()
            
        elif 'thank you' in query or 'thanks' in query :
            speak('no problem sir! I am just doing my job!')
            speak('Next Command! Sir!')
            
        elif 'note down something' in query or 'take a note' in query or 'write a note' in query :
            note()

        elif 'how are you' in query:
            how_are_you()
            
        elif 'who are you' in query :
            who_are_you()

        elif 'take screenshot' in query :
            screenshot()
               
        elif 'open notepad' in query or 'launch notepad' in query:
            open_notepad()
               
        elif 'open downloads' in query or 'open downloads folder' in query :
            open_downloads()
               
        elif 'open music' in query or 'open music folder' in query or 'music files' in query or 'open songs' in query or 'song list' in query or 'music list' in query:
            open_music()
               
        elif 'play music' in query or 'play songs' in query :
            play_music()
                
        elif 'open documents' in query or 'open document folder' in query or 'open documents folder' in query :
            open_documents()
             
        elif 'open pictures' in query or 'pictures folder' in query or 'open photos' in query or 'photos folder' in query:
            open_pictures()
               
        elif 'open videos' in query or 'videos folder' in query:
            open_videos()
             
        elif 'open favorites' in query or 'open favorites folder' in query:
            open_favourites()
              
        elif 'open movies' in query or 'movies folder' in query or 'play movies' in query:
            play_movies()
                   
        elif 'open virtualbox' in query or 'launch virtualbox' in query :
            virtualbox()
               
        elif 'visual studio' in query or 'open vs code' in query :
            visual_studio()
               
        elif 'open command prompt' in query or 'open cmd' in query or 'launch command prompt' in query or 'launch cmd' in query or 'open terminal' in query or 'launch terminal' in query:
            cmd()
              
        elif 'open microsoft word' in query or 'launch microsoft word' in query or 'launch ms word' in query or 'word document' in query or 'open ms word' in query:
            word()
           
        elif 'open wordpad' in query or 'open microsoft wordpad' in query or 'launch wordpad' in query or 'launch microsoft wordpad' in query or 'open ms wordpad' in query or 'launch ms wordpad' in query:
            wordpad()
            
        elif 'open powerpoint' in query or 'open microsoft powerpoint' in query or 'launch powerpoint' in query or 'launch microsoft powerpoint' in query or 'open ms powerpoint' in query or 'launch ms powerpoint' in query or 'make presentation' in query or 'create presentation' in query or 'new presentation' in query or 'open presentation' in query:
            powerpoint()
              
        elif 'open camera' in query or 'open webcam' in query or 'launch camera' in query or 'launch webcam' in query :
            open_camera()
          
        elif 'my ip' in query or 'my internet protocol' in query :
            my_ip()
                    
        elif 'open calculator' in query or 'launch calculator' in query or 'open calci' in query or 'launch calci' in query:
            open_calci()
             
        elif 'open control panel' in query or 'launch control panel' in query:
            control_panel()
            
        elif 'your name' in query:
            speak('sir! call me thursday!')
            speak('sir! tell me how may i help you!')
            
        elif 'ok' in query or 'okay' in query:
            speak('please continue! sir!')
               
        elif 'battery' in query:
            battery()
            
        elif 'my note' in query or 'my notes' in query or 'show notes' in query or 'show note' in query or 'show my notes' in query or 'shiw my note' in query:
            show_notes()
         
        else:
            
            speak('sorry sir! i do not get your command !')
            speak('pardon! sir!')

