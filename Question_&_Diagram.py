# Exercise:
# Upgrading a Spaceship in a Video Game Using the Decorator Design Pattern
# Background:
# In a video game, the spaceship is the central character with basic abilities such as attack,
# defense, and weight.
# Using the Decorator Pattern, you can extend the spaceship's abilities by adding components like shields
# (which increase defense points) and weapons (which increase attack points).
# Each additional component also changes the spaceship's total weight.
#------------------------------------------------------------------------

# Requirements:
# Basic Interface - ISpaceship:
# Create an abstract class named ISpaceship that will include the following methods:

# attack_get(): Returns the spaceship's attack points.
# defense_get(): Returns the defense points.
# weight_get(): Returns the total weight of the spaceship.
# details_get(): Returns a string with a detailed description of the spaceship and the installed components.
#----------------------------------------------------------------------------------------------------------

# Example:
# A basic spaceship (BasicSpaceship) might start with:
#
# Attack: 10 points
# Defense: 50 points
# Weight: 100 units
#----------------------------------------------------

# Base Decorator Class - SpaceshipDecorator:
# Create an abstract class named SpaceshipDecorator that implements ISpaceship and receives an ISpaceship
# object during initialization.
# This class will serve as the base for all decorators and will allow the extension of the spaceship
# object without modifying the basic class.
#-----------------------------------------------------

# Defense Decorators Example:
# ShieldDecorator:
#
# defense_get(): Adds additional defense points (e.g., +10 defense points).
# weight_get(): Adds weight (e.g., +20 units).
# details_get(): Updates the description to include the shield (e.g., "Standard Shield")
#---------------------------------------------------------------------------------------

# Attack Decorators Example:
# WeaponDecorator:
#
# attack_get(): Adds attack points (e.g., +15 for a rifle or +25 for an advanced weapon).
# weight_get(): Adds weight (e.g., +15 units).
# details_get(): Updates the description to include the weapon (e.g., "Laser Rifle").
#==============================================================================================

# Main Code:
# Initialize a basic spaceship object (BasicSpaceship).
# Decorate the spaceship with various decorators (either user-chosen or predetermined).
# Print the final result, including:
# Total attack points
# Total defense points
# Total weight
# Detailed description of the spaceship with all installed components
#===============================================================================================

# DIAGRAM:

#            +-------------------+
#            |    ISpaceship     |  (Abstract Interface)
#            +-------------------+
#             ^            ^
#             |            |
# +----------------+   +---------------------+
# | BasicSpaceship |   | SpaceshipDecorator  |  (Abstract Decorator)
# +----------------+   +---------------------+
#                            ^
#                            |
#              +---------------------------+
#              | ShieldDecorator           |
#              +---------------------------+
#              | WeaponDecorator           |
#              +---------------------------+

