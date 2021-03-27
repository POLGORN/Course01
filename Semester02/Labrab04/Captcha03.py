'''
Даете капчи, а он переводит его в ряд цифр
'''
def divide(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr = arr[size:]
     arrs.append(arr)
     return arrs


def splt():
    alpha = []
    for i in range(4):
        alpha.append(divide(input(), 2))
    return alpha


def distrib(alpha):
    beta = []
    for i in range(len(alpha[0])):
        for item in alpha:
            beta.append(item[i])
    return beta


def give_me_answer_please(beta, nums):
    gamma = []
    for item in beta:
        for i in range(10):
            if list(nums[i]) == item:
                gamma.append(i)
    return gamma


nums = {
0: ('##', '##', '##', '##'),
1: ('.#', '##', '.#', '.#'),
2: ('##', '.#', '#.', '##'),
3: ('##', '.#', '.#', '##'),
4: ('##', '##', '.#', '.#'),
5: ('##', '#.', '.#','##'),
6: ('.#', '#.', '##','##'),
7: ('##', '.#', '#.', '#.'),
8: ('##', '..', '##', '##'),
9: ('##', '##', '.#', '#.')
}

print(''.join(map(str, give_me_answer_please(divide(distrib(splt()), 4), nums))))
