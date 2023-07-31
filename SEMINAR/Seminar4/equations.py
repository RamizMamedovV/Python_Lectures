def equation(coef: int, deg: int, nums: list) -> str:
    if deg == 0:
        return f"{nums[coef]} = 0"

    else:
        if deg == 1:
            if nums[coef] != 0:
                return f"{nums[coef]}*x " + equation(coef + 1, deg - 1, nums)
            else:
                return equation(coef + 1, deg - 1, nums)

        elif nums[coef] == 1:
            return f"x^{deg} " + equation(coef + 1, deg - 1, nums)
        elif nums[coef] == 0:
            return equation(coef + 1, deg - 1, nums)
        else:
            return f"{nums[coef]}*x^{deg} " + equation(coef + 1, deg - 1, nums)
        
def format_list(nums: list):
    for i in range(1, len(nums)):
        if nums[i] > 0:
            nums[i] = f"+ {nums[i]}"

# list_2 = [1, 2, 3]
# res_list = [4, 5, 6, 7, 9]
# for a, i in zip(reversed(list_2), reversed(range(len(res_list)))):
#     res_list[i] += a

# print(res_list)