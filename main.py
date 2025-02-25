from basic_spaceship import BasicSpaceship
from decorators import ShieldDecorator, WeaponDecorator

# Initialize a basic spaceship
spaceship = BasicSpaceship()

# Add decorations (upgrades)
spaceship = ShieldDecorator(spaceship)
spaceship = WeaponDecorator(spaceship)
spaceship = ShieldDecorator(spaceship, shield_name="Advanced Shield", defense_bonus=20, weight_addition=30)
spaceship = WeaponDecorator(spaceship, weapon_name="Plasma Cannon", attack_bonus=25, weight_addition=25)

# Print final stats
print("Final Spaceship Configuration:")
print(f"Total Attack Points: {spaceship.attack_get()}")
print(f"Total Defense Points: {spaceship.defense_get()}")
print(f"Total Weight: {spaceship.weight_get()} units")
print(f"Details: {spaceship.details_get()}")