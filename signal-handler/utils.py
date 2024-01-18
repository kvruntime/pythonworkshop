import logging
from logging.handlers import HTTPHandler
from pathlib import Path
import sys


def get_resource(folder: str) -> Path:
    return Path(__file__).parent.joinpath("resources", folder)


def get_stream_formatter() -> logging.Formatter:
    formatter = logging.Formatter(
        fmt=f"%(levelname)-8s %(asctime)s \t %(filename)s @function %(funcName)s line %(lineno)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    return formatter


def get_http_handler() -> logging.Handler:
    handler = HTTPHandler(host="localhost:8000", url="/logs", method="POST")
    return handler


def get_file_handler() -> logging.Handler:
    file_handler = logging.FileHandler(
        filename=get_resource("logs/app.log").as_posix(), mode="a"
    )
    file_handler.setFormatter(get_stream_formatter())
    return file_handler


def get_global_logger() -> logging.Logger:
    logger = logging.getLogger("global-logger")
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(get_stream_formatter())
    logger.addHandler(console_handler)
    return logger
