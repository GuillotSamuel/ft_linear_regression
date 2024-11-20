import csv
import json

DATAS = "../data/data.csv"
PARAMETERS = "../models/parameters.json"
ITERATIONS = 1000
LEARNING_RATE = 0.01

def read_dataset():
    try:
        mileage = []
        price = []
        with open(DATAS, "r") as file:
            input_file = csv.DictReader(file)
            for row in input_file:
                mileage.append(float(row["km"]))
                price.append(float(row["price"]))
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    return mileage, price


def ft_linear_regression(mileage, price):
    m = len(mileage)
    theta0 = 0
    theta1 = 0
    

    

def update_parameters(theta0, theta1):
    try:
        with open(PARAMETERS, "r") as file:
            data = json.load(file)
        data["theta0"] = theta0
        data["theta1"] = theta1
        with open(PARAMETERS, "w") as file:
            file = json.dump(data, file)
    except Exception as e:
        print(f"An error occured: {e}")
        exit(1)


def main():
    mileage, price = read_dataset()
    theta0, theta1 = ft_linear_regression(mileage, price)
    update_parameters(theta0, theta1)


if __name__ == "__main__":
    main()
