#!/usr/bin/env python

from brain_games.scripts.games.common import game_launcher
from brain_games.scripts.games.brain_calc import calc, game_description


def main():
    game_launcher(calc, game_description)


if __name__ == '__main__':
    main()
