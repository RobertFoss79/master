# Temperature Conversion Problem

# 1. Create a list called temperatures_c that contains the following temperatures in Celsius: 20, 15, 25, 30, 10.

# 2. Print the entire list of temperatures.

# 3. Convert each temperature to Fahrenheit and store the results in a new list called temperatures_f. Use the formula: F = C * 9/5 + 32.

# 4. Print the new list of temperatures in Fahrenheit.

# 5. Find and print the highest temperature in both Celsius and Fahrenheit.

# 6. Sort both lists in ascending order and print the sorted lists.

temperatures_c = [20, 15, 25, 30, 10]
print("Temperatures in Celcuis:", temperatures_c)

temperatures_f = []
for temp_c in temperatures_c:
    temp_f = temp_c * 9/5 + 32
    temperatures_f.append(temp_f)
print("Temperatures in Fehrenheit:", temperatures_f)

max_temp_c = max(temperatures_c)
max_temp_f = max(temperatures_f)
print("Highest temperature in Celcius:", max_temp_c)
print("Highest temperature in Fehrenheit:", max_temp_f)

temperatures_c.sort()
temperatures_f.sort()

print("Temperatures in Celcius:", temperatures_c)
print("Temperatures in Fehrenheit:", temperatures_f)
