#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: callable) -> callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Initialize Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: Callable = None) -> Union[
      str, bytes, int, float]:
        """Get method"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Get method to return string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Get method to return integer"""
        return self.get(key, int)
