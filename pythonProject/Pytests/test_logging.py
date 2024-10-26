import logging

class Test_BaseClass:
    def test_demoClass(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s:,%(levelname)s:, %(name)s, %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # Pass fileHandler object to it

        logger.setLevel(logging.DEBUG)
        logger.debug("A debug statement is executed")
        logger.info("Information statement")
        logger.warning("Something is in warning mode")
        logger.error("A major error has happened")
        logger.critical("Critical issue")
        return logger