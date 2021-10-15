def sum_weight(beep_weight, bop_weight):
    total = beep_weight + bop_weight
    return total

def avg_weight(beep_weight, bop_weight):
    avg = (beep_weight + bop_weight) / 2
    return avg


def run():
    print("Please enter Beep's weight:")
    beep_weight = float(input())
    print("Please enter Bop's weight:")
    bop_weight = float(input())
    print("Would you like the \"sum\" or \"avg\" weight?")
    answer = input()
    if answer == "sum":
        response = sum_weight(beep_weight, bop_weight)
        print(f"The total weight is {response}")
    elif answer == "avg":
        response = avg_weight(beep_weight, bop_weight)
        print(f"The avg weight is {response}")
    else:
        print("I am not sure what you are asking.")
run()
