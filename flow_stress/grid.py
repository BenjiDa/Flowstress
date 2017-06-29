


# Working on grids for fugacity calculations. 
# This bit of code defines some pressure, temperature conditions as numpy arrays
# coverts them to a meshgrid. It then vectorizes the fugacity optimizer function to work in each of those cells and 
# plots the resultant array as an image.

t = np.array([723.15, 775, 780, 790])
p = np.array([400000000, 450000000, 500000000, 550000000])
T, P = np.meshgrid(t,p)

fugacity_optimizer_vectorized = np.vectorize(fugacity_optimizer)

result_array = fugacity_optimizer_vectorized(T, P)
print(result_array)

plt.imshow(result_array)
plt.show()



#This builds an array of CS tables for each individual temperature value
CS_array = np.empty((len(t), 10))

def cs_builder(temperature):
    for num, t in enumerate(temperature):
        result = calculate_coefficient_table(t)
        CS_array[num] = result
    return CS_array






