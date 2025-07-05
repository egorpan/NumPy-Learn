#genereators are functions that allow declaring function that behaves like iterator, i.e for loop

''''
function that returns a list with numbers from 0 to n
'''
def first_n(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(first_n(100))

print(sum_of_first_n)

''''
generator using yield 
'''

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(100))

print(sum_of_first_n)

# yield can be used to replace return when used in loops