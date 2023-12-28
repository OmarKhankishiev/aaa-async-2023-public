from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(
    f: Callable[..., Coroutine[Any, Any, Any]] | Task | Coroutine
) -> Any:
    # На входе одна из стадий жизненного цикла корутины, необходимо
    # вернуть результат её выполнения.

    if isinstance(f, Callable):
        return await f()
    elif isinstance(f, Task):
        return await f
    elif isinstance(f, Coroutine):
        return await f
    else:
        raise ValueError("invalid argument")
