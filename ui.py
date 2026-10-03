# ui for assignment 1

# import modules
import time

# constants
PRNG_FILE = "prng-service.txt"
IMG_FILE = "image-service.txt"

def pipeline(): 
    #  1 to generate new image (PRN) or 2 to exit
    print("\n1. generate new image\n")
    print("2. exit")
    user_input = input("Enter your choice: ").strip()

    # input = 1
    if user_input == "1":
        # open prng-service.txt and write "run" to the file
        with open(PRNG_FILE, "w") as f:
            f.write("run")
        print("[UI] sent "run" to prng-service.txt")

        time.sleep(5) 

        # read the prng-service.txt file to get the random number
        with open(PRNG_FILE, "r") as f:
            random_number = f.read().strip()
        print(f"[UI] received random number: {random_number}")

        # open image-service.txt & erase data
        with open(IMG_FILE, "w") as f:
            f.write(random_number)
        print("[UI] sent random number to image-service.txt")

        time.sleep(5)

        # read & output image-service.txt
        with open(IMG_FILE, "r") as f:
            image_path = f.read().strip()

        print("result image path: ", image_path)

    elif user_input == "2":
        print("exiting...")
        return 
    else: 
        print("unknown option. please try again")
        pipeline()  # restart the pipeline




