# def sum_list(*nums):
#     print(nums)
# sum_list(1,3,5,7)

def sum_list(a,*nums):
    print(a)
    print(nums)
sum_list(1,3,5,7)

# def sum_list(msg,*nums):
#     total=0
#     for i in range(0,len(nums)):
#         total = total+nums[i]
#     print(msg)
#     return total
# print(sum_list(("I am doing sum"),1,3,5,7))

# def build_profile(**things):
#     print("Profile:")
#     for i, j in things.items():
#         print(i,j)

# build_profile(name="Sheelendra", city="mathura", age=19)
