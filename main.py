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
import basics.repetitions.nested_loop.nested as nested_loop_nested
import basics.repetitions.nested_loop.nesting as nested_loop_nesting
import basics.repetitions.while_loop.ascii as while_loop_ascii
import basics.repetitions.while_loop.count as while_loop_count
import basics.repetitions.while_loop.factorial as while_loop_factorial
import basics.repetitions.while_loop.len as while_loop_len
import basics.repetitions.while_loop.len2 as while_loop_len2
import basics.repetitions.while_loop.simple as while_loop_simple
import basics.repetitions.while_loop.sum100 as while_loop_sum100
import basics.repetitions.while_loop.sum_user_numbers as while_loop_sum_user_numbers
import basics.decisions.nested_decisions.nestception as nested_decisions_nestception
import basics.decisions.nested_decisions.nested as nested_decisions_nested
import basics.decisions.simple_decision.comparison_operators as simple_decision_comparison_operators
import basics.decisions.simple_decision.counter as simple_decision_counter
import basics.decisions.simple_decision.if_ as simple_decision_if
import basics.decisions.simple_decision.if_elif_else as simple_decision_if_elif_else
import basics.decisions.simple_decision.if_else as simple_decision_if_else
import basics.decisions.simple_decision.modulo_operator as simple_decision_modulo_operator
import basics.decisions.and_operator as decisions_and_operator
import basics.decisions.or_operator as decisions_or_operator
import basics.decisions.review as decisions_review
import basics.functions.ascii_character as functions_ascii_character
import basics.functions.ascii_code as functions_ascii_code
import basics.functions.function_calls as functions_function_calls
import basics.functions.function_with_loop as functions_function_with_loop
import basics.functions.function_with_nesting as functions_function_with_nesting
import basics.functions.function_with_parameter as functions_function_with_parameter
import basics.functions.function_with_parameters as functions_function_with_parameters
import basics.functions.multiple_functions as functions_multiple_functions
import basics.functions.return_values as functions_return_values
import basics.functions.simple_function as functions_simple_function


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
    elif response == "for_loop_characters":
        for_loop_characters.run()
    elif response == "for_loop_count_down":
        for_loop_count_down.run()
    elif response == "for_loop_membership_operators":
        for_loop_membership_operators.run()
    elif response == "for_loop_range":
        for_loop_range.run()
    elif response == "for_loop_reverse":
        for_loop_reverse.run()
    elif response == "for_loop_simple":
        for_loop_simple.run()
    elif response == "nested_loop_nested":
        nested_loop_nested.run()
    elif response == "nested_loop_nesting":
        nested_loop_nesting.run()
    elif response == "while_loop_ascii":
        while_loop_ascii.run()
    elif response == "while_loop_count":
        while_loop_count.run()
    elif response == "while_loop_factorial":
        while_loop_factorial.run()
    elif response == "while_loop_len":
        while_loop_len.run()
    elif response == "while_loop_len2":
        while_loop_len2.run()
    elif response == "while_loop_simple":
        while_loop_simple.run()
    elif response == "while_loop_sum100":
        while_loop_sum100.run()
    elif response == "while_loop_sum_user_numbers":
        while_loop_sum_user_numbers.run()
    elif response == "nested_decisions_nestception":
        nested_decisions_nestception.run()
    elif response == "nested_decisions_nested":
        nested_decisions_nested.run()
    elif response == "simple_decision_comparison_operators":
        simple_decision_comparison_operators.run()
    elif response == "simple_decision_counter":
        simple_decision_counter.run()
    elif response == "simple_decision_if":
        simple_decision_if.run()
    elif response == "simple_decision_if_elif_else":
        simple_decision_if_elif_else.run()
    elif response == "simple_decision.if_else":
        simple_decision_if_else.run()
    elif response == "simple_decision_modulo_operator":
        simple_decision_modulo_operator.run()
    elif response == "decisions_and_operator":
        decisions_and_operator.run()
    elif response == "decisions_or_operator":
        decisions_or_operator.run()
    elif response == "decisions_review":
        decisions_review.run()
    elif response == "functions_ascii_character":
        functions_ascii_character.run()
    elif response == "functions_ascii_code":
        functions_ascii_code.run()
    elif response == "functions_function_calls":
        functions_function_calls.run()
    elif response == "functions_function_with_loop":
        functions_function_with_loop.cross_bridge()
    elif response == "functions_function_with_nesting":
        functions_function_with_nesting.identify()
    elif response == "functions_function_with_parameter":
        functions_function_with_parameter.escape_by(plan)





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

