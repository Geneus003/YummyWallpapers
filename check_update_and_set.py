import os, sys, requests

def download_image_by_url(photo_url):

    p = requests.get(photo_url)
    out = open("/home/geneus/Documents/YummyWallpapers/wallpaper.jpg", "wb")
    out.write(p.content)
    out.close()

    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/geneus/Documents/YummyWallpapers/wallpaper.jpg")


def set_image_to_screen(image_date, file_url):
    print(image_date, file_url)

    wall_info = open("/home/geneus/Documents/YummyWallpapers/last.txt", "w")
    wall_info.write(image_date)
    wall_info.close()

    download_image_by_url(file_url)

def check_for_updates(list_of_last_images):

    # print(list_of_last_images)

    if not(os.path.exists("/home/geneus/Documents/YummyWallpapers/last.txt")):
        wall_info = open("/home/geneus/Documents/YummyWallpapers/last.txt", "w")
        wall_info.close()
        set_image_to_screen()
    else:
        wall_info = open("/home/geneus/Documents/YummyWallpapers/last.txt", "r")
        wall_info = wall_info.read()

        # print(wall_info)
        # print(str(list_of_last_images[0]["date"]))

        print(len(wall_info), len(str(list_of_last_images[0]["date"])))

        # print(list_of_last_images[0]["attachments"][0]["photo"]["sizes"])

        if wall_info != str(list_of_last_images[0]["date"]):

            for i in range(len(list_of_last_images[0]["attachments"][0]["photo"]["sizes"])):
                # print(list_of_last_images[0]["attachments"][0]["photo"]["sizes"][i])
                if list_of_last_images[0]["attachments"][0]["photo"]["sizes"][i]["width"] == 1920:
                    file_url_1920 = list_of_last_images[0]["attachments"][0]["photo"]["sizes"][i]["url"]
                    # print("GOD")

            set_image_to_screen(str(list_of_last_images[0]["date"]), file_url_1920)
        else:
            print("Nothing interesting")
    return