from time import time, sleep

def decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        sleep(1)
        end = time()
        print(f"{end - start} 초")
        return result
    return wrapper

@decorator
def work(age, name):
    return f"이름 : {name}, 연령 : {age}"

result = work('홍길동', 20)
