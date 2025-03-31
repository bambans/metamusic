from types import LambdaType

def is_lambda(obj):
    return isinstance(obj, LambdaType) and obj.__name__ == "<lambda>"
