import cv2
import os


def extract_keyframes(input_video_path, output_folder, interval_seconds=3):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(input_video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = fps * interval_seconds

    frame_count = 0
    keyframe_count = 0
    input_video = cap.isOpened()
    while input_video.read():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            keyframe_filename = os.path.join(output_folder, f'keyframe_{keyframe_count}.jpg')
            cv2.imwrite(keyframe_filename, frame)
            print(f'Saved keyframe {keyframe_count}: {keyframe_filename}')
            keyframe_count += 1

        frame_count += 1

    cap.release()


if __name__ == "__main__":
    input_video_path = r'E:\\DEV\CPDM04.mp4'  # 输入视频文件路径
    output_folder = r'E:\videos'  # 保存关键帧的文件夹路径
    interval_seconds = 3  # 每隔多少秒抽取一帧

    extract_keyframes(input_video_path, output_folder, interval_seconds)
