from settings.update_json import time_now


def make_Timetable_text():
    now_kst = time_now()  # 현재시간 받아옴

    data = []

    # 1
    video_play = dict()
    video_play_time = dict()
    video_play["time"] = video_play_time
    video_play_time["year"] = str(now_kst.strftime("%Y"))
    video_play_time["month"] = str(now_kst.strftime("%m"))
    video_play_time["day"] = str(now_kst.strftime("%d"))
    video_play_time["hour"] = str(now_kst.strftime("%H"))
    video_play_time["minute"] = str(now_kst.strftime("%M"))
    video_play_time["second"] = str(now_kst.strftime("%S"))
    video_play["type"] = "video"
    video_play["action"] = "play"
    video_play["title"] = []

    data.append(video_play)

    # 2
    video_stop = dict()
    video_stop_time = dict()
    video_stop["time"] = video_stop_time
    video_stop_time["year"] = str(now_kst.strftime("%Y"))
    video_stop_time["month"] = str(now_kst.strftime("%m"))
    video_stop_time["day"] = str(now_kst.strftime("%d"))
    video_stop_time["hour"] = str(now_kst.strftime("%H"))
    video_stop_time["minute"] = str(now_kst.strftime("%M"))
    video_stop_time["second"] = str(now_kst.strftime("%S"))
    video_stop["type"] = "video"
    video_stop["action"] = "stop"

    data.append(video_stop)

    # 3
    img_play = dict()
    img_play_time = dict()
    img_play["time"] = img_play_time
    img_play_time["year"] = str(now_kst.strftime("%Y"))
    img_play_time["month"] = str(now_kst.strftime("%m"))
    img_play_time["day"] = str(now_kst.strftime("%d"))
    img_play_time["hour"] = str(now_kst.strftime("%H"))
    img_play_time["minute"] = str(now_kst.strftime("%M"))
    img_play_time["second"] = str(now_kst.strftime("%S"))
    img_play["type"] = "image"
    img_play["action"] = "play"
    img_play["play_time"] = "-1"
    img_play["title"] = ""

    data.append(img_play)

    # 4
    img_stop = dict()
    img_stop_time = dict()
    img_stop["time"] = img_stop_time
    img_stop_time["year"] = str(now_kst.strftime("%Y"))
    img_stop_time["month"] = str(now_kst.strftime("%m"))
    img_stop_time["day"] = str(now_kst.strftime("%d"))
    img_stop_time["hour"] = str(now_kst.strftime("%H"))
    img_stop_time["minute"] = str(now_kst.strftime("%M"))
    img_stop_time["second"] = str(now_kst.strftime("%S"))
    img_stop["type"] = "image"
    img_stop["action"] = "stop"
    img_stop["title"] = ""

    data.append(img_stop)

    # 5
    text_play = dict()
    text_play_time = dict()
    detail_info = dict()
    text_play["time"] = text_play_time
    text_play["detail_info"] = detail_info
    text_play_time["year"] = str(now_kst.strftime("%Y"))
    text_play_time["month"] = str(now_kst.strftime("%m"))
    text_play_time["day"] = str(now_kst.strftime("%d"))
    text_play_time["hour"] = str(now_kst.strftime("%H"))
    text_play_time["minute"] = str(now_kst.strftime("%M"))
    text_play_time["second"] = str(now_kst.strftime("%S"))
    text_play["type"] = "string"
    text_play["play_time"] = "-1"
    text_play["action"] = "play"
    text_play["title"] = ""
    detail_info["x"] = "0"
    detail_info["y"] = "0"
    detail_info["width"] = "0"
    detail_info["height"] = "0"
    detail_info["scroll_fix"] = "0"
    detail_info["play_count"] = "0"
    detail_info["play_second"] = "0"
    detail_info["font_name"] = "NotoSansCJK-Regular.ttc"
    detail_info["font_size"] = "64"
    detail_info["thickness_italics"] = "0"
    detail_info["red_green_blue"] = ["0", "0", "0"]

    data.append(text_play)

    # 6
    text_stop = dict()
    text_stop_time = dict()
    text_stop["time"] = text_stop_time
    text_stop_time["year"] = str(now_kst.strftime("%Y"))
    text_stop_time["month"] = str(now_kst.strftime("%m"))
    text_stop_time["day"] = str(now_kst.strftime("%d"))
    text_stop_time["hour"] = str(now_kst.strftime("%H"))
    text_stop_time["minute"] = str(now_kst.strftime("%M"))
    text_stop_time["second"] = str(now_kst.strftime("%S"))
    text_stop["type"] = "string"
    text_stop["action"] = "stop"

    data.append(text_stop)

    return data





