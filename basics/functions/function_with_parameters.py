def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still a long way to go!")
    else:
        print("We are almost there!")
if __name__ == "__main__":
    climb_ladder(5,2)
    climb_ladder(2,5)
