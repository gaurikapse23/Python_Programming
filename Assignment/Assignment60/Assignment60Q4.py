def weight_update():
    x = 2
    w = 0.5
    bias = 0.5
    y_true = 1
    lr = 0.1  # learning rate

    # Forward pass
    y_pred = (x * w) + bias

    # Loss (MSE)
    loss = (y_true - y_pred) ** 2

    # Gradient
    dL_dw = -2 * x * (y_true - y_pred)

    # Update weight
    new_w = w - lr * dL_dw

    print("Old Weight:", w)
    print("Loss:", loss)
    print("Updated Weight:", new_w)

weight_update()