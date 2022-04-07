from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dados import *
import random

# config janela

janela = Tk()
janela.title("")
janela.geometry("550x510")
janela.configure(bg="#feffff")

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# config frame

frame_pokemon = Frame(janela, width=550, height=290, relief="flat", bg="#feffff")
frame_pokemon.grid(row=1, column=0)


# config change_pokemon
def change_pokemon(p):
    global image_pokemon, pokemon_image

    # Trocando a cor do fundo
    frame_pokemon["bg"] = pokemon[p]["categoria"][3]
    pokemon_category["bg"] = pokemon[p]["categoria"][3]
    pokemon_name["bg"] = pokemon[p]["categoria"][3]
    pokemon_id["bg"] = pokemon[p]["categoria"][3]

    # Trocando de pokemon
    pokemon_name["text"] = p
    pokemon_category["text"] = pokemon[p]["categoria"][1]
    pokemon_id["text"] = pokemon[p]["categoria"][0]
    image_pokemon = pokemon[p]["categoria"][2]

    image_pokemon = Image.open(image_pokemon)
    image_pokemon = image_pokemon.resize((238, 238))
    image_pokemon = ImageTk.PhotoImage(image_pokemon)

    pokemon_image = Label(frame_pokemon, image=image_pokemon, relief="flat",
                          bg=pokemon[p]["categoria"][3], fg="#403d3d")
    pokemon_image.place(x=60, y=50)

    pokemon_category.lift()

    # Trocando status do pokemon
    pokemon_life["text"] = pokemon[p]["status"][0]
    pokemon_attack["text"] = pokemon[p]["status"][1]
    pokemon_defense["text"] = pokemon[p]["status"][2]
    pokemon_speed["text"] = pokemon[p]["status"][3]
    pokemon_total["text"] = pokemon[p]["status"][4]

    # Colocando habilidades no pokemon
    pokemon_skill_1["text"] = pokemon[p]["habilidades"][0]
    pokemon_skill_2["text"] = pokemon[p]["habilidades"][1]


# config frame: name
pokemon_name = Label(frame_pokemon, text="Pokemon", relief="flat", anchor=CENTER,
                     font="Fixedsys 20", bg="#feffff", fg="#403d3d")
pokemon_name.place(x=12, y=15)

# config frame: category
pokemon_category = Label(frame_pokemon, text="None type", relief="flat", anchor=CENTER,
                         font="Ivy 10 bold", bg="#feffff", fg="#403d3d")
pokemon_category.place(x=12, y=50)

# config frame: id
pokemon_id = Label(frame_pokemon, text="#000", relief="flat", anchor=CENTER,
                   font="Ivy 10 bold", bg="#feffff", fg="#403d3d")
pokemon_id.place(x=12, y=75)

# config status

pokemon_status = Label(janela, text="Status", relief="flat", anchor=CENTER,
                       font="Vedana 20", bg="#feffff", fg="#403d3d")
pokemon_status.place(x=15, y=310)

# config status: life
pokemon_life = Label(janela, text="Hp: None", relief="flat", anchor=CENTER,
                     font="Verdana 10", bg="#feffff", fg="#403d3d")
pokemon_life.place(x=15, y=360)

# config status: attack
pokemon_attack = Label(janela, text="Ataque: None", relief="flat", anchor=CENTER,
                       font="Verdana 10", bg="#feffff", fg="#403d3d")
pokemon_attack.place(x=15, y=385)

# config status: defense
pokemon_defense = Label(janela, text="Defesa: None", relief="flat", anchor=CENTER,
                        font="Verdana 10", bg="#feffff", fg="#403d3d")
pokemon_defense.place(x=15, y=410)

# config status: speed
pokemon_speed = Label(janela, text="Velocidade: None", relief="flat", anchor=CENTER,
                      font="Verdana 10", bg="#feffff", fg="#403d3d")
pokemon_speed.place(x=15, y=435)

# config status: total
pokemon_total = Label(janela, text="Total: None", relief="flat", anchor=CENTER,
                      font="Verdana 10", bg="#feffff", fg="#403d3d")
pokemon_total.place(x=15, y=460)

# config skills
pokemon_skills = Label(janela, text="Habilidades", relief="flat", anchor=CENTER,
                       font="Verdana 20", bg="#feffff", fg="#403d3d")
pokemon_skills.place(x=180, y=310)

pokemon_skill_1 = Label(janela, text="", relief="flat", anchor=CENTER,
                        font="Verdana 10", bg="#feffff", fg="#403d3d")
pokemon_skill_1.place(x=185, y=355)

pokemon_skill_2 = Label(janela, text="", relief="flat", anchor=CENTER,
                        font="Verdana 10", bg="#feffff", fg="#403d3d")
pokemon_skill_2.place(x=185, y=380)

# config button

# config button: pikachu
image_pikachu = Image.open("pokemon/cabeca-pikachu.png")
image_pikachu = image_pikachu.resize((40, 40))
image_pikachu = ImageTk.PhotoImage(image_pikachu)

button_pikachu = Button(janela, command=lambda: change_pokemon("Pikachu"), image=image_pikachu, text="Pikachu",
                        width=150, relief="raised", overrelief=RIDGE, compound=LEFT,
                        anchor=NW, font="Verdana 12", bg="#feffff", fg="#403d3d")
button_pikachu.place(x=375, y=10)

# config button: bulbasaur
image_bulbasaur = Image.open("pokemon/cabeca-bulbasaur.png")
image_bulbasaur = image_bulbasaur.resize((40, 40))
image_bulbasaur = ImageTk.PhotoImage(image_bulbasaur)

button_bulbasaur = Button(janela, command=lambda: change_pokemon("Bulbasaur"), image=image_bulbasaur, text="Bulbasaur",
                          width=150, relief="raised", overrelief=RIDGE, compound=LEFT,
                          anchor=NW, font="Verdana 12", bg="#feffff", fg="#403d3d")
button_bulbasaur.place(x=375, y=65)

# config button: charmander
image_charmander = Image.open("pokemon/cabeca-charmander.png")
image_charmander = image_charmander.resize((40, 40))
image_charmander = ImageTk.PhotoImage(image_charmander)

button_charmander = Button(janela, command=lambda: change_pokemon("Charmander"), image=image_charmander,
                           text="Charmander", width=150, relief="raised", overrelief=RIDGE, compound=LEFT,
                           anchor=NW, font="Verdana 12", bg="#feffff", fg="#403d3d")
button_charmander.place(x=375, y=120)

# config button: gengar
image_gengar = Image.open("pokemon/cabeca-gengar.png")
image_gengar = image_gengar.resize((40, 40))
image_gengar = ImageTk.PhotoImage(image_gengar)

button_gengar = Button(janela, command=lambda: change_pokemon("Gengar"), image=image_gengar, text="Gengar",
                       width=150, relief="raised", overrelief=RIDGE, compound=LEFT,
                       anchor=NW, font="Verdana 12", bg="#feffff", fg="#403d3d")
button_gengar.place(x=375, y=175)

# config button: gyarados
image_gyrados = Image.open("pokemon/cabeca-gyarados.png")
image_gyrados = image_gyrados.resize((40, 40))
image_gyrados = ImageTk.PhotoImage(image_gyrados)

button_gyrados = Button(janela, command=lambda: change_pokemon("Gyarados"), image=image_gyrados, text="Gyrados",
                        width=150, relief="raised", overrelief=RIDGE, compound=LEFT,
                        anchor=NW, font="Verdana 12", bg="#feffff", fg="#403d3d")
button_gyrados.place(x=375, y=230)

# config button: dragonite
image_dragonite = Image.open("pokemon/cabeca-dragonite.png")
image_dragonite = image_dragonite.resize((40, 40))
image_dragonite = ImageTk.PhotoImage(image_dragonite)

button_dragonite = Button(janela, command=lambda: change_pokemon("Dragonite"), image=image_dragonite,
                          text="Dragonite", width=150, relief="raised", overrelief=RIDGE, compound=LEFT,
                          anchor=NW, font="Verdana 12", bg="#feffff", fg="#403d3d")
button_dragonite.place(x=375, y=285)

# config pokemon aleatorio

lista_pokemon = ["Pikachu", "Bulbasaur", "Charmander", "Gengar", "Gyarados", "Dragonite"]

sortear = random.sample(lista_pokemon, 1)
change_pokemon(sortear[0])

janela.mainloop()
