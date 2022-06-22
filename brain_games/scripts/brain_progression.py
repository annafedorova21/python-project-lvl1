#!/usr/bin/env python

from brain_games.scripts.games.common import game_launcher
from brain_games.scripts.games.brain_progression import brain_progression
from brain_games.scripts.games.brain_progression import game_description


def main():
    game_launcher(brain_progression, game_description)


if __name__ == '__main__':
    main()
