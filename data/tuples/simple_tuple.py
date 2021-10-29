def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    smallest_step = min(likelihoods)
    return smallest_step


def run():
    result = likelihood()
    print(f"Minimum likelihood of falling: {result}%")


if __name__ == "__main__":
    run()