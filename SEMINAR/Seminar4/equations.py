def equation(coef: int, deg: int, list1: list) -> str:
    if deg == 0:
        return f"{list1[coef]} = 0"

    else:
        if deg == 1:
            if list1[coef] != 0:
                return f"{list1[coef]}*x + " + equation(coef + 1, deg - 1, list1)
            else:
                return equation(coef + 1, deg - 1, list1)

        elif list1[coef] == 1:
            return f"x^{deg} + " + equation(coef + 1, deg - 1, list1)
        elif list1[coef] == 0:
            return equation(coef + 1, deg - 1, list1)
        else:
            return f"{list1[coef]}*x^{deg} + " + equation(coef + 1, deg - 1, list1)