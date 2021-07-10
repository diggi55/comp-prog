import sys
import shutil


def main():
    try:
        folder_name = sys.argv[1]
        if not folder_name:
            raise ValueError
    except IndexError or ValueError:
        print("No folder name provided as commandline argument!")
        return

    shutil.copytree('archetype', folder_name)


if __name__ == "__main__":
    #base_directory = "/home/miau/pers/programming/rosalind"
    #if os.path.dirname(os.path.realpath(__file__)) != base_directory:
    #    raise RuntimeWarning("Script is not executed in intended directory!")
    main()
