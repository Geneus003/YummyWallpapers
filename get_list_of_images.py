import vk_api


def get_images_list(login, password):

    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    feed_list = vk.newsfeed.search(q = "#yummyart #1920x1080", count = 1)
    feed_list = feed_list["items"]

    return feed_list