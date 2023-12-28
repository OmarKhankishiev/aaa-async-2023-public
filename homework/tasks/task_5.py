import asyncio
from typing import Coroutine


async def limit_execution_time(
        coro: Coroutine,
        max_execution_time: float) -> None:
    # Функция принимает на вход корутину,
    # которую необходимо запустить, однако иногда она выполняется
    # слишком долго, это время необходимо ограничить
    # переданным на вход количеством секунд.
    #
    # Тест проверяет, что каждая переданная корутина была запущена,
    # и все они завершились за заданное время.
    #
    # YOUR CODE GOES HERE
    sample_task = asyncio.create_task(coro)
    try:
        await asyncio.wait_for(sample_task, timeout=max_execution_time)
    except asyncio.TimeoutError:
        sample_task.cancel()
        await sample_task


async def limit_execution_time_many(
        *coros: Coroutine,
        max_execution_time: float) -> None:
    # Функция эквивалентна limit_execution_time,
    # но корутин на вход приходит несколько.
    #
    # YOUR CODE GOES HERE
    sample_tasks = [asyncio.create_task(coro) for coro in coros]
    try:
        await asyncio.wait(sample_tasks, timeout=max_execution_time)
    except asyncio.TimeoutError:
        pass

    for sample_task in sample_tasks:
        if not sample_task.done():
            sample_task.cancel()
            await sample_task
