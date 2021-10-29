def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return max(likelihoods), min(likelihoods)


def run():
    probabilities = likelihood()
    print(f"Minimum likelihood of falling: {probabilities[0]}%")
    print(f"Maximum likelihood of falling: {probabilities[1]}%")


if __name__ == "__main__":
    run()