def only_even(number):
   return int(number) % 2 == 0


numbers = input().split()
even_numbers = list(filter(only_even, numbers))
print([int(num) for num in even_numbers])
