import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b
