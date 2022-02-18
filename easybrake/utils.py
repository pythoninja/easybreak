#!/usr/bin/env python
import pathlib
import re
from pathlib import Path
from typing import Pattern, Final

VIDEO_EXTENSIONS_MAP: Final[dict[str, str]] = {
    ".mkv": "*.mkv",
    ".avi": "*.avi",
    ".m4v": "*.m4v",
    ".mp4": "*.mp4",
    ".webm": "*.webm"
}
QUALITY_RE_PATTERN: Final[Pattern[str]] = re.compile(r"(\d{3,4}[pi])", re.IGNORECASE)


def get_videos(input_path: str) -> list[Path]:
    return [file for file in pathlib.Path(input_path).iterdir()
            if file.suffix in VIDEO_EXTENSIONS_MAP.get(file.suffix, "_")
            and file.suffix != '']


def generate_output(videos_path: list[Path], output_dir, preset_path) -> list[str]:
    output_files_list: list[str] = []
    preset_quality: Final[str] = preset_path.split("-")[1]

    if not videos_path:
        print("No video files found there. Choose another directory or run --help")
        exit(0)

    file: Path
    for file in videos_path:
        temp_filename = f"{output_dir}/{file.stem}.mp4"
        temp_filename = QUALITY_RE_PATTERN.sub(preset_quality, temp_filename)

        output_files_list.append(temp_filename)

    return output_files_list


def generate_commands(input_videos: list[str], output_videos: list[str], preset_path) -> list[str]:
    handbrake_template: Final[str] = 'handbrakecli --preset-import-file "%PRESET_FILE%" ' \
                                     '--input "%INPUT_FILE%" ' \
                                     '--output "%OUTPUT_FILE%" ' \
                                     '--all-audio ' \
                                     '--all-subtitles'

    commands = []
    input_videos = sorted(input_videos)
    output_videos = sorted(output_videos)

    for ivs, ovs in zip(input_videos, output_videos):
        template = handbrake_template
        template = template.replace("%PRESET_FILE%", preset_path)
        template = template.replace("%OUTPUT_FILE%", ovs)
        template = template.replace("%INPUT_FILE%", ivs)

        commands.append(template)

    return commands


def paths_to_str(paths: list[Path]) -> list[str]:
    return [str(_) for _ in paths]
