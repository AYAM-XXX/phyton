def get_formatted_name(first, middle, last):
    full_name = f"{first} {middle} {last}"
    return full_name.title()


if __name__ == "__main__":
    print("Enter 'q' at any time to quit.")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == 'q':
            break
        last = input("Please give me a last name: ")
        if last == 'q':
            break
        formatted_name = get_formatted_name(first, last)
        print(f"\tNeatly formatted name: {formatted_name}.")
