import threading

def SumList(arr, result):
    result.append(sum(arr))

def ProductList(arr, result):
    prod = 1
    for no in arr:
        prod *= no
    result.append(prod)

def main():
    arr = [1, 2, 3, 4, 5]

    sum_result = []
    prod_result = []

    t1 = threading.Thread(target=SumList, args=(arr, sum_result))
    t2 = threading.Thread(target=ProductList, args=(arr, prod_result))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum_result[0])
    print("Product of elements:", prod_result[0])

if __name__ == "__main__":
    main()
