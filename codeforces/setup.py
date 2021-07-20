"""
Sets up wireframe python file for codeforces submission
For practicing:
    setup.py [-p|--practice] <file_name>
For tournaments:
    setup.py [-t|--tournament] <tournament_name> <number_of_problems>
"""


import os
import sys
import string
import shutil


def main():
    wf = "setup_wireframe.py"
    contest = ('-t', '--contest')
    practice = ('-p', '--practice')

    if sys.argv[1] in practice:
        dir_name = "practice/"
        # test if .py is already file ending / another file ending was is used
        fl_name = sys.argv[2] + ".py"
        shutil.copyfile(wf, dir_name + fl_name)
    elif sys.argv[1] in contest:
        trnmt_name = sys.argv[2].replace(" ", "_") + "/"
        dir_name = "contest/" + trnmt_name
        # only if directory isn't already present
        os.mkdir(dir_name)
        count = int(sys.argv[3])

        for i in range(count):
            fl_name = "problem_" + string.ascii_uppercase[i] + ".py"
            shutil.copyfile(wf, dir_name + fl_name)

        string.ascii_uppercase


if __name__ == "__main__":
    main()