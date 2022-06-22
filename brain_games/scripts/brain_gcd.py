#!/usr/bin/env python

from brain_games.scripts.games.common import game_launcher
from brain_games.scripts.games.brain_gcd import greatest_common_divider
from brain_games.scripts.games.brain_gcd import game_description


def main():
    game_launcher(greatest_common_divider, game_description)


if __name__ == '__main__':
    main()
