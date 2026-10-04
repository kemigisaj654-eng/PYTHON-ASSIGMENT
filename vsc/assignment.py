def count_above_50(numbers):
    count=0
    for n in numbers:
        if n > 50:
            count +=1
    return count

print(count_above_50([10,20,55,70,30,100]))
        