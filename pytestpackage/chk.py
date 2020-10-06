# def test():
#     return 1 / 0
#
#
# test()
# ## ZeroDivisionError: division by zero


# def test():
#     try:
#         return 1/0
#     except Exception as e:
#         raise  e
#
# test()
# # ## ZeroDivisionError: division by zero

# def test():
#     try:
#         return 1/0
#     except Exception as e:
#         print("Exception occured during 0 division")
#
# test()
# Exception occured during 0 division
#
# Process finished with exit code 0



def test():
    try:
        return 1/0
    except Exception as e:
        raise Exception("hello...")
test()