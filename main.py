import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b

if __name__ == "__main__":
    result = add(5, 7)
    print("Result is:", result)