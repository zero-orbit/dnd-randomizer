#By Daniel Cortes
#3/15/2020
#DnD Character Randomizer
import time, random
#title
print('\n')
print('DND Character Randomizer')
print('_______________________________________________________________________')
print('\nBy Daniel Cortes\n')
time.sleep(1)
#variables
def main():
    races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Orc', 'Human',
    'Tiefling', 'Goliath', 'Genasi', 'Aarakocra', 'Aasimar', 'Bugbear', 'Hobgoblin',
    'Kobold', 'Lizardfolk', 'Kenku', 'Tabaxi', 'Tortle']

    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
    'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

    alignment = ['True Neutral', 'Lawful Good', 'Neutral Good', 'Chaotic Good',
    'Lawful Neutral', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']

    randrace = random.choice(races)
    randclass = random.choice(classes)
    randalign = random.choice(alignment)

    #randomize race
    print("Choosing race:")
    time.sleep(1)
    print(randrace)
    time.sleep(1)

    #randomize class

    print("\nChoosing class:")
    time.sleep(1)
    print(randclass)
    time.sleep(1)

    print("\nChoosing alignment:")
    time.sleep(1)
    print(randalign)
    time.sleep(1)

    print("\nCalculating Stats:")
    time.sleep(1)
    print("\nStrength: " + str(random.randrange(4,13)))
    time.sleep(1)
    print("\nDexterity: " + str(random.randrange(4,13)))
    time.sleep(1)
    print("\nConstitution: " + str(random.randrange(4,13)))
    time.sleep(1)
    print("\nIntelligence: " + str(random.randrange(4,13)))
    time.sleep(1)
    print("\nWisdom: " + str(random.randrange(4,13)))
    time.sleep(1)
    print("\nCharisma: " + str(random.randrange(4,13)))
    time.sleep(1)

main()
print('\nWhat would you like to do?')
print('1. Make another')
print('2. Quit')
choice = input('\n> ')
if choice == '1':
    main()
else:
    exit()
