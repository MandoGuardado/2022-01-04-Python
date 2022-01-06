#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for farm in farms:
    print(f'{farm["name"]} has the following animals: ')
    animals = farm["agriculture"]
    for animal in animals:
        print(animal)
    print("\n")
print("\nOur loop had ended.")
