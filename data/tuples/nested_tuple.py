def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run():
    step = steps()
    good_steps = []
    bad_steps = []
    for count in step:
        if count[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)
    good = len(good_steps)
    bad = len(bad_steps)
    print(f"Good Steps: {good}\nBad Steps: {bad}")


if __name__ == "__main__":
    run()

