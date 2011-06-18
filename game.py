#!/usr/bin/env python

from chesslib import board

import os
import sys

# Load a save if it exists

if os.path.exists("state.fen"):
    with open("state.fen") as save:
        game = board.Board(save.read())
else:
    game = board.Board()

# Choose display method
if len(sys.argv) > 1:
    if sys.argv[1] in ('--console', '-c'):
        from chesslib.gui_console import display
        display(game)
        exit(0)
    elif sys.argv[1] in ('--help', '-h'):
        print '''Usage: game.py [OPTION]\n\n\tPlay a game of chess\n\n\tOptions:\n\t -c, --console\tplay in console mode\n\n'''
        exit(0)

try:
    from chesslib.gui_tkinter import display
except ImportError:
    from chesslib.gui_console import display
else:
    display(game)

