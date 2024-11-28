import math
import csv
import json
import matplotlib.pyplot as plt
import numpy as np

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
                if not row["km"].isdigit() or not row["price"].isdigit():
                    print(f"Invalid data found: {row}")
                    continue
                mileage.append(float(row["km"]))
                price.append(float(row["price"]))
    except Exception as e:
        print(f"Error: An error occurred: {e}")
        exit(1)
    return mileage, price


def ft_standard_deviation(mileage):
    average = sum(mileage) / len(mileage)
    squared_sum = sum((x - average) ** 2 for x in mileage)

    standard_deviation = math.sqrt(squared_sum / len(mileage))

    return standard_deviation


def ft_standardise_data(mileage):
    average = sum(mileage) / len(mileage)
    standard_deviation = ft_standard_deviation(mileage)

    mileage_standardized = [(x - average) / standard_deviation for x in mileage]

    return mileage_standardized


def ft_predict_y(mileage_std, theta0, theta1):
    length = len(mileage_std)
    y_prediction = [0] * length

    for i in range(length):
        y_prediction[i] = theta0 + (mileage_std[i] * theta1)

    return y_prediction


def ft_mean_absolute_error(price, y_prediction):
    mae = 0
    length = len(price)

    for i in range(length):
        mae += abs(y_prediction[i] - price[i]) / length

    return mae


def ft_linear_regression(mileage_std, price):
    theta0 = 0
    theta1_std = 0
    losses = []

    std_dev = ft_standard_deviation(mileage_std)

    for iteration in range(ITERATIONS):
        y_prediction = ft_predict_y(mileage_std, theta0, theta1_std)
        gradient_theta0 = sum(y_prediction[i] - price[i] for i in range(len(price))) / len(price)
        gradient_theta1 = sum((y_prediction[i] - price[i]) * mileage_std[i] for i in range(len(price))) / len(price)

        theta0 -= LEARNING_RATE * gradient_theta0
        theta1_std -= LEARNING_RATE * gradient_theta1

        loss = ft_mean_absolute_error(price, y_prediction)
        losses.append(loss)

        # if (iteration % 1000 == 0):
        # print(f"Iteration {iteration} :")
        # print(f"y_prediction : {y_prediction}")
        # print(f"gradient_theta0 : {gradient_theta0}")
        # print(f"gradient_theta1 : {gradient_theta1}")
        # print(f"theta0 : {theta0}")
        # print(f"theta1 : {theta1}\n")

    theta1 = theta1_std * std_dev
    print(f"theta1 : {theta1}, theta1_std: {theta1_std}")

    return theta0, theta1_std, losses, theta1


def update_parameters(theta0, theta1):
    try:
        with open(PARAMETERS, "r") as file:
            data = json.load(file)
        data["theta0"] = theta0
        data["theta1"] = theta1
        with open(PARAMETERS, "w") as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error: An error occurred while updating parameters: {e}")
        exit(1)


def plot_graph_display(mileage, price, theta0, theta1_std, losses):
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.scatter(mileage, price, color='blue', label='Data points')
    
    mileage_std = ft_standardise_data(mileage)
    y_prediction = ft_predict_y(mileage_std, theta0, theta1_std)
    
    plt.plot(mileage, y_prediction, color='red', label='Regression line')
    plt.xlabel("Mileage (Standardized)")
    plt.ylabel("Price")
    plt.title("Car Price Prediction")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(range(len(losses)), losses, color='green')
    plt.xlabel("Iterations")
    plt.ylabel("Loss (Mean Absolute Error)")
    plt.title("Model Loss Over Time")

    plt.tight_layout()
    plt.savefig("../results/plot_graph.png")


def predict_price(theta0, theta1_std):
    try:        
        # Demander un kilométrage
        km_input = input("Veuillez entrer le kilométrage du véhicule : ")
        if not km_input.isdigit():
            print("Erreur : Le kilométrage doit être un nombre entier.")
            return
        mileage = float(km_input)
        
        # Charger les données pour calculer la moyenne et l'écart-type
        mileage_data, _ = read_dataset()
        average = sum(mileage_data) / len(mileage_data)
        std_dev = ft_standard_deviation(mileage_data)

        # Standardiser le kilométrage entré
        mileage_std = (mileage - average) / std_dev

        # Prédire le prix
        predicted_price = theta0 + theta1_std * mileage_std
        if predicted_price <= 0:
            print(f"Le prix prédit pour un véhicule avec {mileage:.2f} km est de 0 euros.")
        else:
            print(f"Le prix prédit pour un véhicule avec {mileage:.2f} km est de {predicted_price:.2f} euros.")
    except Exception as e:
        print(f"Erreur : Une erreur s'est produite lors de la prédiction : {e}")


def main():
    mileage, price = read_dataset()
    mileage_std = ft_standardise_data(mileage)
    theta0, theta1_std, losses, theta1 = ft_linear_regression(mileage_std, price)
    update_parameters(theta0, theta1)
    plot_graph_display(mileage, price, theta0, theta1_std, losses)
    predict_price(theta0, theta1_std)

if __name__ == "__main__":
    main()
