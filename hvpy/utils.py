from typing import Any, Callable

__all__ = ["add_shared_docstring"]


def add_shared_docstring(input_class) -> Callable[[Any], Any]:
    def decorator(func):
        split_doc = input_class.__doc__.split("{Shared}")
        func.__doc__ = func.__doc__.replace("{Insert}", split_doc[1])
        input_class.__doc__ = input_class.__doc__.replace("{Shared}", "")
        return func

    return decorator
