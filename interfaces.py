from abc import ABC, abstractmethod


class ISpaceship(ABC):
    @abstractmethod
    def attack_get(self):
        pass

    @abstractmethod
    def defense_get(self):
        pass

    @abstractmethod
    def weight_get(self):
        pass

    @abstractmethod
    def details_get(self):
        pass