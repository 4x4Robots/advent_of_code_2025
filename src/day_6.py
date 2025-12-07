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


@app.cell
def _():
    # testing of find_next
    _text = "593 3311    456 23  9724 *   +  *  345"
    _end_pos = 0
    while _end_pos < len(_text):
        print("New loop")
        _start_pos = _end_pos
        _end_pos = find_next(_text, _start_pos, find_space=True)
        print(f"Extracted string: '{_text[_start_pos:_end_pos]}'")
        _start_pos = _end_pos + 1
        _end_pos = find_next(_text, _start_pos, find_space=False)
        print(f"Extracted string: '{_text[_start_pos:_end_pos]}'")
    return


@app.cell
def _(input):
    def repackage_input(input):
        as_array = []
        for line in input:
            as_array.append(line.split(" "))
            print(as_array[-1])

    repackage_input(input)
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
