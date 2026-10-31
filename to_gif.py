import argparse
import subprocess
import os
import sys


def convert_to_gif(input_file, output_file=None, fps=15, width=None):
    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}")
        sys.exit(1)

    # Default output name
    if output_file is None:
        base = os.path.splitext(input_file)[0]
        output_file = base + ".gif"
        if os.path.abspath(output_file) == os.path.abspath(input_file):
            output_file = base + "_out.gif"

    if os.path.abspath(output_file) == os.path.abspath(input_file):
        print("Output file must differ from input file")
        sys.exit(1)

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
        description="Convert a video to GIF"
    )

    parser.add_argument(
        "input",
        help="Input video file (any format ffmpeg can read)"
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

    convert_to_gif(
        input_file=args.input,
        output_file=args.output,
        fps=args.fps,
        width=args.width
    )


if __name__ == "__main__":
    main()
