import random as rd
import time

while True:

    print("1:Horror👻   2:Sci-fi🚀   3:Mystery🔎   4:Fantasy🐉   5:Comedy😂   6:Adventure🗺️   7:Crime🕵️   8:Romance❤️   9:Superhero🦸   10:Post-apocalyptic☢️")

    prompt = input("Select genre: ")

    name = input("Enter a desired name: ")

    match prompt:

        case "1":
            stories = [
                f"""At midnight, {name} entered the abandoned Blackwood Mansion.
A shadow slowly walked down the hallway toward {name}.
Every light suddenly went out, leaving only silence.
When the lights returned, {name} was no longer alone.""",

                f"""Everyone warned {name} to never visit the old cemetery.
A mysterious figure appeared between the graves and smiled.
The ground began to shake as whispers filled the air.
{name} realized escaping was already impossible.""",

                f"""{name} found a dusty mirror hidden in the attic.
The reflection suddenly started moving on its own.
A cold hand reached out from inside the glass.
{name} screamed as the mirror shattered into darkness."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "2":
            stories = [
                f"""In the year 2099, {name} woke up inside a spaceship.
The ship was heading toward a planet no human had ever seen.
Suddenly, an alien appeared on the screen.
It said, "We have been waiting for you, {name}".""",

                f"""{name} was exploring Mars when the ground suddenly opened.
Inside was a glowing machine from an unknown civilization.
{name} touched it and the entire planet began to shake.
Then a mysterious voice said, "You were not supposed to find this." """,

                f"""{name} entered a secret laboratory hidden beneath the city.
Scientists had created a machine that could travel through time.
{name} activated it and disappeared instantly.
When {name} returned, the world was completely different."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "3":
            stories = [
                f"""Detective {name} received a mysterious letter at midnight.
The letter contained only one strange address.
{name} arrived there and found an empty room.
On the wall, someone had written {name}'s name.""",

                f"""{name} discovered a locked room inside an old hotel.
Nobody knew who had locked it or why.
After opening it, {name} found a mysterious photograph.
The person in the photograph looked exactly like {name}.""",

                f"""{name} woke up and noticed that something was missing.
There were no signs of a break-in anywhere.
{name} searched the entire house for clues.
Then {name} noticed a hidden message under the table."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "4":
            stories = [
                f"""One morning, {name} discovered a magical door in the forest.
Behind it was a kingdom filled with dragons.
A wizard approached {name} and handed over a golden sword.
Then the kingdom suddenly came under attack.""",

                f"""{name} entered a mysterious castle floating above the clouds.
A dragon was guarding a glowing treasure.
Instead of attacking, the dragon asked {name} for help.
{name} accepted and entered the dragon's kingdom.""",

                f"""While walking through the forest, {name} found a talking sword.
The sword told {name} about an ancient evil returning.
{name} picked it up and entered the dark castle.
The final battle was about to begin."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "5":
            stories = [
                f"""{name} walked into a restaurant and ordered a pizza.
The waiter accidentally brought a giant birthday cake instead.
{name} complained, but the cake suddenly started talking.
Everyone in the restaurant began laughing.""",

                f"""{name} decided to become a professional chef for one day.
The first dish looked completely terrible.
{name} tasted it and immediately regretted everything.
Even the dog refused to eat it.""",

                f"""{name} woke up late and rushed to college.
After running for ten minutes, {name} realized it was Sunday.
{name} went back home and slept for another five hours."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "6":
            stories = [
                f"""{name} discovered an ancient map hidden inside a book.
The map showed the location of a legendary treasure.
{name} travelled across the jungle to find it.
But someone else was already waiting there.""",

                f"""{name} boarded a ship heading toward an unexplored island.
A huge storm suddenly appeared on the horizon.
The ship crashed near a mysterious cave.
{name} entered the cave looking for a way out.""",

                f"""{name} climbed the highest mountain in the kingdom.
At the top, {name} discovered a strange glowing portal.
Without thinking twice, {name} stepped inside.
A completely unknown world appeared before them."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "7":
            stories = [
                f"""{name} was suspected of stealing a priceless diamond.
The police found no evidence against {name}.
Then a mysterious message appeared on the detective's desk.
It contained the location of the missing diamond.""",

                f"""{name} witnessed a strange robbery in the city.
The thief escaped before anyone could identify them.
{name} noticed one small clue left behind.
It was a photograph of the criminal.""",

                f"""{name} received an anonymous message about a secret crime.
The message revealed a hidden location.
{name} went there and discovered stolen money.
Then the police suddenly arrived."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "8":
            stories = [
                f"""{name} met someone new at a small coffee shop.
They talked for hours about their dreams.
Before leaving, the stranger gave {name} a mysterious note.
It simply said, "Meet me here tomorrow." """,

                f"""{name} was walking through the park when someone called their name.
It was an old friend {name} had not seen for years.
They spent the evening talking about the past.
By sunset, they realized their feelings had never changed.""",

                f"""{name} received a surprise gift from someone special.
Inside was a handwritten letter full of memories.
{name} smiled while reading every word.
It was the beginning of something beautiful."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "9":
            stories = [
                f"""{name} suddenly discovered they could control electricity.
A dangerous villain attacked the city that night.
{name} put on a mask and flew toward the battlefield.
The city finally had a new hero.""",

                f"""{name} woke up with incredible super strength.
A giant robot was destroying everything downtown.
{name} jumped into action without hesitation.
The final battle had begun.""",

                f"""{name} was just an ordinary student until a strange meteor landed nearby.
After touching it, {name} gained mysterious powers.
A secret organization immediately started hunting {name}.
Now {name} had to save the city."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case "10":
            stories = [
                f"""{name} woke up after the world had been destroyed.
The cities were empty and the streets were silent.
{name} found a radio broadcasting one final message.
Someone was still alive.""",

                f"""{name} walked through the ruins of the old city.
Food and water were becoming impossible to find.
Suddenly, {name} discovered a hidden underground shelter.
But something was already living inside.""",

                f"""{name} had survived the apocalypse for five years.
One day, a strange signal appeared on the radio.
It contained coordinates to a safe settlement.
{name} decided to follow the signal."""
            ]

            story = rd.choice(stories)

            for line in story.splitlines():
                print(f"``{line}``")
                time.sleep(2)

        case _:
            print("Please select a given genre...")