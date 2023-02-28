import math

n_value_input = input('enter the values to be entered: ')
n_value = eval(n_value_input)

rms_average = 0
harmonic_mean = 0
geometric_mean = 1

mean_range = range(n_value)
for i in mean_range:
    val_input = input(f'enter value: ')
    val = eval(val_input)
    rms_average = rms_average + math.pow(val, 2)
    harmonic_mean = harmonic_mean + 1 / val
    geometric_mean = geometric_mean * val

rms_average = math.sqrt(rms_average / n_value)
harmonic_mean = n_value / harmonic_mean
geometric_mean = math.pow(geometric_mean, 1 / n_value)

rms_rounded = round(rms_average, 3)
harmonic_rounded = round(harmonic_mean, 3)
geometric_rounded = round(geometric_mean, 3)
print(rms_rounded)
print(harmonic_rounded)
print(geometric_rounded)
