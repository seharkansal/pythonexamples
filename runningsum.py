def runningSum(nums):
    for i in range(1,len(nums)):
        nums[i]=nums[i]+nums[i-1]
    return nums
    
    
'''def test():
    nums=[4,5,6]
    assert runningSum(nums)==[4,9,15]
    print("passed")'''


    #test()
nums=[1,2,3,4]
arr_new=[]
arr_new=runningSum(nums)
for i in arr_new:
    print(i)

