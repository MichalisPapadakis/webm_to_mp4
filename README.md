# Video converter

Convert videos to `.mp4` or `.gif` using Python + FFmpeg. Any input format FFmpeg can read works (`.webm`, `.mov`, `.mkv`, `.mp4`, ...).

## Usage

### To MP4

```sh
python to_mp4.py input.webm -o output.mp4 -s 3
```

- `-o`: output file name (default: input name with `.mp4`)
- `-s`: speed multiplier (for example, `3` = 3x)

### To GIF

```sh
python to_gif.py input.mp4 -o output.gif --fps 15 -w 480
```

- `-o`: output file name (default: input name with `.gif`)
- `--fps`: GIF frame rate (default: `15`)
- `-w`: output width in pixels (default: keep original)

If the default output name would be the same as the input (e.g. `clip.mp4` → `clip.mp4`), `_out` is appended (`clip_out.mp4`).

## Install FFmpeg (RSL/Linux)

1. Download and extract FFmpeg:

```sh
mkdir -p ~/ffmpeg && cd ~/ffmpeg
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -xf ffmpeg-release-amd64-static.tar.xz
```

2. Add the extracted folder to your `PATH` in `~/.bashrc`:

```sh
export FFMPEG_DIR=$(echo "$HOME"/ffmpeg/ffmpeg-*-amd64-static)
echo "export PATH=$FFMPEG_DIR:\$PATH" >> ~/.bashrc
source ~/.bashrc
```

3. Verify installation:

```sh
ffmpeg -version
```
