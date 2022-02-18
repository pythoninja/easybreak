#!/usr/bin/env python
from argparse import Namespace
from pathlib import Path
from typing import NoReturn

from easybrake.utils import get_videos, generate_output, generate_commands, paths_to_str


def handle_generate(args: Namespace) -> NoReturn:
    input_dir: str = args.input_dir
    output_dir: str = args.output_dir
    preset_path: str = args.preset_path

    videos: list[Path] = get_videos(input_dir)
    output: list[str] = generate_output(videos_path=videos, output_dir=output_dir, preset_path=preset_path)
    commands: list[str] = generate_commands(input_videos=paths_to_str(videos), output_videos=output,
                                            preset_path=preset_path)

    print(*commands, sep="\n")
