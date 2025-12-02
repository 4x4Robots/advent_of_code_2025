import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    PATH_FILE = "input/input_day_1_example.txt"
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
def rotate_dial(start_position: int, steps: list[str], index: int, num_positions: int = 100) -> int:
    """Rotate the position by the steps at the given index left or right. Return the new position."""
    if index >= len(steps):
        print("Reached end of steps.")
        return start_position

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

    return rotate_dial(position, steps, index + 1, num_positions)


@app.cell
def _(input):
    end_position = rotate_dial(start_position=50, steps=input, index=0, num_positions=100)
    end_position
    return


if __name__ == "__main__":
    app.run()
