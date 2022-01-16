from random import choice
from os import system

system("clear")

houses = ["Slitheryn", "Hufflepuff", "Ravenclaw", "Gryffendor"]
your_house = choice(houses)

classes = [
    "charms",
    "defense against the dark arts",
    "herbology",
    "quiddage",
    "potions",
]
your_class = choice(classes)

people = [
    "🐉 Haggrid",
    "⚡Harry Potter",
    "🐌 Ron Weasley",
    "💀 Professor Snape",
    "🔮 Professor Dumbledor",
    "🐈 Professor McGonagal",
    "🐸 Neville Longbottom",
    "👳 Professor Quirrell",
    "🙊 He Who Shall Not Be Named",
    "💯 Hermoine Granger",
    "💌 Hedwig the Owl",
    "🐀 Scabbers the Rat",
    "🐶🐶🐶 Fluffy the 3-headed Dog",
    "🐩 Fang the Coward Dog",
]
your_person = choice(people)

places = [
    "in Haggrid's hut",
    "in Diagon Alley",
    "at #4 Privett Drive",
    "in Hogwarts Great Hall",
    "next to the Whomping Tree",
    "in the Dungeons",
    "in the Chamber of Secrets",
]
your_place = choice(places)



print("🎩 Hello, I am the sorting hat 🎩")
print("🎩 I will sort you into a Hogwarts House 🎩")

for house in houses:
    print(f" - {house}")
print("\nWhat is your name?")

your_name = input("\n> ")

print(
    f"{your_name} of {your_house} and {your_person} studied {your_class} {your_place}"
)

print("\n\nNow what do you want to do?")
print("1) play quiddage")
print("2) make a potion")
print("3) use a charm")
print("\nType a number:")
player_choice = input("\n> ")

if player_choice == "1":
    # this is the quiddage block
    houses.remove(your_house)
    opponent_house = choice(houses)
    print(f"Your house, {your_house} is playing against {opponent_house}")

    if your_house == 'Gryffendor':
        print("you won the house cup! 🏆")
    else:
        print(f"you {choice(['won', 'lost'])}")
if player_choice == "2":
    # this is the potion block
    print("you are now super strong and did 10 pushups! 💪")
if player_choice == "3":
    # this is the charm block
    print("❇️❇️  wingardium leviosa!!!! ❇️❇️")
