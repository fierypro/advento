def get_float(message="", error_msg="Only real numbers are allowed."):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(error_msg)

def get_int(message="", error_msg="Only whole numbers are allowed."):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_msg)


def main():
    pass

if __name__ == "__main__":
    main()
