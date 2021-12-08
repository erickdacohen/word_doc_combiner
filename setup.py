# Setup.py
import os

folders = ["./data-raw", "./data-output", "./scripts"]

[os.mkdir(dir) for dir in folders if not os.path.isdir(dir)]