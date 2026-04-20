# webm_to_mp4

Convert `.webm` videos to `.mp4` using Python + FFmpeg.

## Usage

```sh
python webm_to_mp4.py input.webm -o output.mp4 -s 3
```

- `-o`: output file name
- `-s`: speed multiplier (for example, `3` = 3x)

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
