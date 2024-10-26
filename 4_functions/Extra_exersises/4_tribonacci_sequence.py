def tribonacci_seq(num):
    # Initial values of the Tribonacci sequence
    t1, t2, t3 = 1, 1, 2

    if num == 1:
        return [t1]
    elif num == 2:
        return [t1 ,t2]

    sequence = [t1, t2, t3]
    for i in range(3, num ):

        t_next = t1 + t2 + t3  # Calculate the next number in the Tribonacci sequence
        sequence.append(t_next)  # Append to the sequence

        # Update variables for the next iteration
        t1, t2, t3 = t2, t3, t_next
    return sequence

number = int(input())
fibonacci = [int(numbers)for numbers in tribonacci_seq(number)]
print(*fibonacci, sep=" ")