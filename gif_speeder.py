import os
from PIL import Image, ImageSequence

# 디렉터리 경로 재설정
# input_dir = "~/code/image/"


home = os.path.expanduser("~")
input_dir = os.path.join(home, "code", "image")  # WSL 내부에서 실행할 경우만 사용 가능


# 모든 gif 파일 필터링
gif_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".gif")]

# 각 gif 파일을 2배속 처리
for filename in gif_files:
    input_path = os.path.join(input_dir, filename)

    try:
        with Image.open(input_path) as im:
            frames = []
            durations = []

            for frame in ImageSequence.Iterator(im):
                frames.append(frame.copy())
                duration = frame.info.get("duration", 100)
                durations.append(max(1, duration // 2))  # 2배속

            frames[0].save(
                input_path,
                save_all=True,
                append_images=frames[1:],
                duration=durations,
                loop=0
            )
    except Exception as e:
        print(f"Error processing {filename}: {e}")

gif_files

