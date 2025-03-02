# # 1 - Local Scope

# def wage_bonus(bonus):
#     wage = 2000
#     wage +=bonus

#     return wage

# wage_with_bonus = wage_bonus(500)
# print(wage_with_bonus)


# 2 - Global Scope

wage = 2000

def wage_bonus(bonus):
    global wage
    wage +=bonus

    return wage

wage_with_bonus = wage_bonus(500)
print(wage_with_bonus)