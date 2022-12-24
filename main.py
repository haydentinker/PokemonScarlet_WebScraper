from pokedex_Scraper import scrapePokedex
import os.path


def main():
    pokedex = []
    if not os.path.exists("pokedex.txt"):
        scrapePokedex()
    with open("pokedex.txt", "r") as f:
        entries = [line for line in f]

    for x in entries:
        entry = x.split(".")
        pokedex.append(entry[:-1])
    outputFile = open("pokemonOutput.txt", "w")
    outputFile.write("Pokedex_num, Pokemon Name, Where/How to get \n")
    while True:
        pokedex_num = input(
            "Enter the pokedex number for the pokemon you need or z to quit: "
        )
        if (pokedex_num == "z") | (pokedex_num == "Z"):
            break
        try:
            if (int(pokedex_num) > 0) & (int(pokedex_num) < len(pokedex)):
                outputFile.writelines(pokedex[int(pokedex_num)])
                outputFile.write("\n")
                print("Successfully outputted pokemon information into text file")
            else:
                print("Please enter a valid number or z")
        except ValueError:
            print("Please enter a valid number or z")
    outputFile.close()
    print("You can find information on missing pokemon in the output file")


if __name__ == "__main__":
    main()
