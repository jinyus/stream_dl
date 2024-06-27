import os
import time
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path


def download(url, filename):
    command = f'yt-dlp -o "{filename}" "{url}"'
    os.system(command)


if __name__ == "__main__":
    parser = ArgumentParser(description="Stream video downloader")
    parser.add_argument("--output", "-o", help="output filename")

    args, unknownargs = parser.parse_known_args()

    if len(unknownargs) == 0:
        quit("No url provided")

    rest = " ".join(unknownargs).strip()

    if not rest.startswith("http"):
        quit(f'invalid url: "{rest}"')

    filename = args.output.strip() if args.output else str(datetime.now()) + ".mp4"

    filepath = Path(filename)

    file_stem = filepath.stem
    file_ext = filepath.suffix

    attempt = 1

    while True:
        if not filepath.exists():
            download(rest, filename)

        attempt += 1
        filename = f"{file_stem}_{attempt}{file_ext}"

        for i in range(1, 6):

            print(f"download finished, restarting in {i}")

            time.sleep(1 if filepath.exists() else 0)
