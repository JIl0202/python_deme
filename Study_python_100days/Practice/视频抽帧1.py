import cv2
import os
import numpy as np
import time

# video所在的根目录
video_base_path = r"E:\DEV"
# processVideo所在根目录
save_base_path = r"E:\DEV"
# 保存抽取的图像帧时所在的根目录
JPEGImage_base_path = "./JPEGImage"

# ******************指定提取图像帧的模式********************* #
# model = 0 以帧间隔提取, model = 1以秒间隔提取
extract_frame_model = 1


def form_single_channel_video(video_name: str, save_name: str, channel: int):
    """
    提取RGB中某通道形成一个单通道图像
    :param video_name: 输入根目录文件夹下video_name,eg. test.mp4
    :param save_name: 输入保存视频的name,eg. protest.mp4
    :param channel: 需要的提取的channel -->(0, 1, 2)
    :return: None
    """
    video_path = os.path.join(video_base_path, video_name)
    save_path = os.path.join(save_base_path, save_name)

    input_video = cv2.VideoCapture(video_path)
    if not input_video.isOpened():
        raise IOError("current video path is not exist!")

    ex = int(input_video.get(cv2.CAP_PROP_FOURCC))
    size = (int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = int(input_video.get(cv2.CAP_PROP_FPS))
    total_frame = input_video.get(cv2.CAP_PROP_FRAME_COUNT)
    # 写入视频的文件路径 opencv的Size参数是(width，height)
    output_video = cv2.VideoWriter(save_path, ex, fps, size, True)
    if not output_video.isOpened():
        raise IOError("no way to open the save path, please restart")

    print("input frame resolution: width=%d  height=%d, fps=%d, the total frame=%d"
          % (size[0], size[1], fps, total_frame))

    while input_video.isOpened():
        ret, frame = input_video.read()
        if not ret:
            break
        (B, G, R) = cv2.split(frame)
        zeros = np.zeros(np.shape(frame)[:2], dtype="uint8")
        output = np.zeros(np.shape(frame), dtype="uint8")
        if channel == 0:
            output = cv2.merge([B, zeros, zeros])
        elif channel == 1:
            output = cv2.merge([zeros, G, zeros])
        else:
            output = cv2.merge([zeros, zeros, R])

        # 将帧写入视频
        output_video.write(output)

        cv2.imshow("frame", frame)
        cv2.imshow("output", output)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    print("clearing up!")
    cv2.destroyAllWindows()
    input_video.release()
    output_video.release()


def plus_shot_video_frame(video_name: str, image_save_path: str = None, frequency: int = 1, second: int = 1):
    """
    根据mode实现的不同形式的抽帧方式，当mode==0，按指定的帧间隔抽帧，mode==1，按指定的秒间隔进行抽帧
    :param video_name: 输入根目录文件夹下的video name,eg. test.mp4
    :param image_save_path: 当为None时默认在video所在文件中创建一个同名一个与video同名的文件中用于保存图像帧，否则输入绝对路径
    :param frequency: 当mode为0时，该参数启用，表示设置的帧间隔
    :param second: 当mode为1时，该参数启用，表示设置的秒间隔
    :return: None
    """
    actual_video_name = video_name.split('.')[0]  # 提取真正的文件夹名称
    if image_save_path is None:
        image_save_path = os.path.join(video_base_path, actual_video_name)

    if not os.path.exists(image_save_path):
        os.makedirs(image_save_path)

    video_path = os.path.join(video_base_path, video_name)
    input_video = cv2.VideoCapture(video_path)
    if not input_video.isOpened():
        raise IOError("current video path is not exist!")

    size = (int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = int(input_video.get(cv2.CAP_PROP_FPS))
    total_frame = input_video.get(cv2.CAP_PROP_FRAME_COUNT)
    print("input frame resolution: width=%d  height=%d, fps=%d, the total frame=%d"
          % (size[0], size[1], fps, total_frame))

    num_frame = 0  # 帧计数
    if extract_frame_model == 0:
        frame_gap = frequency
    else:
        frame_gap = int(second * fps)

    start_time = time.time()  # 时间测算

    # 循环读取每一帧,根据model来确定抽帧模式
    while True:
        try:
            if num_frame >= 88 and (num_frame-frame_gap) % total_frame == 0:
                break
            ret_success, frame = input_video.read()
            if ret_success:
                # frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
                image_name = actual_video_name + '-' + str(round(num_frame / frame_gap)) + '.jpg'
                cv2.imwrite(os.path.join(image_save_path, image_name), frame)
                print("saved " + str(round(num_frame / frame_gap)) + '.jpg')

            else:
                print("extract frame from video fail, current frame={}, current time={}".format(
                    num_frame, 3*num_frame/frame_gap))
                num_frame += frame_gap
                input_video.set(cv2.CAP_PROP_POS_FRAMES, num_frame)  # 隔帧读取
                continue
        except:
            print('time_out')

        num_frame += frame_gap  # 更新帧计数
        input_video.set(cv2.CAP_PROP_POS_FRAMES, num_frame)  # 隔帧读取

    end_time = time.time()
    print("time consuming: {:.2f}second".format(end_time - start_time))
    print("cleaning up!")
    input_video.release()


if __name__ == "__main__":
    video_name = 'CPDM04.MP4'
    plus_shot_video_frame(video_name, second=3)
