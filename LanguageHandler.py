import speech_recognition as sr
from random import randint


def getInput(id):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ja-JP')
        #print("Google Speech Recognition thinks you said " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Array of (int) Identities


def selectClipFromSet(questionSet):
    ident = questionSet[randint(0, len(questionSet) - 1)]
    return str(ident) + ".wav", ident


def selectRandomClip(IdLow, IdHigh):
    ident = randint(IdLow, IdHigh)
    return str(ident) + ".wav", ident


