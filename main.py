import get_list_of_images
import check_update_and_set


def main():
    vk_login, vk_pass = input().split(" ")

    feed_list = get_list_of_images.get_images_list(vk_login, vk_pass)

    check_update_and_set.check_for_updates(feed_list)



if __name__ == "__main__":
    main()