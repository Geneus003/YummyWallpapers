import os, sys

def set_image_to_screen(image_date, file_url):



def check_for_updates(list_of_last_images):

    print(list_of_last_images)

    if not(os.path.exists("/home/geneus/Documents/YummyWallpapers/last.txt")):
        wall_info = open("/home/geneus/Documents/YummyWallpapers/last.txt", "w")
        wall_info.close()
        set_image_to_screen()
    else:
        wall_info = open("/home/geneus/Documents/YummyWallpapers/last.txt", "r")
        wall_info = wall_info.read()
        wall_info = wall_info[:-1]

        print(wall_info)
        print(str(list_of_last_images[0]["date"]))

        print(len(wall_info), len(str(list_of_last_images[0]["date"])))


        if wall_info != str(list_of_last_images[0]["date"]):
            set_image_to_screen(str(list_of_last_images[0]["date"])
        else:
            print("Nothing interesting")
    return