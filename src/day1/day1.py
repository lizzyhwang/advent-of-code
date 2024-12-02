
# navigate to src/day1
# run with `python3 day1.py`
def main():
  input = open("input.txt", "r")

  # create our lists
  list1 = []
  list2 = []
  for line in input:
    tokens = line.split()
    list1.append(tokens[0])
    list2.append(tokens[1])

  # sort lists  
  list1.sort()
  list2.sort()
  
  # find differences per line
  diff_counter = 0
  for i in range(0,len(list1)): # the lists are the same size
    diff_counter += abs(int(list1[i]) - int(list2[i]))

  # find repetitions of list1 elements in list2
  score_counter = 0
  for i in list1:
    item = int(i)
    score_counter += item * number_of_instances(item, list2)

  print("part 1 solution:", diff_counter)
  print("part 2 solution:", score_counter)


def number_of_instances(key: int, sorted_list: list):
  idx = binary_search(sorted_list, 0, len(sorted_list)-1, key)
  max_idx = len(sorted_list)-1
  if idx == -1:
    return 0
  else:
    counter = 1
    keep_looking = True
    fwd = idx + 1
    back = idx - 1
    while (keep_looking):
      found_one = False
      if fwd < max_idx:
        next_item = int(sorted_list[fwd])
        if next_item == key:
          counter += 1
          fwd += 1
          found_one = True
      if back >= 0:
        prev_item = int(sorted_list[back])
        if prev_item == key:
          counter +=1
          back -= 1
          found_one = True
      if found_one == False:
        keep_looking = False
  return counter

# binary search code from geeks for geeks
# https://www.geeksforgeeks.org/python-program-for-binary-search/
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
      mid = (high + low) // 2
      if int(arr[mid]) == x:
        return mid
      elif int(arr[mid]) > x:
        return binary_search(arr, low, mid - 1, x)
      else:
        return binary_search(arr, mid + 1, high, x)
    else:
      return -1
  
main()
