import os
import subprocess

# Folder with tests
test_directory = "tests"

# Program name
executable = "main.c"

filePath = os.path.dirname(os.path.abspath(__file__))

def red_text(text):
    print(f"\033[91m{text}\033[0m")

def green_text(text):
    print(f"\033[92m{text}\033[0m")

test_failed_sum = 0
test_passed_sum = 0
tests_total = 0

for test in os.listdir(test_directory):
    folder_path = os.path.join(test_directory, test)
    
    # test is folder that starts with test
    if os.path.isdir(folder_path) and test.startswith("test"):
        tests_total += 1
        stdin_file = os.path.join(folder_path, "stdin")
        stdout_file = os.path.join(folder_path, "stdout")

        try: 
            subprocess.run(["gcc", "-o", "main", executable], cwd=filePath, stdout=subprocess.PIPE, text=True, check=True)
            result = subprocess.run(["./main"], stdin=open(stdin_file, "r"), stdout=subprocess.PIPE, text=True, cwd=filePath, check=True)

            expected_output = open(stdout_file, "r").read()
            if result.stdout == expected_output:
                green_text("Test " + folder_path + " passed.")
                test_passed_sum += 1
            else:
                red_text("Test " + folder_path + " failed.")
                print(f"Expected output: ")
                print(f"", expected_output)
                print(f"\n\nYour output: ")
                print(f"", result.stdout)
                test_failed_sum += 1
        except subprocess.CalledProcessError as e:
            print(f"Error running test in {folder_path}: {e}")

print(f"Tests in total:", tests_total)
print(f"Tests passed:", test_passed_sum)
print(f"Tests failed:", test_failed_sum)