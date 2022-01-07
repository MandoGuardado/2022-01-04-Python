#!/usr/bin/env python3


def max_number(first, second, third):
    max_value = first
    if second > max_value:
        max_value = second
    if third > max_value:
        max_value = third
    return max_value


def sum_values(numbers):
    values_sum = 0
    for number in numbers:
        values_sum += number
    return values_sum


def multiply_values(numbers):
    number_result = 1
    for number in numbers:
        number_result *= number

    return number_result


def unique_values(numbers):
    unique_list = []
    for number in numbers:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list


def main():
    result = max_number(125, 35, 55)
    print(result)

    result2 = sum_values([20, 50, 100])
    print(result2)

    result3 = multiply_values([8, 2, 3, -1, 7])
    print(result3)

    result4 = unique_values([1, 2, 3, 3, 3, 3, 4, 5])
    print(result4)


if __name__ == "__main__":
    main()
