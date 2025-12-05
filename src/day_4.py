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
    return


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
    

    array = add_empty_boundary(input)
    array
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
