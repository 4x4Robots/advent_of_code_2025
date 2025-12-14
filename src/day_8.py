import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import copy
    import math
    import numpy as np
    return math, mo


@app.cell
def _():
    PATH_FILE_EXAMPLE = "input/input_day_8_example.txt"
    PATH_FILE_COMPLETE = "input/input_day_8_complete.txt"
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
    def convert_to_coordinate(line: str) -> (int, int, int):
        return tuple(map(int, line.split(",", 3)))

    def read_input_coordinates(path_file):
        input = read_input(path_file)
        coordinates = [convert_to_coordinate(line) for line in input]
        return coordinates

    coordinates = read_input_coordinates(path_file)
    coordinates[:3]
    return coordinates, read_input_coordinates


@app.cell
def _(math, path_file, read_input_coordinates):
    def calc_distance(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

    def calculate_distances(coordinates):
        distances = [[-1.0 for i in range(len(coordinates))] for j in range(len(coordinates))]
        #print(distances)
        for row in range(len(coordinates)):
            for column in range(row, len(coordinates)):
                distances[row][column] = calc_distance(coordinates[row], coordinates[column])

        #for row in distances:
        #    print(row)
        return distances

    calculate_distances(read_input_coordinates(path_file))
    return (calculate_distances,)


@app.cell
def _(calculate_distances, coordinates, path_file, read_input_coordinates):
    def find_minimum_distance(distances) -> (int, int):
        """Find which two junctions boxes have the minimal distance between each other."""
        min_row = 1
        min_col = 0
        min_distance = float("+inf")
        for row in range(len(distances)):
            for col in range(row, len(distances)):
                if distances[row][col] > 0.0 and distances[row][col] < min_distance:
                    min_row = row
                    min_col = col
                    min_distance = distances[row][col]
        return min_row, min_col, min_distance

    min_row, min_col, min_distance = find_minimum_distance(calculate_distances(read_input_coordinates(path_file)))
    ({min_row: coordinates[min_row], min_col: coordinates[min_col]}, min_distance)
    return (find_minimum_distance,)


@app.cell
def _(
    calculate_distances,
    find_minimum_distance,
    path_file,
    read_input_coordinates,
    ui_switch_complete_file,
):
    def index_to_str(coordinates, node_index: int) -> str:
        return f"{coordinates[node_index]}"

    def connect_circuits(path_file: str, number_of_connections: int):
        print(f"Looking for {number_of_connections} connections.")
        coordinates = read_input_coordinates(path_file)
        distances = calculate_distances(coordinates)

        connections = []
        for i in range(number_of_connections):
            node_1, node_2, min_distance = find_minimum_distance(distances)
            # set distances to already connected
            distances[node_1][node_2] = -1.0
            distances[node_2][node_1] = -1.0
            # add connections
            connections.append((node_1, node_2))
            print(f"Adding connection between node {node_1} and node {node_2} with distance {min_distance}.")
            print(f"- Connecting {index_to_str(coordinates, node_1)} and {index_to_str(coordinates, node_2)}")
        print(f"Connections: {connections}")
    
        # combine to circuits
        circuits: list[list[int]] = []
        for connection in connections:
            matching_circuits: list[int] = []
            # find alle circuits which are aprt of this connection
            for idx_circuit, circuit in enumerate(circuits):
                if connection[0] in circuit or connection[1] in circuit:
                    matching_circuits.append(idx_circuit)

            # no matching circuit -> create a new circuit
            if len(matching_circuits) == 0:
                print(f"Creating new circuit with nodes {connection}.")
                circuits.append([connection[0], connection[1]])

            # only part of one circuit
            if len(matching_circuits) == 1:
                current_circuit = circuits[matching_circuits[0]]
                if connection[0] in current_circuit and connection[1] not in current_circuit:
                    print(f"Adding node {connection[1]} to circuit: {current_circuit}")
                    current_circuit.append(connection[1])
                elif connection[1] in current_circuit and connection[0] not in current_circuit:
                    print(f"Adding node {connection[0]} to circuit: {current_circuit}")
                    current_circuit.append(connection[0])

            # part of multiple circuits -> consolidate circuits
            if len(matching_circuits) > 1:
                consolidated_circuit = []
                for idx_matching_circuit in matching_circuits:
                    current_circuit = circuits.pop(idx_matching_circuit)
                    for node in current_circuit:
                        if node not in consolidated_circuit:
                            print(f"Consolidating node {node} to circuit: {consolidated_circuit}")
                            consolidated_circuit.append(node)
                        
                circuits.append(consolidated_circuit)

        circuits = sorted(circuits, key=len, reverse=True)

        result = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
            
        return circuits, result
                


    connect_circuits(path_file, number_of_connections=1000 if ui_switch_complete_file.value else 10)
    return


@app.cell
def _(mo):
    ui_switch_complete_file = mo.ui.switch(label="Use complete file", value=True)
    ui_switch_part_two = mo.ui.switch(label="Part 2", value=True)
    mo.hstack([ui_switch_complete_file, ui_switch_part_two])
    return ui_switch_complete_file, ui_switch_part_two


if __name__ == "__main__":
    app.run()
