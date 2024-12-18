import os
import math
import csv
import json
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


DATAS = "../data/data.csv"
PARAMETERS = "../models/parameters.json"
PARAMETERS_DIR = "../models"
RESULTS_DIR = "../results"
ITERATIONS = 1000
LEARNING_RATE = 0.1


def read_dataset():
    try:
        mileage = []
        price = []
        with open(DATAS, "r") as file:
            input_file = csv.DictReader(file)
            for row in input_file:
                if not row["km"].isdigit() or not row["price"].isdigit():
                    print(f"Invalid data found: {row}")
                    continue
                mileage.append(float(row["km"]))
                price.append(float(row["price"]))
    except Exception as e:
        print(f"Error: An error occurred: {e}")
        exit(1)
    return mileage, price


def ft_normalize_data(mileage): # Scaling to range Normalisation
    max_value = max(mileage)
    
    mileage_normalized = [x / max_value for x in mileage]
    
    return mileage_normalized


def ft_predict_y(mileage_norm, theta0, theta1):
    length = len(mileage_norm)
    y_prediction = [0] * length

    for i in range(length):
        y_prediction[i] = theta0 + (mileage_norm[i] * theta1)

    return y_prediction


def ft_mean_absolute_error(price, y_prediction):
    mae = 0
    length = len(price)

    for i in range(length):
        mae += abs(y_prediction[i] - price[i]) / length

    return mae


def ft_linear_regression(mileage_norm, mileage, price):
    theta0 = 0
    theta1 = 0
    losses = []
    length = len(price)

    for iteration in range(ITERATIONS):
        y_prediction = ft_predict_y(mileage_norm, theta0, theta1)
        gradient_theta0 = sum(y_prediction[i] - price[i] for i in range(length)) / length
        gradient_theta1 = sum((y_prediction[i] - price[i]) * mileage_norm[i] for i in range(length)) / length

        theta0 -= LEARNING_RATE * gradient_theta0
        theta1 -= LEARNING_RATE * gradient_theta1

        loss = ft_mean_absolute_error(price, y_prediction)
        losses.append(loss)

    theta1 /= max(mileage)

    return theta0, theta1, losses


def update_parameters(theta0, theta1):
    try:
        if not os.path.exists(PARAMETERS_DIR):
            os.makedirs(PARAMETERS_DIR)
        if not os.path.exists(PARAMETERS):
            data = {"theta0": 0, "theta1": 0}
        else:
            with open(PARAMETERS, "r") as file:
                data = json.load(file)
        data["theta0"] = theta0
        data["theta1"] = theta1
        with open(PARAMETERS, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: An error occurred while updating parameters: {e}")
        exit(1)


def plot_graph_display(mileage, price, theta0, theta1, losses):
    mpl.rcParams['axes.facecolor'] = '#1e1e1e'
    mpl.rcParams['figure.facecolor'] = '#121212'
    mpl.rcParams['grid.color'] = '#444444'
    mpl.rcParams['text.color'] = '#e0e0e0'
    mpl.rcParams['axes.labelcolor'] = '#e0e0e0'
    mpl.rcParams['axes.edgecolor'] = '#e0e0e0'
    mpl.rcParams['xtick.color'] = '#e0e0e0'
    mpl.rcParams['ytick.color'] = '#e0e0e0'

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.scatter(mileage, price, color='#1f77b4', label='Data points')

    y_prediction = ft_predict_y(mileage, theta0, theta1)
    
    plt.plot(mileage, y_prediction, color='#ff7f0e', label='Regression line')
    plt.xlabel("Mileage (Normalized)")
    plt.ylabel("Price")
    plt.title("Car Price Prediction", fontsize=14)
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(range(len(losses)), losses, color='#2ca02c')
    plt.xlabel("Iterations")
    plt.ylabel("Loss (Mean Absolute Error)")
    plt.title("Model Loss Over Time", fontsize=14)
    plt.grid(True)

    plt.tight_layout()

    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    plt.savefig("../results/plot_graph.png")


def get_params():
    global LEARNING_RATE, ITERATIONS

    while True:
        try:
            learning_rate_input = input("\nEnter a learning rate (optional) : ")
            if learning_rate_input:
                learning_rate = float(learning_rate_input)
                if learning_rate <= 0 or learning_rate > 1:
                    print("Learning rate must be greater than 0.")
                    continue
                LEARNING_RATE = learning_rate
            iterations_input = input("Enter a number of iterations (optional) : ")
            if iterations_input:
                iterations = int(iterations_input)
                if iterations <= 0:
                    print("Iterations must be greater than 0.")
                    continue
                ITERATIONS = iterations
            break
        except ValueError:
            print("Invalid input, please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break


def main():
    get_params()
    print(f"\nLearning rate : {LEARNING_RATE}\niterations : {ITERATIONS}\n")
    mileage, price = read_dataset()
    mileage_norm = ft_normalize_data(mileage)
    theta0, theta1, losses = ft_linear_regression(mileage_norm, mileage, price)
    update_parameters(theta0, theta1)
    plot_graph_display(mileage, price, theta0, theta1, losses)


if __name__ == "__main__":
    main()
