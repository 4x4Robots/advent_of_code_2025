import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_2_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_2_complete.txt"
    return PATH_FILE_COMPLETE, PATH_FILE_EXAMPLE


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_complete_file
    return (ui_switch_complete_file,)


@app.cell
def _(PATH_FILE_COMPLETE, PATH_FILE_EXAMPLE, ui_switch_complete_file):
    path_file = PATH_FILE_COMPLETE if ui_switch_complete_file.value else PATH_FILE_EXAMPLE
    path_file
    return (path_file,)


@app.cell
def _(path_file):
    with open(path_file, "r") as f:
        input = f.readline()

    # Split input at ,
    input_ranges = [range.strip() for range in input.split(",")]
    #print(input_ranges)
    # Convert to tuple
    _mode = "map"
    if _mode == "for loop":
        input_tuples = []
        for range in input_ranges:
            parts = range.split("-")
            input_tuples.append((int(parts[0]), int(parts[1])))
            #print(parts)
    if _mode == "list comprehension":
        input_tuples = [(int(parts[0]), int(parts[1])) for range in input_ranges for parts in [range.split("-")]]
    if _mode == "map":
        input_tuples = [tuple(map(int, range.split("-"))) for range in input_ranges]
    print(input_tuples)

    input_ranges
    return


if __name__ == "__main__":
    app.run()
