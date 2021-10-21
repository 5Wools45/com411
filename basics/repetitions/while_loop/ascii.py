def run():
    print("How many bars should be charged?")
    #getting users response:
    bars_to_charge = int(input())
    #adding a counter to track charged bars
    charged_bars = 0
    #adding while loop to track how many bars have been charged
    while charged_bars <= bars_to_charge:
        print(f"Charging: {charged_bars * ' █'}")
        charged_bars +=1

if __name__ == "__main__":
    run()