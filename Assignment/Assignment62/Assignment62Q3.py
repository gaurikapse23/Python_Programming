def flattening():
    matrix = [
        [6, 4],
        [8, 6]
    ]

    flatten_output = []

    for row in matrix:
        for val in row:
            flatten_output.append(val)

    print("Flatten Output:", flatten_output)

flattening()