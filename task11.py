potential_coefficients_1 = [1, 2.4, 'hello', 15, 70000.1, 0.0001, True, 2+5j]
new_potential_coefficients_1 = [values for values in potential_coefficients_1 if type(values) == int or type(values) == float]

print(new_potential_coefficients_1)

potential_coefficients_2 = [1, 2.4, 'hello', 15, 70000.1, 0.0001, True, 2+5j]
new_potential_coefficients_2 = [values if values < 0.5 or values > 100 else None for values in potential_coefficients_2 if type(values) == int or type(values) == float]

print(new_potential_coefficients_2)
