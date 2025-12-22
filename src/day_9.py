import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import copy
    import math
    import numpy as np
    return (mo,)


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_9_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_9_complete.txt"
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
    input[:25]
    return (read_input,)


@app.cell
def _(path_file, read_input):
    def convert_input_tuple(path_file: str) -> list[tuple[int, int]]:
        input = read_input(path_file)
        red_tiles = [tuple(map(int, line.split(","))) for line in input]
        # (column, row)
        return red_tiles

    def convert_input_point(path_file: str) -> list[Point]:
        tuples = convert_input_tuple(path_file)
        points = [Point(*pos) for pos in tuples]
        return points

    red_tiles = convert_input_point(path_file)
    red_tiles
    return (convert_input_tuple,)


@app.class_definition
# Define helper classes for polygon calculations
# https://blog.jverkamp.com/2025/12/09/aoc-2025-day-9-polygoninator/

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"


@app.cell
def _():
    # Check if two line segments are intersecting
    # https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
    # https://www.geeksforgeeks.org/dsa/check-if-two-given-line-segments-intersect/
    class Line2D:
        def __init__(self, start: Point, end: Point):
            self.start = start
            self.end = end

        def intersects(self, other: Point) -> bool:
            d1 = ((self.end.x - self.start.x) * (other.start.y - self.start.y)
                - (self.end.y - self.start.y) * (other.start.x - self.start.x))
            d2 = ((self.end.x - self.start.x) * (other.end.y - self.start.y)
                - (self.end.y - self.start.y) * (other.end.x - self.start.x))
            d3 = ((other.end.x - other.start.x) * (self.start.y - other.start.y)
                - (other.end.y - other.start.y) * (self.start.x - other.start.x))
            d4 = ((other.end.x - other.start.x) * (self.end.y - other.start.y)
                - (other.end.y - other.start.y) * (self.end.x - other.start.x))

            if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
                return True

            return False

    # basic tests
    def test_intersects():
        # two diagonals
        l1 = Line2D(Point(0, 0), Point(10,10))
        l2 = Line2D(Point(0, 10), Point(10,0))
        assert l1.intersects(l2) == True
        # two parallel lines
        l3 = Line2D(Point(10, 0), Point(20, 10))
        assert l1.intersects(l3) == False
        # two orthogonal lines with gap
        lx = Line2D(Point(0, 0), Point(10, 0))
        lv = Line2D(Point(5, 1), Point(5, 10))
        assert lx.intersects(lv) == False

    test_intersects()
    return


@app.cell
def _():
    def calculate_area(pos1, pos2):
        """Calculate the area between two posistions."""
        delta_x = abs(pos2[0] - pos1[0]) + 1
        delta_y = abs(pos2[1] - pos1[1]) + 1
        area = delta_x * delta_y
        print(f"Calculated area for {pos1} and {pos2} = {area}")
        return area

    assert calculate_area((2, 5), (9, 7)) == 24
    assert calculate_area((7, 1), (11, 7)) == 35
    assert calculate_area((7, 3), (2, 3)) == 6
    assert calculate_area((2, 5), (11, 1)) == 50
    return (calculate_area,)


@app.cell
def _(calculate_area, convert_input_tuple, path_file):
    def find_largest_area(positions: list):
        """calculate the area for all combinations of posistions"""
        max_area = 0
        for i in range(len(positions)):
            for j in range(i, len(positions)):
                area = calculate_area(positions[i], positions[j])

                if area > max_area:
                    max_area = area
        print(f"Found maximum possible area: {max_area}")
        return max_area

    find_largest_area(convert_input_tuple(path_file))  # part 1: 4735222687
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
