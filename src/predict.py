import json

MIN = 22899
MAX = 240000


def import_parameters():
    try:
        with open("../models/parameters.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def price_estimation(mileage, theta0, theta1):
    real_mileage = (mileage - MIN) / (MAX - MIN) 
    return theta0 + (theta1 * real_mileage)


def main():
    parameters = import_parameters()
    theta0 = parameters["theta0"]
    theta1 = parameters["theta1"]

    while True:
        try:
            mileage = float(input("Enter a mileage : "))
            if mileage < 0:
                raise Exception("Mileage can't be a negative number.")
            break
        except ValueError:
            print("Invalid input, please enter a valid input (float).")
        except Exception as e:
            print(f"{e}")
            exit(1)
    price = int(price_estimation(mileage, theta0, theta1))
    if price <= 0:
        print(f"Price estimated : 0")
    else:
    	print(f"Price estimated : {price}")


if __name__ == "__main__":
    main()

# # TEST CODE
# import json
# import sys

# def get_thetas_values() :
# 	try:
# 		with open("../models/parameters.json", "r") as read_file:
# 			data = json.load(read_file)
# 	except:
# 		sys.exit(-1)
# 	return data["theta0"], data["theta1"]

# def price_estimation() :
# 	theta0, theta1 = get_thetas_values()
# 	while(1):
# 		s = input("Wich mileage is on your car ? ")
# 		if not s:
# 			print('\nPlease enter a value')
# 		else:
# 			break
# 	try:
# 		assert(all([c in '-0123456789' for c in s]))
# 	except:
# 		print('\nPlease use a valid litteral value for int() with base 10.')
# 		sys.exit(-1)
# 	km_input = float(s)
# 	if km_input < 0:
# 		print("\nA mileage under 0 ?\n.\n.\n.\nReally ?")
# 		sys.exit(-1)
# 	if km_input >= 409764:
# 		print("\nYour price car is estimated at 0 euros or under.. You should not sell it.")
# 		sys.exit(-1)
# 	km = (km_input - 22899) / (240000 - 22899)
# 	price = theta0 + km * theta1
# 	print("\nYour price car is estimated at " + str(int(price)) + " euros.")


# if __name__ == '__main__' :
# 	price_estimation()
 