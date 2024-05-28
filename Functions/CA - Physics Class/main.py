# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

def f_to_c(f_temp): return (f_temp - 32) * 5/9

def c_to_f(c_temp): return c_temp * (9/5) + 32

def get_force(mass, acceleration): return mass * acceleration

def get_energy(mass, c = 3 * 10 ** 8): return mass * c

def get_work(mass, acceleration, distance): return get_force(mass, acceleration) * distance

f100_in_celsius = f_to_c(100)
#print(f100_in_celsius)

c0_in_fahrenheit = c_to_f(0)
#print(c0_in_fahrenheit)

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies", train_force, "Newtons of force")

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules")

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters")