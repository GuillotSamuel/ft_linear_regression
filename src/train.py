import csv
import json

def read_dataset(data_file):
    try:
        mileage = []
        price = []
            with open(data_file, "r") as file:
                input_file = csv.DictReader(file)
                for row in input_file:
                    mileage.append(float(row["km"]))
                    price.append(float(row["price"]))
    except Exception as e:
        print(f"An error occurred: {e}")
        exit 1
    return mileage, price


def ft_linear_regression(mileage, price):
    m = len(mileage)
    theta0 = 0
    theta1 = 0

    

def update_parameters(parameters_file, theta0, theta1)
    try:
        with open(parameters_file, "r") as file:
            data = json.loads(file)
        data["theta0"] = theta0
        data["theta1"] = theta1
        with open(parameters_file, "w") as file:
            file = json.dumps(data)
    except Exception as e:
        print(f"An error occured: {e}")
        exit 1


def main():
    mileage, price = read_dataset("../data/data.csv")
    theta0, theta1 = ft_linear_regression(mileage, price)
    update_parameters("../models/parameters.json", theta0, theta1)


if __name__ == "__main__":
    main()
