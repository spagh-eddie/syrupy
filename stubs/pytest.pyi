from typing import (
    Any,
    Callable,
    TypeVar,
)

ReturnType = TypeVar("ReturnType")

def hookimpl(tryfirst: bool) -> Callable[..., Any]: ...
def fixture(func: Callable[..., ReturnType]) -> Callable[..., ReturnType]: ...

class Function: ...
class Item: ...
