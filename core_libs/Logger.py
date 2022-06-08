import os
import sys


dir_name = os.path.dirname(__file__).replace(f"{os.sep}core_libs", "")
sys.path.append(dir_name)


try:
    import logging

except ImportError as imp_err:
    print("There was an error importing files - From %s" % __file__)
    print("\n---{{{ Failed - " + format(imp_err) + " }}}---\n")
    raise

MAP_LEVELS = {
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
}


class Logger:
    def __init__(self, prefix=None, log_level="INFO", is_date=True):
        self.prefix = prefix
        self.log_level = MAP_LEVELS[log_level.upper()]

        if is_date:
            logging.basicConfig(
                level=self.log_level,
                format="%(asctime)s %(name)-16s %(levelname)-8s %(message)s",
            )
        else:
            logging.basicConfig(level=self.log_level)
        logger = logging.getLogger(self.prefix)
        self.map_func = {
            "ERROR": logger.error,
            "WARNING": logger.warning,
            "INFO": logger.info,
            "DEBUG": logger.debug,
        }

    def error(self, msg):
        self.__write("ERROR", msg)

    def warning(self, msg):
        self.__write("WARNING", msg)

    def info(self, msg):
        self.__write("INFO", msg)

    def debug(self, msg):
        self.__write("DEBUG", msg)

    def __write(self, level, msg):
        self.map_func[level.upper()](msg)

    def error_in_box(self, msg):
        self.__write_in_box("ERROR", msg)

    def warning_in_box(self, msg):
        self.__write_in_box("WARNING", msg)

    def info_in_box(self, msg):
        self.__write_in_box("INFO", msg)

    def debug_in_box(self, msg):
        self.__write_in_box("DEBUG", msg)

    def __write_in_box(self, level, msg):
        lines = ["╔═" + "═" * len(str(msg)) + "═╗"]
        lines += ["║" + " %s " % msg + "║"]
        lines += ["╚═" + "═" * len(str(msg)) + "═╝"]
        list(map(self.map_func.get(level.upper()), lines))

    def print_in_box(self, msg):
        lines = ["╔═" + "═" * len(str(msg)) + "═╗"]
        lines += ["║" + " %s " % msg + "║"]
        lines += ["╚═" + "═" * len(str(msg)) + "═╝"]
        list(map(print, lines))
