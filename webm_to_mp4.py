import argparse
import subprocess
import os
import sys


def convert_webm_to_mp4(input_file, output_file=None, speed=1.0):
    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}")
        sys.exit(1)

    if not input_file.endswith(".webm"):
        print("Input file must be .webm")
        sys.exit(1)

    # Default output name
    if output_file is None:
        output_file = input_file.replace(".webm", ".mp4")

    # Video speed filter + ensure even dimensions for libx264 (yuv420p)
    video_filter = f"setpts={1/speed}*PTS,pad=ceil(iw/2)*2:ceil(ih/2)*2"

    # Audio speed filter (must stay in 0.5–2.0 range per step)
    audio_filters = []
    remaining_speed = speed

    while remaining_speed > 2.0:
        audio_filters.append("atempo=2.0")
        remaining_speed /= 2.0

    while remaining_speed < 0.5:
        audio_filters.append("atempo=0.5")
        remaining_speed /= 0.5

    audio_filters.append(f"atempo={remaining_speed}")

    audio_filter = ",".join(audio_filters)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-filter:v", video_filter,
        "-filter:a", audio_filter,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        output_file,
    ]

    print("Running command:")
    print(" ".join(cmd))

    subprocess.run(cmd, check=True)

    print(f"Saved: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert WEBM to MP4 with adjustable playback speed"
    )

    parser.add_argument(
        "input",
        help="Input .webm file"
    )

    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output .mp4 file"
    )

    parser.add_argument(
        "--speed",
        "-s",
        type=float,
        default=1.0,
        help="Playback speed (e.g., 2.0 = 2x faster)"
    )

    args = parser.parse_args()

    convert_webm_to_mp4(
        input_file=args.input,
        output_file=args.output,
        speed=args.speed
    )


if __name__ == "__main__":
    main()