import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar micrófono y devolver audio como texto

def transformar_audio_en_texto():
    # Almacenar recognicer en variable
    r= sr.Recognizer()
    #Configurar el micrófono
    with sr.Microphone(device_index=1) as origen:
        #tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzó
        print('ya puedes hablar')

        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r. recognize_google(audio, lenguage="es-es")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # Devolver a pedido
            return pedido
        # En caso de que no comprenda
        except sr.UnknownValueError:
            # prueba de que no comprendió el audio
            print('Ups, no entendí')

            # Devolver error
            return 'Sigo esperando'

        # En caso de no resolver el pedido

        except sr.RequestError:
            # prueba de que no comprendió el audio
            print('Ups, no hay servicio')

            # Devolver error
            return 'Sigo esperando'
        # error inesperado
        except:
            # prueba de que no comprendió el audio
            print('Ups, algo salió mal')

            # Devolver error
            return 'Sigo esperando'

transformar_audio_en_texto()
