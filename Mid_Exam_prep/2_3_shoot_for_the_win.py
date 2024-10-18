sequence_of_int = list(map(int, input().split()))
current_target = 0
count_targets = 0

while True:

    indices = input()

    if indices == "End":
        print(f"Shot targets: {count_targets} -> {' '.join(map(str, sequence_of_int))}")
        break
    current_index = int(indices)

    if 0 <= current_index < len(sequence_of_int) and sequence_of_int[current_index] != -1:
        count_targets += 1
        current_target = sequence_of_int[current_index]
        sequence_of_int[current_index] = -1
        for i in range(len(sequence_of_int)):
            if sequence_of_int[i] != -1:
                if sequence_of_int[i] > current_target:
                    sequence_of_int[i] -= current_target
                else:
                    sequence_of_int[i] += current_target








