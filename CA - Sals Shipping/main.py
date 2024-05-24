# Shipping.py

"""
shipping Method:
1 -> Ground shipping
2 -> Ground shipping premium
3 -> Drone shipping
"""

# Declare global vars
ground_shipping_flat = 20.00
ground_shipping_premium = 125.00
weight_under_2 = 1.50
weight_2_6 = 3.00
weight_6_10 = 4.00
weight_over_10 = 4.75
premium_multiplier = 3


def calc_ground_premium_cost():
    return ground_shipping_premium


def calc_ground_shipping(weight):
    if weight <= 2:
        return (weight * weight_under_2) + ground_shipping_flat
    elif weight <= 6:
        return (weight * weight_2_6) + ground_shipping_flat
    elif weight <= 10:
        return (weight * weight_6_10) + ground_shipping_flat
    else:
        return (weight * weight_over_10) + ground_shipping_flat


def calc_drone_shipping(weight):
    if weight <= 2:
        return (weight * weight_under_2) * premium_multiplier
    elif weight <= 6:
        return (weight * weight_2_6) * premium_multiplier
    elif weight <= 10:
        return (weight * weight_6_10) * premium_multiplier
    else:
        return (weight * weight_over_10) * premium_multiplier


def calc_shipping_cost(weight, shipping_method):
    if shipping_method == 2:
        return calc_ground_premium_cost()
    elif shipping_method == 1:
        return calc_ground_shipping(weight)
    elif shipping_method == 3:
        return calc_drone_shipping(weight)


"""
ship1 = Ground Shipping
ship2 = Ground Shipping Premium
ship3: Drone Shipping
"""


def find_cheapest_shipping(weight):
    ship1 = calc_shipping_cost(weight, 1)
    ship2 = calc_shipping_cost(weight, 2)
    ship3 = calc_shipping_cost(weight, 3)
    if (ship1 <= ship2) and (ship1 <= ship3):
        #ship1 is cheaper
        return 1
    elif (ship2 <= ship1) and (ship2 <= ship3):
        return 2
    else:
        return 3


def main():


    customer_package_weight = 41.5
    if find_cheapest_shipping(customer_package_weight) == 1:
        print("The cheapest shipping method is: Ground Shipping")
        print("Total price: " + str(calc_shipping_cost(customer_package_weight, 1)))
    elif find_cheapest_shipping(customer_package_weight) == 2:
        print("The cheapest shipping method is: Ground Premium Shipping")
        print("Total price: " + str(calc_shipping_cost(customer_package_weight, 2)))
    else:
        print("The cheapest shipping method is: Drone Shipping")
        print("Total price: " + str(calc_shipping_cost(customer_package_weight, 3)))


    print ("Debug: ")
    print("Ground Shipping: " + str(calc_shipping_cost(customer_package_weight, 1)))
    print("Ground Premium: " + str(calc_shipping_cost(customer_package_weight, 2)))
    print("Drone Shipping: " + str(calc_shipping_cost(customer_package_weight, 3)))

if __name__ == "__main__": main()