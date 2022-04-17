import os
from argparse import ArgumentParser, REMAINDER
from datetime import datetime
import time
from pathlib import Path
import sys


def download(url, filename):
    command = f'yt-dlp -o "{filename}" "{url}"'
    print(f'command : {command}')
    os.system(command)


if __name__ == "__main__":
    parser = ArgumentParser(description='Stream video downloader')
    parser.add_argument('--output', '-o', help='output filename')

    args, unknownargs = parser.parse_known_args()

    rest = ' '.join(unknownargs).strip()

    filename = args.output.strip() if args.output else str(datetime.now()) + ".mp4"

    filepath = Path(filename)

    file_stem = filepath.stem
    file_ext = filepath.suffix

    attempt = 1

    while True:
        download(rest, filename)

        attempt += 1
        filename = f'{file_stem}_{attempt}{file_ext}'
        for i in range(1, 6):

            print(
                f'download finished, restarting in {i}')

            time.sleep(1)
