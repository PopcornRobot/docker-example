import os

TEST_VARIABLE = os.environ.get('TEST_VARIABLE')

def main():
    for count, value in enumerate(range(20)):
        print(f"{count+1}) Hello, World!: test environment varaible...{TEST_VARIABLE}")

if __name__ == "__main__":
    print("This is a sample Python Script running in a container...")
    main()
