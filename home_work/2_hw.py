def task_1(a: int, b: float, c: str, d: list, e: bool):
    return a,b,c,d,e
print(task_1.__annotations__)


def task_3(x: int) -> int:
    print("Вот тебе квадрат",x,"=",x**2)


task_3(12)
