import math
import csv
import json
import matplotlib.pyplot as plt

DATAS = "../data/data.csv"
PARAMETERS = "../models/parameters.json"
ITERATIONS = 1000000
LEARNING_RATE = 0.000001


def read_dataset():
    try:
        mileage = []
        price = []
        with open(DATAS, "r") as file:
            input_file = csv.DictReader(file)
            for row in input_file:
                try:
                    mileage.append(float(row["km"]))
                    price.append(float(row["price"]))
                except ValueError:
                    print(f"Invalid data found: {row}")
                    continue
    except Exception as e:
        print(f"Error: An error occurred: {e}")
        exit(1)
    return mileage, price


def ft_predict_y(mileage, theta0, theta1):
    y_prediction = [theta0 + (mileage[i] * theta1) for i in range(len(mileage))]
    return y_prediction


def ft_mean_absolute_error(price, y_prediction):
    mae = sum(abs(y_prediction[i] - price[i]) for i in range(len(price))) / len(price)
    return mae


def ft_linear_regression(mileage, price):
    theta0 = 0
    theta1 = 0
    losses = []

    for iteration in range(ITERATIONS):
        y_prediction = ft_predict_y(mileage, theta0, theta1)
        gradient_theta0 = sum(y_prediction[i] - price[i] for i in range(len(price))) / len(price)
        gradient_theta1 = sum((y_prediction[i] - price[i]) * mileage[i] for i in range(len(price))) / len(price)

        theta0 -= LEARNING_RATE * gradient_theta0
        theta1 -= LEARNING_RATE * gradient_theta1

        loss = ft_mean_absolute_error(price, y_prediction)
        losses.append(loss)

    return theta0, theta1, losses


def update_parameters(theta0, theta1):
    try:
        try:
            with open(PARAMETERS, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data["theta0"] = theta0
        data["theta1"] = theta1

        with open(PARAMETERS, "w") as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error: An error occurred while updating parameters: {e}")
        exit(1)


def plot_graph_display(mileage, price, theta0, theta1, losses):
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.scatter(mileage, price, color='blue', label='Data points')
    y_prediction = ft_predict_y(mileage, theta0, theta1)
    plt.plot(mileage, y_prediction, color='red', label='Regression line')
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")
    plt.title("Car Price Prediction")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(range(len(losses)), losses, color='green')
    plt.xlabel("Iterations")
    plt.ylabel("Loss (Mean Absolute Error)")
    plt.title("Model Loss Over Time")

    plt.tight_layout()
    plt.savefig("../results/plot_graph.png")


def main():
    mileage, price = read_dataset()
    theta0, theta1, losses = ft_linear_regression(mileage, price)
    update_parameters(theta0, theta1)
    plot_graph_display(mileage, price, theta0, theta1, losses)


if __name__ == "__main__":
    main()
