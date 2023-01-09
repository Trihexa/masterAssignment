import os
import sys
import json
import sqlite3

from climber import Climber
from mountain import Mountain
from expedition import Expedition


def main():
    with open("expeditions.json") as file:
        data = json.load(file)

        for i in data:
            print(i)


if __name__ == "__main__":
    main()
