# FILEPATH

# This code snippet demonstrates the usage of loggers in Python.
# Loggers are used to record events that occur during the execution of a program.
# They are useful for debugging, monitoring, and auditing purposes.
# This code initializes a logger object and sets its logging level to INFO.
# It then logs a sample message using the logger's various logging methods.
# The logged messages can be configured to be displayed on the console or saved to a file.
# Loggers can be customized with different handlers, formatters, and filters to suit specific logging requirements.

import logging

# Initialize the logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.INFO)

# Log a sample message
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
