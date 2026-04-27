def relu_and_pooling():
    feature_map = [
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ]

    # ReLU
    relu_output = []
    for row in feature_map:
        relu_row = []
        for val in row:
            relu_row.append(max(0, val))
        relu_output.append(relu_row)

    print("ReLU Output:")
    for r in relu_output:
        print(r)

    # Max Pooling (2x2)
    pooled = []
    for i in range(0, 2, 2):
        row = []
        for j in range(0, 2, 2):
            pool = [
                relu_output[i][j],
                relu_output[i][j+1],
                relu_output[i+1][j],
                relu_output[i+1][j+1]
            ]
            row.append(max(pool))
        pooled.append(row)

    print("\nMax Pooling Output:")
    for r in pooled:
        print(r)

relu_and_pooling()