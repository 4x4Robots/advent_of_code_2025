import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import copy
    import math
    import numpy as np
    return (mo,)


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_9_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_9_complete.txt"
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
    input[:25]
    return (read_input,)


@app.cell
def _(path_file, read_input):
    def convert_input(path_file: str) -> list[tuple[int, int]]:
        input = read_input(path_file)
        red_tiles = [tuple(map(int, line.split(","))) for line in input]
        # (column, row)
        return red_tiles

    red_tiles = convert_input(path_file)
    red_tiles
    return


@app.cell
def _():
    def calculate_area(pos1, pos2):
        """Calculate the area between two posistions."""
        delta_x = abs(pos2[0] - pos1[0]) + 1
        delta_y = abs(pos2[1] - pos1[1]) + 1
        area = delta_x * delta_y
        print(f"Calculated area for {pos1} and {pos2} = {area}")
        return area

    assert calculate_area((2, 5), (9, 7)) == 24
    assert calculate_area((7, 1), (11, 7)) == 35
    assert calculate_area((7, 3), (2, 3)) == 6
    assert calculate_area((2, 5), (11, 1)) == 50
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
