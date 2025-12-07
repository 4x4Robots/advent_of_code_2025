import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import copy
    return (mo,)


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_6_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_6_complete.txt"
    return PATH_FILE_COMPLETE, PATH_FILE_EXAMPLE


@app.cell
def _(PATH_FILE_COMPLETE, PATH_FILE_EXAMPLE, ui_switch_complete_file):
    path_file = PATH_FILE_COMPLETE if ui_switch_complete_file.value else PATH_FILE_EXAMPLE
    path_file
    return (path_file,)


@app.cell
def _(ui_switch_part_two):
    is_part_two = ui_switch_part_two.value
    return


@app.cell
def _(path_file):
    def read_input(path_file):
        with open(path_file, "r") as f:
            input = f.readlines()
            input = [line.strip() for line in input if line.strip() != ""]
        return input

    input = read_input(path_file)
    input
    return (input,)


@app.function
def find_next(text: str, start_pos: int, find_space: bool) -> int:
    """find_space == True  the next space, == False the next non space character"""
    for i in range(start_pos, len(text)):
        if find_space:
            if text[i] == " ":
                return i
        else:
            if text[i] != " ":
                return i
    return len(text)


@app.function
def split_line(line: str, debug: bool = False) -> list[str]:
    parts = []
    _end_pos = 0
    while _end_pos < len(line):
        if debug:
            print("New loop")
        _start_pos = _end_pos
        _end_pos = find_next(line, _start_pos, find_space=True)
        parts.append(line[_start_pos:_end_pos])
        if debug:
            print(f"Extracted string: '{line[_start_pos:_end_pos]}'")
        _start_pos = _end_pos + 1
        _end_pos = find_next(line, _start_pos, find_space=False)
        # don't add spaces as part
        if debug:
            print(f"Extracted string: '{line[_start_pos:_end_pos]}'")
    return parts


@app.cell
def _():
    # testing of find_next
    _text = "593 3311    456 23  9724 *   +  *  345"
    split_line(_text, debug=True)
    return


@app.cell
def _(input, ui_switch_complete_file):
    def repackage_input(input):
        as_array = []
        for line in input:
            as_array.append(split_line(line))
            print(as_array[-1])
            if len(as_array) > 1:  # all lines should contain the same number of parts
                assert len(as_array[-1]) == len(as_array[-2])
            
        if not ui_switch_complete_file.value:  # example input should be the same length
            as_array.insert(3, ["0" for i in range(len(as_array[-1]))])
        #zipped = zip([row for row in as_array])
        #print(list(zipped))  # wrong output!
        return as_array

    repackage_input(input)
    return (repackage_input,)


@app.cell
def _(input, repackage_input, ui_switch_complete_file):
    def calculate_column(part1, part2, part3, part4, operator, debug: bool = False):
        if debug:
            print(f"Calculating: {part1} {part2} {part3} {part4} with operator {operator}")
        if operator == "*":
            return int(part1) * int(part2) * int(part3) * int(part4)
        if operator == "+":
            return int(part1) + int(part2) + int(part3) + int(part4)
        raise ValueError("Unknown operator")

    def calculate_part_1(input):
        as_array = repackage_input(input)
        sum = 0
        for i in range(len(as_array[0])):
            result = calculate_column(as_array[0][i], as_array[1][i], as_array[2][i], as_array[3][i], as_array[4][i], not ui_switch_complete_file.value)
            if not ui_switch_complete_file.value:
                print(f" = {result}")
            sum += result

        print(f"Total sum: {sum}")
        return sum

    calculate_part_1(input)  # part 1: 5667835681547
    return


@app.cell
def _(mo):
    max_length = mo.ui.number(label="max length", value=83)
    return (max_length,)


@app.cell
def _(input, max_length):
    for _line in input:
        print(_line[:max_length.value])  # each block starts with an operator
    return


@app.cell
def _(input):
    def find_start_pos(line, debug: bool = False) -> list[int]:
        parts = []
        start_pos = []
        _end_pos = 0
        while _end_pos < len(line):
            if debug:
                print("New loop")
            _start_pos = _end_pos
            _end_pos = find_next(line, _start_pos, find_space=True)
            parts.append(line[_start_pos:_end_pos])
            start_pos.append(_start_pos)
            if debug:
                print(f"Extracted string: '{line[_start_pos:_end_pos]}'")
            _start_pos = _end_pos + 1
            _end_pos = find_next(line, _start_pos, find_space=False)
            # don't add spaces as part
            if debug:
                print(f"Extracted string: '{line[_start_pos:_end_pos]}'")
        return start_pos


    def analyze_part_2(input):
        start_positions = find_start_pos(input[-1])
    
        max_length = 80
        for line in input:
            print(line[:max_length])
        test = list("".join([" " for i in range(len(input[0]))]))
        for start_pos in start_positions:
            test[start_pos] = "^"
        print("".join(test[:max_length]))

    analyze_part_2(input)
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
