# Definición de personajes
define noora = Character("Noora", color="#6495ED")
define eva = Character("Eva", color="#FF69B4")
define isaac = Character("Isaac", color="#FF7F50")

# Definición de imágenes
image noora_neutral = "images/noora_neutral.png"
image noora_happy = "images/noora_happy.png"
image isaac_neutral = "images/isaac_neutral.png"
image isaac_happy = "images/isaac_happy.png"
image eva_neutral = "images/eva_neutral.png"
image eva_happy = "images/eva_happy.png"

image bg_university = "images/bg_university.png"
image bg_library = "images/bg_library.png"
image bg_cafeteria = "images/bg_cafeteria.png"
image bg_frognerparken = "images/bg_frognerparken.png"
image bg_night = "images/bg_night.png"

# Pantalla para bajar el menú
screen choice:
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.8
        spacing 20

        for i in items:
            button:
                action i.action
                text i.caption

# Escena 1: Universidad de Oslo
label start:
    scene bg_university with fade
    show isaac_neutral at center with dissolve

    "Isaac, un estudiante español de intercambio, está esperando a Noora en la entrada de la Universidad de Oslo. Está nervioso por practicar su noruego."

    hide isaac_neutral
    show isaac_neutral at right with dissolve

    isaac "Hola Noora... ¿me ayudarás hoy con mi noruego? ¡Estoy a punto de darme por vencido!"

    hide isaac_neutral
    show noora_neutral at left with dissolve

    noora "Isaac, ¡no me asustes! Vamos a ser positivos. Si no te rindes, lo vas a conseguir. ¿Cómo va todo?"

    hide noora_neutral
    show isaac_neutral at right with dissolve

    isaac "Bueno, he estado repasando... pero tengo miedo de pronunciarlo mal. ¿Qué tal si lo intento?"

    hide isaac_neutral
    show noora_neutral at left with dissolve

    noora "A ver, ¿cómo me saludarías por la mañana?"

    menu:
        "God morgen":
            jump saludo_correcto
        "Ha det bra":
            jump saludo_incorrecto

label saludo_correcto:
    hide noora_neutral
    show isaac_happy at right with dissolve

    isaac "God morgen, Noora!"

    hide isaac_happy
    show noora_happy at left with dissolve

    noora "¡Eso es! ¡Lo has dicho perfectamente! ¿Ves? No es tan difícil. ¿Te animas a decir algo más?"

    hide noora_happy
    show isaac_happy at right with dissolve

    isaac "¡Claro! ¿Qué tal si te pregunto cómo estás?"

    hide isaac_happy
    show noora_happy at left with dissolve

    noora "Vale, pues ¿cómo me preguntarías?"

    menu:
        "Hvordan har du det?":
            jump pregunta_correcta
        "Hva skjer?":
            jump pregunta_incorrecta

label saludo_incorrecto:
    hide noora_neutral
    show isaac_neutral at right with dissolve

    isaac "Ha det bra!"

    hide isaac_neutral
    show noora_neutral at left with dissolve

    noora "¡Eso es más bien para despedirse, no para saludar! Pero no te preocupes, ¡estás aprendiendo!"

    noora "Ahora prueba a preguntarme cómo estoy."

    menu:
        "Hvordan har du det?":
            jump pregunta_correcta
        "Hva skjer?":
            jump pregunta_incorrecta

label pregunta_correcta:
    hide noora_happy
    show isaac_happy at right with dissolve

    isaac "Hvordan har du det?"

    hide isaac_happy
    show noora_happy at left with dissolve

    noora "¡Perfecto! ¿Ves? ¡Lo estás pillando! ¿Cómo me siento? Pues hoy muy bien, aunque me estoy ahogando en deberes."

    hide noora_happy
    show isaac_happy at right with dissolve

    isaac "¡Me suena a algo muy noruego eso de ahogarse en deberes! ¿Tú no haces nada divertido?"

    hide isaac_happy
    show noora_happy at left with dissolve

    noora "¿Sabías que los noruegos tenemos una relación especial con las montañas y las nieves? Para nosotros, hacer algo divertido es... escalar una montaña o esquiar. Pero, un café y una charla como esta no están nada mal."

    jump llegada_eva

label pregunta_incorrecta:
    hide noora_neutral
    show isaac_neutral at right with dissolve

    isaac "Hva skjer?"

    hide isaac_neutral
    show noora_neutral at left with dissolve

    noora "Hmm... 'Hva skjer?' significa más bien '¿Qué pasa?'"

    noora "Está bien. Pero se usa entre amigos, de manera informal, no para preguntar educadamente cómo está alguien. Recuérdalo."

    hide noora_neutral
    show isaac_neutral at right with dissolve

    isaac "¡Vaya! ¡Entonces me he equivocado!"

    hide isaac_neutral
    show noora_neutral at left with dissolve

    noora "No te preocupes, Isaac. ¡Lo importante es que te atreves a hablar!"

    noora "¡Vamos a seguir practicando!"

    jump llegada_eva

# Escena 2: Biblioteca en Oslo
label llegada_eva:
    scene bg_library with fade
    hide noora_happy
    hide noora_neutral
    hide isaac_happy
    hide isaac_neutral

    show isaac_neutral at left
    show eva_neutral at right with dissolve

    eva "Hei, Isaac! Hvordan går det?"

    hide eva_neutral
    show isaac_neutral at left with dissolve

    isaac "Hei, Eva! ¡Necesito tu ayuda con algo urgente!"

    hide isaac_neutral
    show eva_neutral at right with dissolve

    eva "¿Qué pasa, Isaac? ¿Algo con el noruego otra vez?"

    hide eva_neutral
    show isaac_neutral at left with dissolve

    isaac "Sí... me cuesta mucho recordar algunas cosas. No me sale bien la pronunciación de algunas palabras."

    hide isaac_neutral
    show eva_happy at right with dissolve

    eva "¡Ah, ya veo! El sonido 'skj' es complicado al principio, pero lo importante es relajarte. Trata de hacerlo como si fueras a decir 'shh', como cuando pides silencio."

    hide eva_happy
    show isaac_neutral at left with dissolve

    isaac "¡Eso tiene sentido! ¡Lo intentaré!"

    hide isaac_neutral
    show eva_happy at right with dissolve

    eva "¡Lo harás genial! No te pongas nervioso, que con práctica todo sale."

    menu:
        "Takk":
            jump gracias_correcto
        "Bare ha det bra":
            jump gracias_incorrecto

label gracias_correcto:
    hide eva_happy
    show isaac_happy at left with dissolve

    isaac "Takk!"

    hide isaac_happy
    show eva_happy at right with dissolve

    eva "¡Exactamente! 'Takk' es la forma correcta de decir 'gracias' en noruego. Vær så god, Isaac."

    jump cafeteria_con_noora

label gracias_incorrecto:
    hide eva_happy
    show isaac_neutral at left with dissolve

    isaac "Bare ha det bra"

    hide isaac_neutral
    show eva_happy at right with dissolve

    eva "Hmm, vale, adiós. Pero recuerda decir 'takk'! Es lo que se dice para agradecer cuando alguien te ayuda."

    jump cafeteria_con_noora

# Escena 3: Cafetería en Oslo
label cafeteria_con_noora:
    scene bg_cafeteria with fade
    hide isaac_happy
    hide isaac_neutral
    hide eva_happy
    hide eva_neutral

    show noora_happy at left

    noora "¡Hola, chicos! ¿Cómo va esa mente desbordada por el noruego?"

    hide noora_happy
    show eva_happy at right

    eva "Isaac ya está empezando a dominar el 'til' y el 'for'. ¡Estoy muy orgullosa!"

    hide eva_happy
    show isaac_happy at center

    isaac "¡Teoría básica! ¡Pero ya me he liado con algunas frases!"

    hide isaac_happy
    show noora_happy at left

    noora "¿Ya has encontrado algo de comer? Porque el cerebro también necesita comida para funcionar."

    hide noora_happy
    show eva_happy at right

    eva "Noora tiene razón. Yo siempre me pido un café, pero Isaac, si quieres, te recomiendo algo de aquí... ¿un 'kakao'?"

    hide eva_happy
    show isaac_happy at center

    isaac "¡Kakao? ¡Eso suena como algo muy... reconfortante!"

    hide isaac_happy
    show noora_happy at left

    noora "Es una bebida tradicional. Básicamente, es chocolate caliente noruego. Si lo bebes, es como un abrazo en una taza."

    hide noora_happy
    show isaac_happy at center

    isaac "¡Perfecto, lo que necesito! Un abrazo líquido, ¡esto sí que es cultura noruega!"

    scene black with fade
    centered "Una hora después..."
    pause 1.0

    scene bg_cafeteria with fade
    show isaac_happy at center

    isaac "Bueno, se me ha pasado el tiempo volando... creo que debería ir volviendo."

    isaac "¡Nos vemos en el parque dentro de un rato! Pero antes, me gustaría despedirme de vosotras como un auténtico noruego."

    menu:
        "Vi sees i parken!":
            jump saludo_hei_cafeteria
        "God morgen, det er godt å se deg!":
            jump saludo_incorrecto_cafeteria

label saludo_hei_cafeteria:
    hide isaac_happy
    show isaac_happy at center
    isaac "Vi sees i parken!"
    hide isaac_happy
    show noora_happy at left
    noora "¡Perfecto, Isaac! ¡Tienes madera de noruego!"

    # Interludio
    scene black with fade
    centered "Unas horas más tarde..."
    pause 1.0

    jump escena_parque

label saludo_incorrecto_cafeteria:
    hide isaac_happy
    show isaac_neutral at center
    isaac "God morgen, det er godt å se deg!"
    hide isaac_happy
    show noora_neutral at left
    noora "No, Isaac, 'god morgen' es solo para la mañana."

    # Interludio
    scene black with fade
    centered "Unas horas más tarde..."
    pause 1.0

    jump escena_parque

# Escena 4: Paseo por Frognerparken
label escena_parque:
    scene bg_frognerparken with fade
    hide noora_happy
    hide eva_happy
    hide isaac_happy
    hide isaac_neutral

    show noora_happy at left
    "Después de tomar su kakao y descansar, los tres deciden dar un paseo por Frognerparken, rodeados de las famosas esculturas de Gustav Vigeland."
    noora "Mira estas esculturas, Isaac. ¿Las conoces?"
    hide noora_happy
    show isaac_neutral at center
    isaac "¡Son impresionantes! No puedo dejar de pensar en cuántas horas de trabajo tiene que haber detrás de estas."
    hide isaac_neutral
    show noora_happy at left
    noora "Sí, claro, pero lo interesante es lo que intentan transmitir. La vida noruega está llena de contrastes: calma y fuerza, silencio y movimiento."
    hide noora_happy
    show eva_happy at right
    eva "Noora está obsesionada con las esculturas. Siempre que venimos aquí, se pone a filosofar sobre ellas."
    hide eva_happy
    show isaac_neutral at center
    isaac "Bueno, las esculturas son bonitas, pero no puedo evitar pensar en lo complicado que debe ser hacer una de estas sin perder la cabeza."
    hide isaac_neutral
    show noora_happy at left
    noora "¡Si logras sobrevivir a un invierno noruego, puedes hacer cualquier cosa!"
    hide noora_happy
    show eva_happy at right
    eva "Isaac, si no puedes con el invierno, ¿por qué no te apuntas a unas clases de esquí? ¡Eso sí que es una experiencia completa de noruego!"
    hide eva_happy
    show isaac_neutral at center
    isaac "¿Esquiar? ¡Nunca lo he intentado! Pero si esto va a mejorar mi noruego, ¡estoy listo!"
    hide isaac_neutral
    show noora_happy at left
    noora "¡Eso es el espíritu! ¡Te esperamos en la pista, entonces!"
    jump despedida_final


label despedida_final:
    scene bg_night with fade
    show isaac_happy at center
    with dissolve
    isaac "Gracias, chicas. La verdad es que Noruega me está ganando. ¡Lo estoy disfrutando mucho!"
    hide isaac_happy
    show eva_happy at right
    with dissolve
    eva "¡Lo estás haciendo genial! Nos vemos pronto."
    hide eva_happy
    show noora_happy at left
    with dissolve
    noora "No te olvides de lo más importante: el 'kakao' es tu amigo ahora."

    # Menú de despedida final
    menu:
        "Ha en fin kveld!":
            jump despedida_correcta
        "God natt!":
            jump despedida_incorrecta

label despedida_correcta:
    hide noora_happy
    show isaac_happy at center
    with dissolve

    isaac "Ha en fin kveld!"

    hide isaac_happy
    show noora_happy at left
    with dissolve

    noora "¡Perfecto, Isaac! Así se despiden los noruegos cuando aún no es hora de dormir."

    hide noora_happy
    show eva_happy at right
    with dissolve

    eva "¡Nos vemos en la próxima aventura!"

    return

label despedida_incorrecta:
    hide noora_happy
    show isaac_neutral at center
    with dissolve

    isaac "God natt!"

    hide isaac_neutral
    show noora_thinking at left
    with dissolve

    noora "¡Eso sería si ya te fueras a dormir! Pero has estado cerca, no está mal."

    hide noora_thinking
    show eva_laughing at right
    with dissolve

    eva "¡La próxima vez seguro que lo clavas!"

    return