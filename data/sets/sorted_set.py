def observed():
    observations = []
    for count in range(5):
        print("Please enter an observation:")
        values = str(input())
        observations.append(values)
    return observations


def remove_observations(observations):
    loop_running = True
    while loop_running:
        print("Do you wish to remove an observation? (yes/no)?")
        answer = str(input())
        if answer == "yes":
            print("Please enter the observation you would like removed:")
            removed_data = str(input())
            observations.remove(removed_data)
        else:
            loop_running = False


def run():
    observations = observed()
    remove_observations(observations)
    print("Observations:")
    observation_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observation_set.add(data)
    for data in sorted(observation_set):
        print(f"{data[0]} observed {data[1]} times")


run()