def num_to_word(num):
    words = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    return words.get(num, 'Invalid input. Please enter a digit from 0 to 9.')


digit = int(input('Enter a digit from 0 to 9: '))
result = num_to_word(digit)
print(result)
