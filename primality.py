def prime(number):

    if number == 1:
        return True
    elif 1 < number:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    else:
        return False
