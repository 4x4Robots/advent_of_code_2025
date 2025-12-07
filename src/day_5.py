import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_5_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_5_complete.txt"
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
    id_ranges = []
    ids = []
    with open(path_file, "r") as f:
        individual_ids = False
        while line := f.readline():
            if line.rstrip() == "":
                individual_ids = True
                continue  # don't add empty strings
            if not individual_ids:
                id_ranges.append(line.rstrip())
            else:
                ids.append(line.rstrip())
        #input = f.readlines()
        #input = [line.strip() for line in input if line.strip() != ""]

    {"ranges": id_ranges, "ids": ids}
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
