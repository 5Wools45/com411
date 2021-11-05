def observed():
    observations = []
    for count in range(7):
        print("Please enter an observation:")
        values = str(input())
        observations.append(values)
    return observations


def run():
    print("Counting observations...")
    observed_values = observed()
    observation_set = set()
    for value in observed_values:
        data = (value, observed_values.count(value))
        observation_set.add(data)
    for data in observation_set:
        print(f"{data[0]} observed {data[1]} times")


run()



