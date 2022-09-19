import os
import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

preguntas = [
    'Hay cuatro pares de frutas del diablo y sus propietarios a continuación. ¿Qué par es incorrecto?',
    '“Cicatriz con forma de rayo”, “criatura”, y “sandalias tradicionales japonesas”. ¿A qué personaje se refiere esta descripción?',
    'Verdadero o falso: La tripulación de Barbablanca tiene 15 divisiones, todas ellas con su propio Comandante.',
    'Verdadero o falso: el antiguo Almirante de la Armada Sengoku the Buddha posee Haoshoku Haki, Busoshoku Haki, y Kenbunshoku Haki.',
    '¿Qué estilo de natación utiliza Yokozuna?',
    '¿Cuántos "Siete Guerreros del Mar" han habido (incluyendo los personajes que ya no tienen el título)?',
    '“Espada maldita”, “valor de más de un millón de Bellys”, y “tienda de armas en Loguetown”。¿A qué espada se refiere esta descripción?',
    '¿Cuál de las habitaciones y características de abajo hizo el Going Merryno tenía?',
    'Verdadero or Falso: Reiju Vinsmoke es la hermana menor de Sanji Vinsmoke.',
    'Verdadero o Falso: La Fruta Fuego Fuego y la Fruta Temblor Temblor tienen más de un usuario.',
    '¿Cuál de los siguientes personajes no es un capitán de la “Gran Flota de Sombrero de Paja”?',
    '¿Qué edad tenían Shanks y Buggy cuando se convirtieron en aprendices de la tripulación de los Piratas de Roger?',
    '¿Cuál de los siguientes personajes no puede usar Haoshoku Haki?',
    '¿Cuál de los siguientes personajes no es un miembro del Ejército Revolucionario?',
    '¿Cuál de los siguientes personajes no es un maestro de una de las Doce Espadas de Grado Supremo?',
    '¿Dónde vivió Silvers Rayleigh tras la disolución de los Piratas de Roger?',
    'Hay cuatro órdenes de recompensas por personaje de la más alta a la más baja de bajo. ¿Cuál es el orden correcto?',
    '¿Cuál de las Frutas del Diablo de abajo no está en el manga original?',
    '¿Cuál de los siguientes personajes no aparece en el Reino de Arabasta?',
    '¿Qué nivel de Impel Down (Gran Prisión Submarina) está nombrada incorrectamente?'
]

choices = [
    [
        'a) Yuki Yuki no Mi(Fruta Nieve Nieve) y Monet',
        'b) Kame Kame no Mi (Fruta Tortuga) y Pekoms',
        'c) Fude Fude no Mi y Kurozumi Kanjuro',
        'd) Bata Bata no Mi (Fruta mantequilla) y Charlote Opera',
        'x) Secret option', 'd'
    ], ['a) Jinbe', 'b) Urouge', 'c) Enel', 'd) Sr. Ceaser Clown', 'a'],
    ['Verdadero', 'Falso', 'f'], ['Verdadero', 'Falso', 'v'],
    ['a) Brazada de pecho', 'b) Crol', 'c) Perrito', 'd) Estilo libre', 'd'],
    ['a) 9', 'b) 10', 'c) 11', 'd) 12', 'c'],
    ['a) Shusui', 'b) Yubashi', 'c) Sandai Kitetsu', 'd) Wado Ichimonji', 'c'],
    [
        'a) Jardin de naranjos', 'b) Sala de lectura',
        'c) El asiento Favorito de Luffy', 'd) Sala de reuniones (y Timón)',
        'b'
    ], ['Verdadero', 'Falso', 'f'], ['Verdadero', 'Falso', 'v'],
    ['a) Hajrudin', 'b) Gambia', 'c) Cavendish', 'd) Bartolomeo', 'b'],
    ['a) 8', 'b) 9', 'c) 10', 'd) 11', 'b'],
    ['a) Yamato', 'b) Boa Hancock', 'c) Eustass Kid', 'd) Nico Robin', 'd'],
    ['a) Tsuru', 'b) Sabo', 'c) Ahiru', 'd) Emporio Ivankov', 'a'],
    [
        'a) Gol D. Roger', 'b) Edward Newgate', 'c) Roronoa Zoro',
        'd) Dracule Mihawk', 'c'
    ],
    [
        'a) Isla de Drum ', 'b) Isla Judicial', 'c) Long Ring Long Land',
        'd) Archipielago Sabaody', 'd'
    ],
    [
        'a) Charlotte LinLin > Kaido > Shanks > Marshall D. Teach',
        'b) Charlotte LinLin > Kaido > Marshall D. Teach > Shanks',
        'c) Kaido > Charlotte LinLin > Shanks > Marshall D. Teach',
        'd) Kaido > Marshall D. Teach > Charlotte LinLin > Shanks', 'c'
    ],
    [
        'a) Kobu Kobu no Mi (Fruta Ánimo Ánimo)',
        'b) Baku Baky no Mi (Fruta Come Come)',
        'c) Fuku Fuku no Mi (Fruta Vestir Vestir)',
        'd) Hiso Hiso no Mi (Fruta Susurro Susurro)', 'd'
    ],
    [
        'a) Igaram', 'b) Kozuki Momonosuke', 'c) Crocodile',
        'd) Nefertari Vivi', 'b'
    ],
    [
        'a) Nivel 2 - El infierno Carmesí',
        'b) Nivel 3 - El infierno de la Hambruna',
        'c) Nivel 5 - El infierno Helado', 'd) Nivel 5.5 - Newkama Land', 'a'
    ]
]

pregunta_extras = [
    '¿Cuántos años le dieron a Tom para construir el tren marino de Water 7?',
    '¿Cómo se llama la Isla en donde se encuentra el castillo de Mihawk?',
    '¿Cuál es el nombre de la fruta de Caribou?'
]

respuestas_extras = [['a) 5 Años', 'b) 1 Año', 'c) 10 Años', 'd) 7 Años', 'c'],
                     [
                         'a) Isla namakura', 'b) Isla Kuraigara',
                         'c) Isla Raijin', 'd) Isla Kambaka', 'b'
                     ],
                     [
                         'a) Poru Poru no mi', 'b) Numa Numa no mi',
                         'c) Boru Boru no mi', 'd) Nagi Nagi no mi', 'b'
                     ]]


def avg_nakama(scores):
    prom = sum(scores) / len(scores)
    if prom < 50:
        print(RED +
              'uy! nakama tienes que leer el manga y ver el anime urgente!!!')
    elif prom < 100:
        print(CYAN + 'Nada mal nakama, pero echale una ojeadita al manga' + RESET)
    elif prom < 150:
        print(YELLOW + 'Muy bien!, eres un buen candidato para ser el Rey de los Piratas.' +
              RESET)
    else:
        print(GREEN + 'Eres un verdadero Nakama ' + nombre +
              ' que tengas un buen viaje y encuentres el ONE PIECE')


puntaje = random.randint(3, 12)
play = True
print(CYAN + '-=BIENVENIDO NAKAMA=-' + RESET)
time.sleep(0.8)
nombre = input(CYAN + 'Cual es tu nombre?\n' + RESET)
index = 0
scores = []
while play:

    print('\nGenial ' + str(nombre) + "!")
    print(CYAN + 'Vamos a ver que tan fan de ONE P' + RESET + '' + RED + 'I' +
          RESET + '' + CYAN + 'ECE eres te parece?' + RESET)
    print(GREEN + 'Estas listo para empezar la trivia?' + RESET)
    ready = input(YELLOW + 'Escriba "S" Para Sí o "N" para No : \n' + RESET)
    while ready not in ['S', 's']:
        ready = input(
            YELLOW +
            'Ok nakama sin apuros tomate tu tiempo, cuando estes listo digita "S" : '
            + RESET)

    print('\nListo! Empecemos :D')
    print('Intento N°' + str(len(scores) + 1))
    time.sleep(0.9)
    print('\nComenzarás con un puntaje de :' + GREEN+str(puntaje)+RESET)
    time.sleep(0.8)
    print('Recuerda que cada pregunta incorrecta te resta unos puntitos')
    time.sleep(0.8)
    print('Mucha Suerte Nakama!\n\n')
    for i in range(0, 4):
        time.sleep(1)

    for pregunta in range(0, len(preguntas)):
        time.sleep(0.5)
        print(YELLOW + "" + str(pregunta + 1) + ".) " + preguntas[pregunta] +
              RESET)
        time.sleep(0.9)
        if len(choices[pregunta]) - 1 == 2:
            for choice in range(len(choices[pregunta]) - 1):
                print(GREEN + choices[pregunta][choice] + RESET)
                

            print('esta pregunta es de 2 opciones')
            respuesta = input('Escriba "V" para verdadero o "F" para Falso: ')
            while respuesta.lower() not in ['v', 'f']:
                respuesta = input(
                    'Por favor ingrese una alternativa correcta (V / F):')
                respuesta = respuesta.lower()

            if (respuesta == choices[pregunta][2]):
                print('Correcto acertaste!')
                puntaje += 10
                print('Tu puntaje es de ' + str(puntaje))
            else:
                puntaje -= 5
                time.sleep(0.4)
                print('INCORRECTO!')
                print('Tu puntaje es de :' + str(puntaje))

        elif len(choices[pregunta]) - 1 == 5:
            for choice in range(len(choices[pregunta]) - 2):
                print(GREEN + choices[pregunta][choice] + RESET)
                

            respuesta = input('Escriba la alternativa correcta : ')
            while respuesta.lower() not in ['a', 'b', 'c', 'd', 'x']:
                respuesta = input(
                    'Por favor ingrese una alternativa correcta : ')
                respuesta = respuesta.lower()

            if (respuesta == 'x' or respuesta == 'X'):
                print('Esta es una pregunta con contenido secreto :O ')
                puntaje += 50
                print('Se te ha sumado un puntaje de +50')

            elif respuesta == choices[pregunta][5]:
                puntaje += 10
                time.sleep(0.6)
                print('La respuesta es correcta!!')
                print('Tu puntaje es de ' + str(puntaje))
            else:
                print('La respuesta es incorrecta ')
                puntaje -= 5
                print('Tu puntaje es de ' + str(puntaje))

        else:
            for choice in range(len(choices[pregunta]) - 1):
                print(GREEN + choices[pregunta][choice] + RESET)                

            respuesta = input('Escriba la alternativa correcta : ')
            while respuesta.lower() not in ['a', 'b', 'c', 'd']:
                respuesta = input(
                    'Por favor ingrese una alternativa correcta  : ')
                respuesta = respuesta.lower()

            correcta = choices[pregunta][4]
            time.sleep(0.2)
            if (respuesta == choices[pregunta][4]):
                print('Correcta! Siuuuuu')
                puntaje += 10
                print('Tu puntaje es de ' + str(puntaje))
            else:
                print('La respuesta es incorrecta')
                puntaje -= 5
                print('Tu puntaje es de ' + str(puntaje))

        index += 1
        if (index == len(preguntas)):
            time.sleep(0.7)
            print('\n\nHas terminado la trivia.')
            time.sleep(0.4)
            print('Y haz hecho un total de ' + GREEN + str(puntaje) + RESET +
                  ' puntos.\n \n')
            for i in range(0, random.randint(0, 4)):
                time.sleep(1)
            if (puntaje > 30) and (puntaje <= 70):
                print('Nada mal nakama pero...')
                time.sleep(1)
                print(
                    GREEN +
                    'Puedes aumentar tu puntaje drasticamente si respondes bien a esta pregunta'
                    + RESET)
                time.sleep(0.7)
                print(RED + 'o puedes perderlo  casi todo si erras.' + RESET)
                pregunta_extra = input('Quieres intentarlo? S: Si  N: No:   ')
                if pregunta_extra.lower() in ['S', 's']:
                    time.sleep(0.6)
                    print(
                        'La siguiente pregunta es un poco dificil asi que piensalo bien! \n'
                    )
                    time.sleep(0.4)
                    numero_pregunta = random.randint(0,
                                                     len(pregunta_extras) - 1)
                    print(YELLOW + "" + str(numero_pregunta) + ".)" +
                          pregunta_extras[numero_pregunta] + RESET)

                    for choice in range(
                            len(respuestas_extras[numero_pregunta]) - 1):
                        print(GREEN +
                              respuestas_extras[numero_pregunta][choice] +
                              RESET)
                        time.sleep(0.4)

                    respuesta = input('Escriba la alternativa correcta : ')
                    while respuesta.lower() not in ['a', 'b', 'c', 'd']:
                        respuesta = input(
                            'Por favor ingrese una alternativa correcta: ')
                        respuesta = respuesta.lower()

                    print('La respuesta es ...')
                    time.sleep(1)
                    if (respuesta == respuestas_extras[numero_pregunta][4]):
                        print('Correcta! Siuuuuuuuu')
                        puntaje += random.randint(30, 60)
                        print('Tu puntaje es de ' + str(puntaje))
                    else:
                        print('La respuesta es incorrecta')
                        puntaje -= random.randint(30, 60)
                        print('Tu puntaje es de ' + str(puntaje))
           
                  
                
              
            scores.append(puntaje)
            print()
            play_again = input(
                YELLOW +
                'Deseas jugar de nuevo? "S" Si ó cualquier tecla para  No : ' +
                RESET)
            if play_again.lower() in ['s', 'si']:
                print('Tus puntos se reiniciaran...')
                time.sleep(1)
                index = 0
                puntaje = random.randint(3, 12)
                os.system("clear")
                play = True
            else:
                play = False
        print()

        time.sleep(1)
score = ''
for item in scores:
    score += '| ' + str(item) + " "
score += ' |'
print(nombre + ' obtuviste unos puntajes de :')
print(score)
if len(scores) >= 2:
    avg_nakama(scores)
print(YELLOW + 'Adios Nakama... espero que te hayas divertido! :D' + RESET)