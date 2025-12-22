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
    def read_input(path_file):
        id_ranges = []
        ids = []
        with open(path_file, "r") as f:
            individual_ids = False
            while line := f.readline():
                if line.rstrip() == "":
                    individual_ids = True
                    continue  # don't add empty strings
                if not individual_ids:
                    range_str = line.rstrip()
                    min_max = range_str.split("-")
                    id_ranges.append([int(min_max[0]), int(min_max[1])])
                else:
                    ids.append(int(line.rstrip()))
            #input = f.readlines()
            #input = [line.strip() for line in input if line.strip() != ""]
        return id_ranges, ids

    id_ranges, ids = read_input(path_file)
    {"ranges": id_ranges, "ids": ids}
    return id_ranges, ids


@app.cell
def _():
    def is_in_range(id, range):
        return id >= range[0] and id <= range[1]

    def is_in_ranges(id, ranges):
        for range in ranges:
            if is_in_range(id, range):
                return True
        return False
    return (is_in_ranges,)


@app.cell
def _(id_ranges, ids, is_in_ranges):
    def check_ids(ids, ranges):
        number_of_fresh_ingredients = 0
        for id in ids:
            is_fresh = is_in_ranges(id, ranges)
            if is_fresh:
                number_of_fresh_ingredients += 1
                print(f"- Ingredient with id {id} is fresh.")
            else:
                print(f"- Ingredient with id {id} is spoiled.")
        print(f"Total number of fresh ingredients: {number_of_fresh_ingredients}")
        return number_of_fresh_ingredients

    check_ids(ids, id_ranges)  # part 1: 617
    return


@app.cell
def _():
    def determine_all_fresh(ranges):
        """Set of unique ids in ranges"""
        valid_ids = []
        for r in ranges:
            for i in range(r[0], r[1]+1):
                valid_ids.append(i)

        unique_ids = set(valid_ids)
        print(f"Unique ids: {unique_ids}")
        print(f"There are {len(unique_ids)} fresh ids.")
        return unique_ids

    #determine_all_fresh(id_ranges)  # this bricks my laptop
    return


@app.cell
def _(id_ranges):
    def consolidate_ranges_try_1(ranges):  # doesn't work when a new range bridges the gap between two other ranges
        """Try to combine all overlapping ranges"""
        consolidated_ranges = []
        for _range in ranges:
            was_added = False
            for inner in consolidated_ranges:
                if _range[0] >= inner[0] and _range[0] <= inner[1]:  # minium is inside
                    if _range[1] > inner[1]:
                        inner[1] = _range[1]  # extend above
                        was_added = True
                if _range[1] >= inner[0] and _range[1] <= inner[1]:  # maximum is inside
                    if _range[0] < inner[0]:
                        inner[0] = _range[0]  # extend below
                        was_added = True
            if not was_added:  # wasn't able to extend an already exisiting range
                consolidated_ranges.append(_range)

        print(f"{consolidated_ranges = }")
        return consolidated_ranges       

    consolidate_ranges_try_1(id_ranges)
    return


@app.function
def count_elements_in_range(range):
    return range[1] - range[0] + 1


@app.function
def consolidate_ranges_try_2(ranges):
    new_ranges = []
    for _range in ranges:
        print(f"- Analyzing range {_range}")
        new_min = _range[0]
        new_max = _range[1]
        #for i in range(len(new_ranges)):
        for inner in new_ranges:
            #print(f"inner: {inner}")
            inner_subsumed = False
            if _range[0] >= inner[0] and _range[0] <= inner[1]:  # minimum of current _range is part of inner
                print(f"{inner[0]} is part of range {_range}")
                if inner[1] > new_max:
                    new_max = inner[1]  # extend above
                    print(f"New max found: {new_max}")
                inner_subsumed = True
            if _range[1] >= inner[0] and _range[1] <= inner[1]:  # maximum of current _range is part of inner
                print(f"{inner[1]} is part of range {_range}")
                if inner[0] < new_min:
                    new_min = inner[0]  # extend below
                    print(f"New min found: {new_min}")
                inner_subsumed = True    
            if inner_subsumed:
                print(f"Deleting range: {inner}")
                #del inner  # always delete (is part of current _range)
                new_ranges.remove(inner)
        _range[0] = new_min
        _range[1] = new_max
        print(f"Adding range: {_range}")
        new_ranges.append(_range)

    print(f"Consolidated ranges: {new_ranges}")
    return new_ranges


@app.cell
def _(copy):
    def consolidate_ranges(ranges):
        new_ranges = []
        for outer in ranges:
            print(f"- Analyzing outer: {outer}")
            outer_subsumed = False
            for inner in new_ranges:
                # always adapting the inner range (every range at least once)
                # subsumed outer ranges become (0, 0)
                if outer[0] > inner[0] and outer[0] < inner[1]:  # minium of outer is part of inner
                    print(f"outer min {outer[0]} is part of {inner}")
                    outer_subsumed = True
                    if outer[1] > inner[1]:
                        inner[1] = outer[1]  # extend inner above
                        print(f"New max found: {inner[1]}")
                if outer[1] > inner[0] and outer[1] < inner[1]: # maximum of outer is part of inner
                    print(f"outer max {outer[1]} is part of {inner}")
                    outer_subsumed = True
                    if outer[0] < inner[0]:
                        inner[0] = outer[0]  # extend inner below
                        print(f"New min found: {inner[0]}")
            if outer_subsumed:
                print(f"Subsumed: {outer}")
                #new_ranges.remove(outer)  # or replace with (0, 0)
            else:
                print(f"Adding: {outer}")
                new_ranges.append(copy.deepcopy(outer))
        print(f"All ranges: {new_ranges}")
        return new_ranges
    return (consolidate_ranges,)


@app.cell
def _(consolidate_ranges, id_ranges):
    def count_fresh_ids(ranges):
        new_ranges = consolidate_ranges(ranges)
        num_fresh_ids = 0
        for _range in new_ranges:
            num_fresh_ids += count_elements_in_range(_range)
        print(f"There are a total of {num_fresh_ids} fresh ids.")
        return num_fresh_ids

    # part 2 solution: 398109659614960
    count_fresh_ids(id_ranges)  # part 2: 368069932536331 too high - 317974505182124 -- too low
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
