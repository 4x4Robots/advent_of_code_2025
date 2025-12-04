import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_3_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_3_complete.txt"
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


@app.function
def find_max_in_string_loop(numbers: str, digits: int) -> int:
    """Find the number of digits which correspond to the largest number in a string of numbers."""
    maximum = 0
    max_i = 0
    max_j = 0
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            first_number = numbers[i]
            second_number = numbers[j]
            current_number = int(first_number+second_number)
            if current_number > maximum:
                maximum = current_number
                max_i = i
                max_j = j
    print(f"- In {numbers}, you can make the largest joltage possible by turning on the batteries labeled {max_i} and {max_j}, producing {maximum} jolts.")
    return maximum


@app.cell
def _(input, is_part_two):
    if is_part_two == False:
        maximum_part_1 = 0
        for _numbers in input:
            maximum_part_1 += find_max_in_string_loop(_numbers, digits=2)
        print(f"Total maximum: {maximum_part_1}")
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
