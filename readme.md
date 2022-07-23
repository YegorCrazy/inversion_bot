# Simple Google Sheet Parser

This is a simple telegram bot code that does geometrical invertion to any picture it receives.

You can learn more about geometrical invertion at https://en.wikipedia.org/wiki/Inversive_geometry

## Requirements

You need to have Docker and Docker Compose to use this script.

## Installation

1) Clone this repository;
2) Edit configuration file (.env) as described below;
3) Run command
```bash
docker compose run -i bot
```
*OR*

Use 
```bash
python3 inverter.py --help
```
to learn how it works if you have numpy, pillow and argparse modules installed.

## Configuration

Options from .env file are the following:

- KEY_STORAGE: name of the folder that contains token file.
- TOKEN_FILE_NAME: name of the token file. This file must contain telegram bot token in string format at the first line.

Please do not use spaces when configuring .env file. All this options must be initialized before starting bot.

## Contributing
For any help please contact me!
- Email: egor2002288@gmail.com
- Telegram: @time_is_ticking
