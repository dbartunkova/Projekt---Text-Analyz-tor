oddelovac = ("-" * 40)
data = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,\n 
Fossil Butte is a ruggedly impressive\n 
topographic feature that rises sharply\n
some 1000 feet above Twin Creek Valley\n 
to an elevation of more than 7500 feet\n 
above sea level. The butte is located just\n 
north of US 30N and the Union Pacific Railroad,\n 
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright\n 
red, purple, yellow and gray beds of the Wasatch\n 
Formation. Eroded portions of these horizontal\n 
beds slope gradually upward from the valley floor\n 
and steepen abruptly. Overlying them and extending\n 
to the top of the butte are the much steeper\n 
buff-to-white beds of the Green River Formation,\n 
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects\n 
a portion of the largest deposit of freshwater fish\n 
fossils in the world. The richest fossil fish deposits\n  
are found in multiple limestone layers, which lie some\n  
100 feet below the top of the butte. The fossils\n  
represent several varieties of perch, as well as\n  
other freshwater genera and herring similar to those\n  
in modern oceans. Other fish such as paddlefish,\n  
garpike and stingray are also present.'''
         ]
user = input("Type your username: ")
password = input("Type your password: ")

print(oddelovac)

if data.get(user) == password:
    print("Welcome to the app,", user)
    print("We have 3 texts to be analyzed.")
    print(oddelovac)

    try:
        vyber_textu = int(input("Enter a number btw. 1 and 3 to select: "))
        print(oddelovac)

        VYBER_UZIVATELE = TEXTS[vyber_textu - 1]

        jednotliva = VYBER_UZIVATELE.split(" ")

        vycistena = []

        for slovo in jednotliva:
            vycistena.append(slovo.strip(".,! ? : "))

        print("There are", len(vycistena), "words in the selected text.")
        print("There are", len([x for x in vycistena if x.istitle()]), "titlecase words.")
        print("There are", len([x for x in vycistena if x.isupper() and x.isalpha()]), "uppercase words.")
        print("There are", len([x for x in vycistena if x.islower()]), "lowercase words.")
        print("There are", len([x for x in vycistena if x.isdigit()]), "numeric strings.")

        celkova_suma = 0
        while vycistena:
            char = vycistena.pop()
            if type(char) == int:
                celkova_suma += char
            elif type(char) == str:
                if char.isnumeric():
                    celkova_suma += int(char)

        print("The sum of all the numbers", celkova_suma)
        print(oddelovac)
        print("LEN|  OCCURENCES  |NR.")
        print(oddelovac)
        for slovo in jednotliva:
            vycistena.append(slovo.strip(".,! ? : "))

        print("1|", sum(1 for x in vycistena if len(x) == 1) * "*", "|", sum(1 for x in vycistena if len(x) == 1))
        print("2|", sum(1 for x in vycistena if len(x) == 2) * "*", "|", sum(1 for x in vycistena if len(x) == 2))
        print("3|", sum(1 for x in vycistena if len(x) == 3) * "*", "|", sum(1 for x in vycistena if len(x) == 3))
        print("4|", sum(1 for x in vycistena if len(x) == 4) * "*", "|", sum(1 for x in vycistena if len(x) == 4))
        print("5|", sum(1 for x in vycistena if len(x) == 5) * "*", "|", sum(1 for x in vycistena if len(x) == 5))
        print("6|", sum(1 for x in vycistena if len(x) == 6) * "*", "|", sum(1 for x in vycistena if len(x) == 6))
        print("7|", sum(1 for x in vycistena if len(x) == 7) * "*", "|", sum(1 for x in vycistena if len(x) == 7))
        print("8|", sum(1 for x in vycistena if len(x) == 8) * "*", "|", sum(1 for x in vycistena if len(x) == 8))
        print("9|", sum(1 for x in vycistena if len(x) == 9) * "*", "|", sum(1 for x in vycistena if len(x) == 9))
        print("10|", sum(1 for x in vycistena if len(x) == 10) * "*", "|", sum(1 for x in vycistena if len(x) == 10))
        print("11|", sum(1 for x in vycistena if len(x) == 11) * "*", "|", sum(1 for x in vycistena if len(x) == 11))

    except ValueError:
        print('You did not type a number.')

else:
    print("Wrong user/or password.")
