import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.review as review
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input
import basics.repetitions.for_loop.characters as for_loop_characters
import basics.repetitions.for_loop.count_down as for_loop_count_down
import basics.repetitions.for_loop.membership_operators as for_loop_membership_operators
import basics.repetitions.for_loop.range as for_loop_range
import basics.repetitions.for_loop.reverse as for_loop_reverse
import basics.repetitions.for_loop.simple as for_loop_simple




def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "escape_characters":
        escape_characters.run()
    elif response == "ascii_art":
        ascii_art.run()
    elif response == "ascii_robot":
        ascii_robot.run()
    elif response == "data_types":
        data_types.run()
    elif response == "review":
        review.run()
    elif response == "string_operators":
        string_operators.run()
    elif response == "user_input":
        user_input.run()


def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")


run()

