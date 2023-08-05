
import os
from moviepy.editor import VideoFileClip

def reduce_video_size(video_path, output_path, reduced_by):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Get the original video resolution
    original_width, original_height = video_clip.size
    print(f"original_width={original_width}, original_height={original_height}")

    if video_clip.rotation == 90:
        print("vertical video")
        # print(f"video-rotation={video_clip.rotation}, type={type(video_clip.rotation)}")
        resized_clip = video_clip.resize(video_clip.size[::-1])
        resized_clip.rotation = 0
        resized_clip = resized_clip.resize(reduced_by)
    else:
        print("horizontal video")
        resized_clip = video_clip.resize(reduced_by)

    # # Write the resized video clip to the output file
    resized_clip.write_videofile(output_path, codec="libx264")
    
    # Close the video clip
    video_clip.close()


def get_output_file_path(video_path):
    # Get the directory and filename from the video_path
    directory = os.path.dirname(video_path)
    filename = os.path.basename(video_path)

    # Append " - updated" to the filename
    updated_filename = os.path.splitext(filename)[0] + " - updated" + os.path.splitext(filename)[1]

    # Generate the output_path by joining the directory and updated_filename
    output_path = os.path.join(directory, updated_filename)

    return output_path


def get_video_list(folder_path, min_size):
    video_list = []
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.endswith(('.mp4', '.avi', '.mkv')):
            size = os.path.getsize(file_path)
            # print(f"size={size}")
            if size > min_size:
                video_list.append(file_path)
    
    return video_list


# Only one video
# video_path = "D:\\Mobile\\2023-08-05\\US Photos\\5 - Las Vegas\\20230721_210031_1.mp4"
# reduce_video_size(video_path, get_output_file_path(video_path), reduced_by=0.8)


# All videos in a Folder
folder_path = "D:\\Mobile\\2023-08-05\\US Photos\\7 - Chicago"

video_list = get_video_list(folder_path, min_size=10000000)
for video_path in video_list:
    output_path = get_output_file_path(video_path)
    reduce_video_size(video_path, output_path, reduced_by=0.8)
    os.remove(video_path)
