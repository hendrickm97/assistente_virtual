import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


def listening():
    rec = sr.Recognizer()

    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Fale Alguma Coisa...")
        audio = rec.listen(mic)

        try:
            frase = rec.recognize_google(audio, language="pt-BR")
            print(frase)

        except Exception as e:
            print(e)
            print("Por favor fale novamente")
            return "None"

    return frase


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()


def date():
    day = datetime.datetime.today().weekday() + 1

    day_dict = {1: 'Segunda-Feira', 2: 'Terça-Feira',
                3: 'Quarta-Feira', 4: 'Quinta-Feira',
                5: 'Sexta-Feira', 6: 'Sábado',
                7: 'Domingo'}

    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(f"O dia de hoje é {day_of_the_week}")
        speak(f"O dia de hoje é {day_of_the_week}")

    return day


def tempo():
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    minute = time[14:16]
    speak(f"Agora São {hour} horas e {minute} minutos")
    print(f"Agora São {hour} horas e {minute} minutos")

    return time


def comando_voz():
    while True:
        tarefa = listening().lower()
        if "abra o google" in tarefa:
            speak("Abrindo Google")
            print("Abrindo Google")
            webbrowser.open("www.google.com")
            continue
        elif "qual o dia de hoje" in tarefa:
            date()
            continue
        elif "me diga as horas" in tarefa:
            tempo()
            continue
        elif "desligar" in tarefa:
            speak("Alfa desligando")
            print("Alfa desligando")
            exit()


def comando_escrito():
    while True:
        tarefa = input("Comandos : 'abra o google', 'qual o dia de hoje', 'me diga as horas', 'desligar'").lower()
        if "abra o google" in tarefa:
            speak("Abrindo Google")
            print("Abrindo Google")
            webbrowser.open("www.google.com")
            continue
        elif "qual o dia de hoje" in tarefa:
            date()
            continue
        elif "me diga as horas" in tarefa:
            tempo()
            continue
        elif "desligar" in tarefa:
            speak("Alfa desligando")
            print("Alfa desligando")
            exit()


if __name__ == '__main__':
    speak("Olá eu sou Alfa sua assistente virtual,"
          "No que posso te ajudar?(escreva: 'falar' ou 'digitar')")
    answer = input("Olá eu sou Alfa sua assistente virtual,"
                   "No que posso te ajudar?(escreva: 'falar' ou 'digitar')").lower()

    if answer == "falar":
        comando_voz()
    elif answer == "digitar":
        comando_escrito()
