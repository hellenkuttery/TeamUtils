from arithmetic_utils import add, subtract, multiply, divide
from string_utils import reverse_string, uppercase_string, lowercase_string, count_vowels
from array_utils import sum_list, max_list, min_list, average_list
from dict_utils import dict_keys, dict_values, dict_items, dict_merge

def main():
    print("=== Team Utils CLI ===")
    while True:
        print("\nSeçenekler:")
        print("1) Aritmetik")
        print("2) String")
        print("3) Array/List")
        print("4) Dictionary")
        print("5) Çıkış")
        choice = input("Seçiminiz: ")

        if choice == '1':
            a = float(input("Sayı 1: "))
            b = float(input("Sayı 2: "))
            add(a, b)
            subtract(a, b)
            multiply(a, b)
            divide(a, b)

        elif choice == '2':
            s = input("Bir metin girin: ")
            reverse_string(s)
            uppercase_string(s)
            lowercase_string(s)
            count_vowels(s)

        elif choice == '3':
            lst = list(map(float, input("Sayıları boşlukla girin: ").split()))
            sum_list(lst)
            max_list(lst)
            min_list(lst)
            average_list(lst)

        elif choice == '4':
            def parse_dict(s):
                d = {}
                for item in s.split():
                    if ':' in item:
                        k, v = item.split(':')
                        d[k] = v
                return d
            d1 = parse_dict(input("Birinci dict (key:value): "))
            d2 = parse_dict(input("İkinci dict (key:value): "))
            dict_keys(d1)
            dict_values(d1)
            dict_items(d1)
            dict_merge(d1, d2)

        elif choice == '5':
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == '__main__':
    main()