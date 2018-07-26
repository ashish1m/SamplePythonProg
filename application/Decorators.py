def new_decorator(original_func):
    def wrap_func():
        print("Some code before original func.")
        original_func()
        print("Some code after original func.")

    return wrap_func


# Actual syntax below
# @new_decorator
def func_need_decorator():
    print("I want to be decorated!!!")


func_need_decorator()
