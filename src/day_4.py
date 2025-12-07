import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_4_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_4_complete.txt"
    return PATH_FILE_COMPLETE, PATH_FILE_EXAMPLE


@app.cell
def _(PATH_FILE_COMPLETE, PATH_FILE_EXAMPLE, ui_switch_complete_file):
    path_file = PATH_FILE_COMPLETE if ui_switch_complete_file.value else PATH_FILE_EXAMPLE
    path_file
    return (path_file,)


@app.cell
def _(ui_switch_part_two):
    is_part_two = ui_switch_part_two.value
    return (is_part_two,)


@app.cell
def _(path_file):
    with open(path_file, "r") as f:
        input = f.readlines()
        input = [line.strip() for line in input if line.strip() != ""]

    input
    return (input,)


@app.cell
def _(input):
    # state[row][column]
    def add_empty_boundary(input: list[str]):
        # add an empty row and column for convienence
        max_rows = len(input)
        max_cols = len(input[0])
        print(f"The current input contains {max_rows} rows and {max_cols} columns.")

        empty_row = "".join(["." for i in range(0, max_cols+2)])

        empty_box_input = []
        empty_box_input.append(empty_row)
        for row in input:
            empty_box_input.append("." + row + ".")
        empty_box_input.append(empty_row)
        print(f"The input with an empty box around contains {len(empty_box_input)} rows and {len(empty_box_input[0])} columns.")

        return empty_box_input


    boxed_input = add_empty_boundary(input)
    boxed_input
    return (boxed_input,)


@app.cell
def _(boxed_input):
    def convert_to_array(input: str) -> list[list[str]]:
        array = []
        #max_rows = len(input)
        #max_cols = len(input)
        for row in input:
            row_list = []
            for char in row:
                row_list.append(char)
            array.append(row_list)
        return array

    array = convert_to_array(boxed_input)
    array[:2]
    return (array,)


@app.cell
def _(array):
    def convert_to_str(array: list[list[str]]) -> list[str]:
        as_str = []
        for row in array:
            as_str.append("".join(row))
        return as_str

    _test_convert_str = convert_to_str(array)
    _test_convert_str
    return (convert_to_str,)


@app.function
def place_is_valid(array, x, y):
    adjacent_paper = -1  # don't count yourself
    for i in range(x-1, x+2):  # non-inclusive
        for j in range(y-1, y+2):
            if array[i][j] == "@" or array[i][j] == "x":
                adjacent_paper += 1
    return adjacent_paper < 4


@app.function
def remove_paper_rolls(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            array[i][j] = "." if array[i][j] == "x" else array[i][j]
    return array


@app.cell
def _(convert_to_str):
    def count_valid_places(array, repeat: bool = False):
        max_rows = len(array)
        max_cols = len(array[0])
        number_of_valid_places = 0
        first = True
        number_of_valid_places_this_iteration = 1
        while number_of_valid_places_this_iteration > 0:
            number_of_valid_places_this_iteration = 0
            for i in range(1, max_rows-1):
                for j in range(1, max_cols-1):
                    if array[i][j] == "@" or array[i][j] == "x":  # only analyze if there is paper at this place
                        place_valid = place_is_valid(array, i, j)
                        array[i][j] = "x" if place_valid else array[i][j]
                        if place_valid:
                            number_of_valid_places_this_iteration += 1
            number_of_valid_places += number_of_valid_places_this_iteration
            print(f"You can remove {number_of_valid_places_this_iteration} paper rolls.")
            if repeat:
                array = remove_paper_rolls(array)
                for row in convert_to_str(array):
                    print(row)
            else:
                number_of_valid_places_this_iteration = 0
        return array, number_of_valid_places
    return (count_valid_places,)


@app.cell
def _(array, convert_to_str, count_valid_places, is_part_two):
    analyzed_array, number_of_valid_places = count_valid_places(array, is_part_two)
    print(f"Number of valid places: {number_of_valid_places}")  # part 1: 1445. part 2: 8317
    convert_to_str(analyzed_array)
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
