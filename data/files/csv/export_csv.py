import csv

def export(path,bot_count):
    print("Exporting...")
    print("How many bots would you like to input?")
    bot_count = int(input())
    with open(path, "a") as file:
        for count in range(bot_count):
            print("Please enter the bot ID:")
            bot_id = int(input())

            print("Please enter the bot name:")
            bot_name = str(input())

            print("Please enter the bot paint:")
            bot_paint = str(input())

            data = f"{bot_id},{bot_name},{bot_paint}\n"
            file.write(data)
    print("Done!")

def run():
    export("exported_bots.csv", 2)

if __name__ == "__main__":
    run()
