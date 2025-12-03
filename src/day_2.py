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
    return input_tuples, range


@app.function
def id_is_valid_part_one(id: int) -> bool:
    # no repeating pattern twice
    id_str = str(id)
    middle = len(id_str) // 2
    #print(f"Checking id: {id} index of middle: {middle} first part: {id_str[:middle]} second part: {id_str[middle:]}")
    if id_str[:middle] == id_str[middle:]:
        return False
    return True


@app.cell
def _(range):
    def id_is_valid_part_two(id: int) -> bool:
        # no repeating patterns at all
        id_str = str(id)
        for pattern_length in range(1, len(id_str) // 2 + 1):
            print(f"Checking pattern {id_str[:pattern_length]} with length: {pattern_length}.")
            is_repeating = True
            for multiplier in range(1, len(id_str) // pattern_length + 1):
                print(f"Comparing: {id_str[:pattern_length]} == {id_str[multiplier*pattern_length:(multiplier+1)*pattern_length]}")
                if id_str[:pattern_length] != id_str[multiplier*pattern_length:(multiplier+1)*pattern_length]:
                    is_repeating = False
            if is_repeating:
                return False
            else:
                print("Still valid")

        return True
    return (id_is_valid_part_two,)


@app.cell
def _(id_is_valid_part_two, ui_switch_part_two):
    id_is_valid = id_is_valid_part_two if ui_switch_part_two.value else id_is_valid_part_one
    return (id_is_valid,)


@app.cell
def _(id_is_valid, range):
    def get_invalid_ids(start: int, stop: int) -> list[int]:
        invalid_ids = []
        for id in range(start, stop + 1):
            if not id_is_valid(id):
                invalid_ids.append(id)
        #print(f"- {start}-{stop} has {len(invalid_ids)} invalid IDs: {", ".join(invalid_ids)}.")
        print(f"- {start}-{stop} has {len(invalid_ids)} invalid IDs: {invalid_ids}.")
        return invalid_ids
    return (get_invalid_ids,)


@app.cell
def _(id_is_valid):
    #id_is_valid(212121)
    id_is_valid(2121212118)
    return


@app.cell
def _(get_invalid_ids, input_tuples):
    total_sum = 0
    for start, stop in input_tuples:
        invalid_ids = get_invalid_ids(start, stop)
        for invalid_id in invalid_ids:
            total_sum += invalid_id

    print(total_sum)
    f"Total sum of invalid ids: {total_sum}"
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
