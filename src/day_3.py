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


@app.function
def find_max_in_str_recursive(numbers: str, numbers_found: str, count_missing: int) -> str:

    if count_missing == 0:
        #print("no missing digits")
        return numbers_found
    
    # break if we don't have enough digits left
    if len(numbers) <= count_missing:
        #print("not enough digits left for variation")
        return numbers_found + numbers

    #print(f"Searching for maximum in {numbers} with length {len(numbers)}; {numbers_found = } missing didgits: {count_missing}")
    # search for the largest digit in the first (n - count_missing) numbers
    largest_digit = numbers[0]
    largest_index = 0
    for i in range(0, len(numbers) - count_missing + 1):
        current_digit = numbers[i]
        #print(f"- Comparing {largest_digit} with {current_digit} at index {i}")
        if largest_digit < current_digit:
            largest_digit = current_digit
            largest_index = i

    numbers_found = numbers_found + str(largest_digit)

    return find_max_in_str_recursive(numbers[largest_index+1:], numbers_found, count_missing-1)


@app.cell
def _(input, is_part_two):
    if is_part_two:
        max_part_2 = 0
        for _numbers in input:
            part = find_max_in_str_recursive(_numbers, "", 12)
            print(f"Maximum number: {part}")
            max_part_2 += int(part)
        print(f"Total maximum: {max_part_2}")  # 170449335646486
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
