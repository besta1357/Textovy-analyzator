TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
vycistena_slova = []
pocet_malych_slov = 0
pocet_velkych_slov = 0
pocet_cisel = 0
pocet_slov_s_velkym_pismenom = 0
cisla_v_textu = []

for cisla in TEXTS[0].split():
    if cisla.isnumeric():       
       cisla_v_textu.append(int(cisla))
       suma_cisel = sum(cisla_v_textu)
print(cisla_v_textu)        
for slova in TEXTS[0].split():
    ciste_slovo = slova.strip(",.:;'")
    vycistena_slova.append(ciste_slovo)
    #num = [int(x) for x in TEXTS[0].split() if x.isdigit()]
    if slova.islower():
        pocet_malych_slov += 1
      #print(f"There are {pocet_malych_slov} lowercase words.")
    elif slova.isupper():
        pocet_velkych_slov += 1
       #print(f"There are {pocet_velkych_slov} uppercase words.")
    elif slova.isnumeric():
        pocet_cisel += 1
       #print(f"There are {pocet_cisel} numeric strings.")    
    for pismena in slova:
        break
    if pismena.isupper():
       pocet_slov_s_velkym_pismenom += 1
      #print(f"There are {pocet_slov_s_velkym_pismenom} titlecase words.")
print(f"There are {pocet_malych_slov} lowercase words.")
print(f"There are {pocet_velkych_slov} uppercase words.")
print(f"There are {pocet_slov_s_velkym_pismenom - pocet_velkych_slov} titlecase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {suma_cisel}")