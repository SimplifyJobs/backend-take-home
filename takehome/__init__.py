import logging

# Logger messages are sent directly to uvicorn and will be logged to the console
# Brownie points for passing a custom logger to uvicorn
# This is outside the criteria of this project

logger = logging.getLogger('uvicorn.error')