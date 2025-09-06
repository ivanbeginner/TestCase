import inspect
from abc import ABC, abstractmethod
from typing import Any, Dict, Type


class Shape(ABC):
    
    _registry: Dict[int, Type['Shape']] = {}
    def __init_subclass__(cls, **kwargs):
        """Автоматическая регистрация всех подклассов"""

        arg_count = cls._get_expected_arg_count()

        cls._registry[arg_count] = cls

    @classmethod
    def _get_expected_arg_count(cls) -> int:

        init_signature = inspect.signature(cls.__init__)
        parameters = list(init_signature.parameters.keys())
        return len([p for p in parameters if p != 'self'])

    @abstractmethod
    def area(self) -> float:
        pass

    @classmethod
    def create(cls, *args) -> 'Shape':
        
        arg_count = len(args)

        if arg_count not in cls._registry:
            available = list(cls._registry.keys())
            raise ValueError(
                f"No shape registered for {arg_count} arguments. "
                f"Available: {available}"
            )

        shape_class = cls._registry[arg_count]
        return shape_class(*args)

