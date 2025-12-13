import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import copy
    import math
    import numpy as np
    return math, mo


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_8_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_8_complete.txt"
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
    def convert_to_coordinate(line: str) -> (int, int, int):
        return tuple(map(int, line.split(",", 3)))

    def read_input_coordinates(path_file):
        input = read_input(path_file)
        coordinates = [convert_to_coordinate(line) for line in input]
        return coordinates

    read_input_coordinates(path_file)[:3]
    return (read_input_coordinates,)


@app.cell
def _(math, path_file, read_input_coordinates):
    def calc_distance(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    
    def calculate_distances(coordinates):
        distances = [[-1.0 for i in range(len(coordinates))] for j in range(len(coordinates))]
        #print(distances)
        for row in range(len(coordinates)):
            for column in range(len(coordinates)):
                distances[row][column] = calc_distance(coordinates[row], coordinates[column])

        for row in distances:
            print(row)

    calculate_distances(read_input_coordinates(path_file))
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
