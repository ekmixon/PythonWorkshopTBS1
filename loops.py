def main():
    # Normal for-i loop
    for i in range(5):
        print('Value of i is', i)

    # Looping through an array
    array = ['hello', 'my', 'name', 'is', 'John']
    for word in array:
        print('\t', word)

    # looping through a list
    a_list = ['Peter', 'Maria', 'John']
    for name in a_list:
        print('Hello', name)

    for number in range(10):
        print('Number value', number)
    # unpack nested data
    nested_data_array = [
        ('colors', ['red', 'blue', 'orange', 'yellow']),
        ('animals', ['cow', 'tiger', 'fish', 'dog'])
    ]
    for (identifier, values) in nested_data_array:
        for value in values:
            print(identifier, ':', value)

    # unpack dictionary
    dictionary = {
        'username': 'admin',
        'password': '1234',
        'url': 'localhost:8080'
    }
    for key in dictionary:
        print(key, ':', dictionary.get(key))

    for value in dictionary.values():
        print(value)

    for key, value in dictionary.items():
        print(key, ':', value)

    for entry, value_ in dictionary.items():
        print(entry, ':', value_)


    # inline loops e.g. for filters
    numbers = [1, 2, 3, 4]
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(even_numbers)
    odd_numbers = [x for x in numbers if x % 2 != 0]
    print(odd_numbers)

    # nested inline loops
    letters = ['a', 'b', 'c']
    letters_combined = [n * letter for n in numbers for letter in letters]
    print(letters_combined)


if __name__ == '__main__':
    main()
