import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    #PATH_FILE = "input/input_day_1_example.txt"
    PATH_FILE = "input/input_day_1_complete.txt"
    return (PATH_FILE,)


@app.cell
def _(PATH_FILE):
    with open(PATH_FILE, "r") as f:
        input = f.readlines()

    # Strip withespaces and newlines
    for i in range(len(input)):
        input[i] = input[i].strip()
        input[i] = input[i].strip('\n')

    # Remove empty lines
    input = [line for line in input if line != ""]

    _i = 0
    for line in input:
        _i += 1
        if _i < 12:
            print(line)
    return (input,)


@app.cell
def _(input):
    input
    return


@app.function
def rotate_dial_recursive(start_position: int, steps: list[str], index: int, num_zeros: int = 0, num_positions: int = 100) -> (int, int):
    """Rotate the position by the steps at the given index left or right. Return the new position."""
    if index >= len(steps):
        print("Reached end of steps.")
        return (start_position, num_zeros)

    step = steps[index]
    if step[0] == "L":
        direction = -1
    elif step[0] == "R":
        direction = +1
    else:
        raise ValueError(f"Don't recognize step: {step}")
    step = int(step[1:]) * direction
    
    position = (start_position + step) % num_positions
    print(f"- The dial is rotated {steps[index]} to point at {position}.")
    if position == 0:
        num_zeros += 1

    return rotate_dial_recursive(position, steps, index + 1, num_zeros, num_positions)


@app.cell
def _(input):
    end_position, num_zeros = rotate_dial_recursive(start_position=50, steps=input, index=0, num_positions=100)
    f"{end_position = }, {num_zeros = }"
    return


@app.cell
def _(step):
    def rotate_dial_part_one(start_position: int, lines: list[str], num_positions: int = 100) -> int:
        """Rotate the position by the steps at the given index left or right. Return the number of zeros."""
        position = start_position
        num_zeros = 0
    
        for line in lines:
            if line[0] == "L":
                direction = -1
            elif line[0] == "R":
                direction = +1
            else:
                raise ValueError(f"Don't recognize step: {step}")
            step = int(line[1:]) * direction
    
            position = (position + step) % num_positions
            print(f"- The dial is rotated {line} to point at {position}.")
            if position == 0:
                num_zeros += 1

        return num_zeros
    return (rotate_dial_part_one,)


@app.cell
def _(input, rotate_dial_part_one):
    result_one = rotate_dial_part_one(50, input, num_positions = 100)
    result_one
    return


@app.cell
def _(step):
    def rotate_dial_part_two(start_position: int, lines: list[str], num_positions: int = 100) -> int:
        """Rotate the position by the steps at the given index left or right. Return the number of zeros."""
        position = start_position
        num_zeros = 0
        print(f"- The dial starts by pointing at {start_position}.")
    
        for line in lines:
            if line[0] == "L":
                direction = -1
            elif line[0] == "R":
                direction = +1
            else:
                raise ValueError(f"Don't recognize step: {step}")
            step = int(line[1:]) * direction

            # How many times was 0 passed?
            zeros_passed = 0
            if position + step > num_positions:
                zeros_passed = (position + step) // num_positions
                if position == 0:
                    zeros_passed -= 1
            if position + step < 0:
                zeros_passed = -(position + step - num_positions)  // num_positions
                if position == 0:
                    zeros_passed -= 1
            num_zeros += zeros_passed

            # rotate to new position
            position = (position + step) % num_positions

            # don't count stopped at zero when overrotating (automatically included)
            if position == 0: #and zeros_passed == 0:
                num_zeros += 1
        
            print(f"- The dial is rotated {line} to point at {position}{'.' if zeros_passed == 0 else f'; during this rotation, it points at 0 {zeros_passed} times.'} {zeros_passed = } {num_zeros = }")

        return num_zeros
    return (rotate_dial_part_two,)


@app.cell
def _(input, rotate_dial_part_two):
    result_part_two = rotate_dial_part_two(50, input, 100)
    result_part_two
    return


if __name__ == "__main__":
    app.run()
