def generate_big_tindex_values(tindex_values, size_of_value):
    big_tindex_values = []
    for value in tindex_values:
        big_tindex_values.extend([value] * size_of_value)
    return big_tindex_values

# Example usage

tindex_values = [1.7,1.75,1.85,1.9] # manully off make multiplcation here by hours_back_to_test * len(tindex_values)
dt_values = [0.0002,0.0003,0.0004,0.0005,0.0006,0.0007,0.0008,0.0009]
hours_back_to_test = 6

size_of_value = len(tindex_values) * hours_back_to_test
big_dt_values = generate_big_tindex_values(dt_values, size_of_value)
print(big_dt_values)
print(len(big_dt_values))
