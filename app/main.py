import sys

from logger import get_logger
from canvas import Canvas

log = get_logger(__name__)


def run(commands):
    log.info("Application started successfully...")
    log.info(commands)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            raise Exception("Invalid input file path")
        input_file_path = sys.argv[1]
        file = open(input_file_path)
        commands = file.readlines()
        commands = [command.replace("\n", "") for command in commands]
        run(commands)
    except Exception as e:
        log.error(e)
