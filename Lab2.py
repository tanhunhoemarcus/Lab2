import statistics
def display_main_menu():

  print("Enter some numbers separated by commas (e.g. 5, 67, 32)\n")
def calc_average(num):

  length = len(num)

  total = 0

  for i in range(0, len(num)):
    total = num[i]+total

  average = total/length

  print("The average is ", average)

def get_user_input():

  print("Enter some values")

  num = input()

  num_split = num.split(", ")

  num_split = list(map(float, num_split))

  print(num_split)

  return num_split

def find_min_max(num_split):

  minimum = min(num_split)

  print("The minimum value is ",minimum)

  maximum = max(num_split)

  print("The maximum value is ",maximum)

  return num_split

def sort_temperature(num_split):

  sortme = sorted(num_split)

  print("Ascending order: ",sortme)

def calc_median_temperature(num_split):

  median = statistics.median(num_split)
  print("The median is: ", median)
def main():

  print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

  num_split = get_user_input()

  calc_average(num_split)

  find_min_max(num_split)

  sort_temperature(num_split)

  calc_median_temperature(num_split)



if __name__ == "__main__":
  main()