# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Yumiku")
define b = Character("Haru")
define q = Character("Você")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene escola

    # This shows a character sprite. A
    # placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show yumiko

    # These display lines of dialogue.


    e "Ola seja bem vind(a,o)"
    e "eu me chamo Yumiko muito prazer"

    hide yumiko
    show haru

    b "Yumiko eu existo sabia"

    hide haru
    show yumiko

    e "Assim *risadinha* desculpa essa e a Haru"

    hide yumiko
    show haru

    b "Oi..."
    b "Me chamo Haru"

    hide haru
    show yumiko

    e "Bem, seja muito bem vind(a,o)"

    hide yumiko
    show haru

    b "Voce ja falou isso Yumi"

    hide haru
    show yumiko

    e "..."
    e "Vdd"

    hide yumiko
    show haru

    b "Vamos mostrar logo a faculdade e finalizar nosso trabalho"

    hide haru
    show yumiko

    e "Sim sim desculpa"

    hide yumiko
    show haru

    b"Licença *sai*"

    hide haru
    show yumiko

    e "...."

    scene corredor
    with fade

    show yumiko

    e "Vamos começa-"

    hide yumiko
    show haru

    b "Eu vou falar com o professor encontro voces depois"

    hide haru
    show yumiko

    e "Esta bem"

    e "Te vejo dps"

    hide yumiko
    show haru

    b "...*sai*"

    hide haru
    show yumiko

    e "..."
    e "Ela e assim msm"
    e "Ela teve um passado muito dificil..."
    e "Entao nao a julgo por ser assim..."
    e "vamos começar então"
    q "Sim vamos..."
    e "...!!!"

    # pergunta

    e "VOCE FALA??!!"
menu:

    "Sim....eu nao falei antes por que voce nao perguntou":
        jump choco1

    "Obvio que sim tenho boca pra que?":
        jump choco2

label choco1:

    show yumiko

    e"vdd voce tem um ponto"

    jump yumiko

label choco2:

    show yumiko

    e "quanta ignorancia, eu sei que voce tem boca pra fala mas nao precisava disso..."

    jump yumiko

label yumiko:

    "..."
    e "Vamos?"
    q "Sim"
    scene fundo
    with fade

    q "Foi ate legal hj"
    q "A Yumiko tem uma personalidade..."
    q "Eu diria muito forte..."
    q "No  final do dia nao vimos a Haru"
    q "A Yumiko disse que nao vai contar ao professor"
    q "E que vai perguntar oque aconteceu com ela nesse tempo que ela ficou fora"
    q "Eu nao me importei com ela ter ficado fora, eu teria ficado fora tambem"
    q "Mas sobre a faculdade..."
    q "Estou vendo que e so o começo de tudo"
    q "E que pode piorar no final de contas"
    q "Agora ir pra casa e descansar"
    q "Que amanha sera um longo dia"
    q "PROXIMO EPISODEO->"

    scene fundo
    with fade

    # This ends the game.
    return
