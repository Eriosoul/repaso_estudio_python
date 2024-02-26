import ffmpeg


def trim_video(input_file, output_file, start_time, end_time):
    (
        ffmpeg.input(input_file, ss=start_time)
        .output(output_file, to=end_time)
        .run()
    )


input_file = 'input_video.mp4'
output_file = 'output_video.mp4'
start_time = '00:00:02'
end_time = '00:00:06'

trim_video(input_file, output_file, start_time, end_time)
