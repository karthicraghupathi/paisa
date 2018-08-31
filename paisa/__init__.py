# setup logging for the entire module
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# build public API here
from .rest import Rest
