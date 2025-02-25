from interfaces import ISpaceship


class SpaceshipDecorator(ISpaceship):
    def __init__(self, spaceship: ISpaceship):
        self._spaceship = spaceship

    def attack_get(self):
        return self._spaceship.attack_get()

    def defense_get(self):
        return self._spaceship.defense_get()

    def weight_get(self):
        return self._spaceship.weight_get()

    def details_get(self):
        return self._spaceship.details_get()


class ShieldDecorator(SpaceshipDecorator):
    def __init__(self, spaceship: ISpaceship, shield_name="Standard Shield", defense_bonus=10, weight_addition=20):
        super().__init__(spaceship)
        self._shield_name = shield_name
        self._defense_bonus = defense_bonus
        self._weight_addition = weight_addition

    def defense_get(self):
        return super().defense_get() + self._defense_bonus

    def weight_get(self):
        return super().weight_get() + self._weight_addition

    def details_get(self):
        return super().details_get() + f", equipped with {self._shield_name}"


class WeaponDecorator(SpaceshipDecorator):
    def __init__(self, spaceship: ISpaceship, weapon_name="Laser Rifle", attack_bonus=15, weight_addition=15):
        super().__init__(spaceship)
        self._weapon_name = weapon_name
        self._attack_bonus = attack_bonus
        self._weight_addition = weight_addition

    def attack_get(self):
        return super().attack_get() + self._attack_bonus

    def weight_get(self):
        return super().weight_get() + self._weight_addition

    def details_get(self):
        return super().details_get() + f", equipped with {self._weapon_name}"