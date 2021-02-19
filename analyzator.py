oddelovac = ("-" * 40)
data = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

user = input("Zadej uzivatelske jmeno: ")
password = input("Zadej sve heslo: ")

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
    

#výpočet součtu čísel (ale počítá mi to číslice), jak to prosím mám upravit?       
        celkova_suma = 0
        while vycistena:
            char = vycistena.pop()
            if type(char) == int:
                celkova_suma += char
            elif type(char) == str:
                for ch in list(char):
                    if ch.isdigit():
                        celkova_suma += int(ch)
        print("The sum of all the numbers", celkova_suma)
        
        print(oddelovac)
        print("LEN|  OCCURENCES  |NR.")
        print(oddelovac)
        

        for slovo in jednotliva:
            vycistena.append(slovo.strip(".,! ? : "))
            
#počet slov o různé délce (jak prosím udělat, aby se přiřadily i počty hvězdiček?); (proč mi to nepočítá i slova, která jsou z číslic?)
        print("1|", sum(1 for x in vycistena if len(x) == 1))
        print("2|", sum(1 for x in vycistena if len(x) == 2))
        print("3|", sum(1 for x in vycistena if len(x) == 3))
        print("4|", sum(1 for x in vycistena if len(x) == 4))
        print("5|", sum(1 for x in vycistena if len(x) == 5))
        print("6|", sum(1 for x in vycistena if len(x) == 6))
        print("7|", sum(1 for x in vycistena if len(x) == 7))
        print("8|", sum(1 for x in vycistena if len(x) == 8))
        print("9|", sum(1 for x in vycistena if len(x) == 9))
        print("10|", sum(1 for x in vycistena if len(x) == 10))
        print("11|", sum(1 for x in vycistena if len(x) == 11))



    except ValueError:

        print('You did not type a number.')

else:
    print("Wrong user/or password.")
