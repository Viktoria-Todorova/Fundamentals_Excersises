
n = int(input())
positives = []
negatives = []
count_positives = 0
sum_negatives = 0
for i in range(n):
    num = int(input())

    if num >= 0:
        positives.append(num)
        count_positives +=1
    else:
        negatives.append(num)
        sum_negatives += num

print(positives)
print(negatives)
print(f"Count of positives: {count_positives} \nSum of negatives: {sum_negatives}")
