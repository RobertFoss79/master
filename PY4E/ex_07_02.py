file_name = input("Enter file name: ")
file_handle = open(file_name)
total_sum = 0
line_count = 0
for line in file_handle:
    if line.startswith("X-DSPAM-Confidence:"):
        value = float(line.strip().split(":")[1])
        total_sum += value
        line_count += 1

if line_count > 0:
    average = total_sum / line_count
    print("Average spam confidence:", average)