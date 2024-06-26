from typing import Any, Dict, Iterator

class ConfigBase:
    def __init__(self, **kwargs: Any) -> None:
        # add the attributes from the class to the instance
        for name, value in self.__class__.__dict__.items():
            if not name.startswith("__") and not callable(value):
                setattr(self, name, value)
        # update instance's attributes
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        # a list containing all attributes of instance in form key = value
        attributes = ', '.join([f'{name}={value!r}' for name, value in self.__dict__.items()])
        return f'{self.__class__.__name__}({attributes})'
    
    def __post__init__(self) -> None:
        pass

    def __iter__(self) -> Iterator:
        return iter(self.__dict__)
    
    def __getitem__(self, key: str) -> Any:
        return self.__dict__[key]
    
    def keys(self) -> Dict[str, Any].keys:
        return self.__dict__.keys()