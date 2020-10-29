def BinarySearch(array, lower_range, upper_range, number_to_be_search):
    if upper_range >= lower_range:
        middle = (upper_range + lower_range) // 2

        if array[middle] == number_to_be_search:
            return middle
        elif array[middle] > number_to_be_search:
            return BinarySearch(array, lower_range, middle - 1, number_to_be_search)        
        else:
            return BinarySearch(array, middle + 1, upper_range, number_to_be_search)
    else:
        return -1

length_of_number = int(input("How many number you would like to store in the list: "))
number_list = []
for i in range(0, length_of_number, 1):
    number_list.append(int(input(str(i+1) + " number: ")))
print("Before sorting: ", number_list)
number_list.sort()
print("After sorting: ", number_list)
def play_game():
    flag = True
    while flag:
        number_to_be_search = int(input("Which number you would like to search: "))
        guess = BinarySearch(number_list, 0, len(number_list), number_to_be_search)
        if number_list[guess] == number_to_be_search:
            print("Searching number position ", guess + 1)
            print("\nWould you like to continue: \nPress ENTER\nPress q | Q to exit: ")
            play = input(": ")
            if play == 'q' or play == 'Q':
                flag = False
            else:
                play_game()
        else:
            print("Number does exist")

play_game()
