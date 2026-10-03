# MICROSERVICE
# pseudorandom number generator

# import modules
import random
import time

# constants
PRNG_FILE = "prng-service.txt"

print("PRNG microservice started - listening for requests")

# prng function
while True:
    time.sleep(1)  # sleep for 1 second
       
    # open prng-service.txt and read the file
    with open(PRNG_FILE, "r") as f:
        file_content = f.read().strip()

    # if file content = run, then generate random number 
    if file_content == "run"
        random_number = random.randint(0, 100)
        print(f"PRNG microservice generated random number: {random_number}")

        # erase run & write random_number to prng-service.txt
        with open(PRNG_FILE, "w") as f:
            f.write(str(random_number))

