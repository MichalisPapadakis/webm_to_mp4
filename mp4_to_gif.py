import argparse
import subprocess
import os
import sys


def convert_mp4_to_gif(input_file, output_file=None, fps=15, width=None):
    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}")
        sys.exit(1)

    if not input_file.endswith(".mp4"):
        print("Input file must be .mp4")
        sys.exit(1)

    # Default output name
    if output_file is None:
        output_file = input_file[:-len(".mp4")] + ".gif"

    # Build a palette from the video for better GIF colors
    scale = f",scale={width}:-1:flags=lanczos" if width else ""
    video_filter = (
        f"fps={fps}{scale},split[a][b];"
        "[a]palettegen[p];[b][p]paletteuse"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-filter_complex", video_filter,
        "-loop", "0",
        output_file,
    ]

    print("Running command:")
    print(" ".join(cmd))

    subprocess.run(cmd, check=True)

    print(f"Saved: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert MP4 to GIF"
    )

    parser.add_argument(
        "input",
        help="Input .mp4 file"
    )

    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output .gif file"
    )

    parser.add_argument(
        "--fps",
        type=int,
        default=15,
        help="GIF frame rate (default: 15)"
    )

    parser.add_argument(
        "--width",
        "-w",
        type=int,
        default=None,
        help="Output width in pixels (default: keep original)"
    )

    args = parser.parse_args()

    convert_mp4_to_gif(
        input_file=args.input,
        output_file=args.output,
        fps=args.fps,
        width=args.width
    )


if __name__ == "__main__":
    main()
