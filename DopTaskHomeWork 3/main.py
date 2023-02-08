import random
def create_equation() -> dict:
    degree = int(input("Введите максимальную степень: "))
    equation = {}
    for n in range(degree, -1, -1):
        equation[n] = random.randint(-5, 5)
    return equation

dict_eq_1 = create_equation()
dict_eq_2 = create_equation()
def dict_to_str(equation: dict) -> str:
    new_eq = ""
    for degree, koef in equation.items():
        if koef != 0:
            new_eq += f"{koef}*x**{degree} + "
    if new_eq.startswith("1") or new_eq.startswith("-1"):
        new_eq = new_eq.replace("1*", "")
    return new_eq.replace("+ -", "- ").\
            replace("x**1 ", "x ").\
            replace("*x**0", "").\
            replace(" 1*x", " x")[:-2] + "= 0"


def str_to_dict(equation: str) -> dict:
    new_eq = equation.replace(" ", "")[:-2].\
        replace("+", " ").replace("-", " -"). \
        replace("*x ", "*x**1 ").replace(" x ", " 1*x**1"). \
        replace(" -x ", " -1x**1 ").split()
    new_dict_eq = {}
    for item in new_eq:
        if "x**" in item:
            if item.startswith("x") or item.startswith("-x"):
                new_item = item.split("x**")
                new_dict_eq[int(new_item[1])] = -1 if new_item[0] == "-" else 1
            elif "*x**" in item:
                new_item = item.split("*x**")
                new_dict_eq[int(new_item[1])] = int(new_item[0])
        else:
            new_dict_eq[int(new_item[0])] = int(item)
    return new_dict_eq

def summ_dict(first: dict, second: dict) -> dict:
    final_dict = {}
    final_dict.update(first)
    final_dict.update(second)
    for degree in final_dict:
        final_dict[degree] = first.get(degree, 0) + second.get(degree, 0)
    return final_dict

print(dict_to_str(dict_eq_1))
print(dict_to_str(dict_eq_2))
final = summ_dict(dict_eq_1, dict_eq_2)
print(dict_to_str(final))