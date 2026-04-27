def convolution():
    image = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    kernel = [
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ]

    output = []

    # Convolution (5x5 with 3x3 → 3x3 output)
    for i in range(3):
        row = []
        for j in range(3):
            sum_val = 0
            print(f"\nRegion ({i},{j}) Calculation:")

            for ki in range(3):
                for kj in range(3):
                    val = image[i+ki][j+kj] * kernel[ki][kj]
                    sum_val += val
                    print(f"{image[i+ki][j+kj]}*{kernel[ki][kj]} ", end="")

            print("\nOutput:", sum_val)
            row.append(sum_val)

        output.append(row)

    print("\nFinal Feature Map:")
    for r in output:
        print(r)

convolution()