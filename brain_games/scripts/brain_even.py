#!/usr/bin/env python

from brain_games.scripts.games.common import game_launcher
from brain_games.scripts.games.brain_even import even_or_not, game_description


def main():
    game_launcher(even_or_not, game_description)


if __name__ == '__main__':
    main()
