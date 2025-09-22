import array_utils as au

def main():
    print("Array/List Test")
    user_input = input("Sayilari giriniz: ")
    lst = list(map(int, user_input.split()))

    print("Sum:", au.sum_list(lst))
    print("Max:", au.max_list(lst))
    print("Min:", au.min_list(lst))
    print("Average:", au.average_list(lst))

if __name__ == "__main__":
    main()
