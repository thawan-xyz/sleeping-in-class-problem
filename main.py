import sys

input = sys.stdin.readline
print = sys.stdout.write

total_cases = int(input())

for _ in range(total_cases):
    class_periods = int(input())
    sleep_record = [int(x) for x in input().split()]

    modifications_number = 0

    end_condition = False
    while not end_condition:
        sleep_record.sort()

        not_largest_index = 0
        for i in range(len(sleep_record)):
            if sleep_record[i] < sleep_record[-1]:
                not_largest_index = i

        if sleep_record[0] != sleep_record[-1]:
            sleep_record.append(sleep_record.pop(not_largest_index) + sleep_record.pop(0))
            modifications_number += 1
        else:
            end_condition = True

    print(str(modifications_number) + '\n')
