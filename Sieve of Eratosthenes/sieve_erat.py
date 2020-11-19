def erat(num):
    nums = [i for i in range(2,num+1)]
    for i in nums:
        for j in nums:
            if j%i == 0 and j!=i:
                nums.remove(j)

    return nums
