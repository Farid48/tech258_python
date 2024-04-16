from random import randint
from poke_req import *

def battle_round(fighter_1: dict, fighter_2: dict, round_count: int) -> None:
    print(f"{'='*40}")
    print(f"{'*'*17}round {round_count}{'*'*16}")
    print(f"{'=' * 40}")
    # Fighter 1 attack
    fighter_1_att = randint(0, fighter_1["attack"])
    fighter_2_def = randint(0, fighter_2["defense"])

    if fighter_1_att > fighter_2_def:
        fighter_2["hp"] -= 1
        print(f"{'-'*10}HIT{'-'*10}")
        print(f"{fighter_1["name"]} damages {fighter_2["name"]} for 1 hp.")
    else:
        print(f"{'-' * 10}BLOCK{'-' * 10}")
        print(f"{fighter_2["name"]} blocks {fighter_1["name"]}'s attack.")
    print(f"{fighter_2["name"]} has {fighter_2["hp"]} hp left.")

    # Fighter 2 attack
    fighter_2_att = randint(0, fighter_2["attack"])
    fighter_1_def = randint(0, fighter_1["defense"])

    if fighter_2_att > fighter_1_def:
        fighter_1["hp"] -= 1
        print(f"{'-' * 10}HIT{'-' * 10}")
        print(f"{fighter_2["name"]} damages {fighter_1["name"]} for 1 hp.")
    else:
        print(f"{'-' * 10}BLOCK{'-' * 10}")
        print(f"{fighter_1["name"]} blocks {fighter_2["name"]}'s attack.")
    print(f"{fighter_1["name"]} has {fighter_1["hp"]} hp left.")


def choose_fighter(player: str) -> dict:
    """Asks the user to choose a pokemon."""

    print(f"{player} choose your pokemon.")
    pokemon = get_pokemon()
    pokemon_stats = get_pokemon_stats(pokemon)
    return pokemon_stats

def choose_fighter_random(player: str) -> dict:
    """Asks the user to choose a pokemon."""

    print(f"{player} choose your pokemon.")
    pokemon = get_random_pokemon()
    pokemon_stats = get_pokemon_stats_random(pokemon)
    return pokemon_stats

def main() -> None:
    print(f"\n{'=' * 60}")
    print(f"{'*' * 20}pokemon battle game{'*' * 21}")
    print(f"{'=' * 60}")

    # Choose a character, then validate the input
    pokemon_1 = choose_fighter("Player 1")
    pokemon_2 = choose_fighter_random("Player 2")

    print(f"Player 1's pokemon is {pokemon_1}")
    print(f"Player 2's pokemon is {pokemon_2}")

    fighter1 = {}
    fighter2 = {}

    # Choose who goes first by comparing speeds.
    if pokemon_1["speed"] >= pokemon_2["speed"]:
        fighter1 = pokemon_1
        fighter2 = pokemon_2
    else:
        fighter1 = pokemon_2
        fighter2 = pokemon_1

    # Game is a series of rounds, taking turns to attack and defend
    round_count = 0
    while fighter1["hp"] > 0 and fighter2["hp"] > 0:
        battle_round(fighter1, fighter2, round_count)
        round_count += 1

        print(f"\n{'='*10}BATTLE END{'='*10}")

    if fighter1["hp"] > 0:
        print(f"{fighter1['name']} WINS!")
    else:
        print(f"{fighter2['name']} WINS!")


if __name__ == "__main__":
    main()