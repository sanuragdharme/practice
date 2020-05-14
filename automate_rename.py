# Replacing "Zip-Anime.xyz OP (480p) Sub Eng EP 601" to "One Piece - 601.
# If already available in that format it will print message"

import os


def rename_file(folder_path):
    try:
        os.chdir(folder_path)

        for i in os.listdir():
            f_file, f_ext = os.path.splitext(i)
            f_list = list()
            f_title = "One Piece"
            f_episode = ""

            if i.find("Watch") > 1:
                # Here I only want to use 1st part of split and ignore 2nd. So to do that we can use _
                f_content, _ = f_file.split("Watch")
                f_list = f_content.split(" ")
            else:
                f_match = f_title + " - "
                if f_file.startswith(f_match):
                    print("File is already available in that format!")
                else:
                    f_list = f_file.split(" ")

            for j in range(len(f_list)):
                if f_list[j].isdigit():
                    f_episode = f_list[j].strip().zfill(3)

            if len(f_episode) > 1:
                new_name = "{} - {}{}".format(f_title, f_episode, f_ext)
                os.rename(i, new_name)
    except FileNotFoundError:
        print("The system cannot find the file specified: {}".format(folder_path))


rename_file("E:\one piece\Season 6 (2003 - 2004)")
