import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    PATH_FILE = "input/input_day_1_dummy.txt"
    return (PATH_FILE,)


@app.cell
def _(PATH_FILE):
    with open(PATH_FILE) as f:
        input = f.readlines()

    for line in input:
        print(line)
    return (input,)


@app.cell
def _(input):
    input
    return


if __name__ == "__main__":
    app.run()
