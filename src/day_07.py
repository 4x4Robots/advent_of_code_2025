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
    PATH_FILE_EXAMPLE = "input/input_day_7_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_7_complete.txt"
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
    input[:20]
    return input, read_input


@app.function
def analyze_line(previous_line: str, current_line: str) -> (str, int):
    illuminated_line = [character for character in current_line]
    number_of_splits = 0
    for i, character in enumerate(previous_line):
        #print(f"{i}: {character}")
        
        if previous_line[i] == "S":
            if illuminated_line[i] == ".":
                illuminated_line[i] = "|"
            else:
                raise ValueError("Can't start illumination!")
                
        if illuminated_line[i] == "^" and previous_line[i] == "|":
            number_of_splits += 1  # split to two beams
            illuminated_line[i-1] = "|"
            illuminated_line[i+1] = "|"
        elif previous_line[i] == "|":
            # beam continues straigt
            illuminated_line[i] = "|"
        
    return "".join(illuminated_line), number_of_splits


@app.cell
def _(path_file, read_input):
    def calculate_illumination(path_file: str):
        input = read_input(path_file)
        illuminated_lines = [input[0]]
        total_number_of_splits = 0
        for i in range(1, len(input)):
            new_line, number_of_splits = analyze_line(illuminated_lines[i-1], input[i])
            illuminated_lines.append(new_line)
            total_number_of_splits += number_of_splits
        return illuminated_lines, total_number_of_splits

    calculate_illumination(path_file)  # part 1: 1687
    return


@app.cell
def _(explore_direction):
    def explore_direction_brute_force(input: list[str], row_index: int, beam_position: int, number_of_found_ways: int, go_left: bool) -> int:
        """Return the total number of ways if going left or right.
        Don't change input!"""
        #print(f"Exploring: {row_index = }, {beam_position = }, {number_of_found_ways = }")
        #print(f"Current input line: {input[row_index]}")
    
        if row_index + 1 >= len(input):
            # reached bottom
            return number_of_found_ways + 1

        if input[row_index][beam_position] == "^":
            number_of_found_ways = explore_direction(input, row_index+1, beam_position-1, number_of_found_ways, go_left)  # go left
            number_of_found_ways = explore_direction(input, row_index+1, beam_position+1, number_of_found_ways, go_left)  # go right
        elif input[row_index][beam_position] == ".":
            number_of_found_ways = explore_direction(input, row_index+1, beam_position, number_of_found_ways, go_left)  # go straight

        return number_of_found_ways

        # always explore left, then right

    def find_start_position(first_line: str) -> int:
        for i, character in enumerate(first_line):
            if character == "S":
                print(f"Found starting index: {i}")
                return i
        

    #number_of_found_ways = explore_direction(input, 1, find_start_position(input[0]), 0, go_left=True)  # takes way too long
    #print(f"Number of posssible tachyon paths: {number_of_found_ways}")
    #number_of_found_ways
    return


@app.cell
def _(input):
    def count_possible_paths(input) -> (int, list[list[int]]):
        """Return the total amount of possible paths for a tachyon beam.
        Don't change input."""
        number_of_lasers = [[0 for i in range(len(row))] for row in input]
        #print(number_of_lasers)
    
        for column_index, character in enumerate(input[0]):
            if character == "S":  # find start
                number_of_lasers[0][column_index] += 1
            
        for row_index in range(1, len(input)):
            for column_index, character in enumerate(input[row_index]):
                #if character == "S":
                #    number_of_lasers[row_index][column_index] += 1
                if character == ".":  # only go straigt
                    number_of_lasers[row_index][column_index] += number_of_lasers[row_index-1][column_index]
                if character == "^":
                    number_of_lasers[row_index][column_index-1] += number_of_lasers[row_index-1][column_index]  # go left
                    number_of_lasers[row_index][column_index+1] += number_of_lasers[row_index-1][column_index]  # go right

        total_number_paths = 0
        for number_lasers in number_of_lasers[-1]:
            total_number_paths += number_lasers
    
        return total_number_paths, number_of_lasers

    number_of_paths, laser_paths = count_possible_paths(input)
    print(f"Number of posssible tachyon paths: {number_of_paths}")  # part 2: 390684413472684
    number_of_paths
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
