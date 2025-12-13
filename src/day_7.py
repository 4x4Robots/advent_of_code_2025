import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import copy
    return copy, mo


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
    return (read_input,)


@app.cell
def _(copy):
    def analyze_line(previous_line: str, current_line: str) -> str:
        illuminated_line = copy.deepcopy(current_line)
        for i, character in enumerate(previous_line):
            print(f"{i}: {character}")
        return illuminated_line
    return (analyze_line,)


@app.cell
def _(analyze_line, path_file, read_input):
    def calculate_illumination(path_file: str):
        input = read_input(path_file)
        illuminated_lines = [input[0]]
        for i in range(1, len(input)):
            new_line = analyze_line(illuminated_lines[i-1], input[i])
            illuminated_lines.append(new_line)
        return illuminated_lines

    calculate_illumination(path_file)
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
