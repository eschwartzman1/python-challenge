# Dependencies
# ------------------------------------
import csv

# Files to Load and Output
# ------------------------------------
file_to_load = "budget_data_1.csv"
file_to_output = "budget_analysis_1.txt"

# Variables
# ------------------------------------
total_months = 0
total_revenue = 0
prev_revenue = 0
current_revenue = 0
revenue_change_list = []

# Main Process
# ------------------------------------

# Read the CSV
with open(file_to_load) as revenue_data:

  # Loop through each row of the dataset as a Dictionary
  reader = csv.DictReader(revenue_data)

  for row in reader:
    print(row)

    # Take note of the current revenue 
    # Current Revenue = 1154293
    # Current Revenue = 885773
    current_revenue = int(row["Revenue"])

    # Calculate the Change in Revenue
    # Change in Revenue = 1154293 - 0
    # Change in Revenue = 885773 - 1154293
    revenue_change_list.append(current_revenue - prev_revenue)

    # Set the value of the previous revenue
    # Previous Revenue = 1154293
    prev_revenue = current_revenue

    # Tally up the months
    total_months = total_months + 1

    # Tally up the revenue
    total_revenue = total_revenue + int(row["Revenue"])


  print("-----------------")

  # Print the Total Months
  print("Total Months: " + str(total_months))

  # Print the Total Revenue
  print("Total Revenue: $" + str(total_revenue))

  # Print the Greatest Increase
  print("Greatest Increase: $" + str(max(revenue_change_list)))
  greatest_increase = max(revenue_change_list)

  # Print the Greatest Decrease
  print("Greatest Decrease: $" + str(min(revenue_change_list)))
  greatest_decrease = min(revenue_change_list)

  # Print the Average Change
  print("Average Change: $" + str(sum(revenue_change_list) / len(revenue_change_list)))
  average_change = sum(revenue_change_list) / len(revenue_change_list)

  # Write Output
  with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months) + "\n")
    txt_file.write("Total Revenue: $" + str(total_revenue) + "\n")
    txt_file.write("Greatest Increase: $" + str(greatest_increase) + "\n")
    txt_file.write("Greatest Decrease: $" + str(greatest_decrease) + "\n")
    txt_file.write("Average Change: $" + str(average_change) + "\n")
    
