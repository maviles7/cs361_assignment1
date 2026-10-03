# MICROSERVICE
# pseudorandom number generator

# import modules
import random
import time
import os

# constants
PRNG_FILE = "prng-service.txt"

print("PRNG microservice started - listening for requests")

# prng function
def generate_random_number():
    while True:
        time.sleep(1)  # sleep for 1 second
        # if path exists, then read the file
        if os.path.exists(PRNG_FILE):
            with open(PRNG_FILE, "r") as f:
                file_content = f.read().strip()

            # if the file content = "run", then generate a random number & write to file
            if file_content == "run":
                # generate a random number between 1 and 6
                random_number = random.randomint(1, 6)
                # write the random number to the file
                with open(PRNG_FILE, "w") as f:
                    f.write(str(random_number))
                print(f"random number generated: {random_number}")

generate_random_number()