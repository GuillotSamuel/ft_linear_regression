import json


def import_parameters():
    try:
        with open("../models/parameters.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def price_estimation(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)


def main():
    parameters = import_parameters()
    theta0 = parameters["theta0"]
    theta1 = parameters["theta1"]

    while True:
        try:
            mileage = float(input("Enter a mileage : "))
            if mileage < 0:
                print("Mileage can't be a negative number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a valid input (float).")
        except Exception as e:
            print(f"{e}")
            exit(1)
    price = price_estimation(mileage, theta0, theta1)
    if price <= 0:
        print(f"Price estimated : 0")
    else:
    	print(f"Price estimated : {price:.2f}")


if __name__ == "__main__":
    main()
