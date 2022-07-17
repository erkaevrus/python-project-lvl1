#!/usr/bin/env/ python3
from brain_games.games.check_even import check_even
from brain_games.logics.hello import welcome_user


def main():
    name = welcome_user()
    check_even(name)


if __name__ == '__main__':
    main()
