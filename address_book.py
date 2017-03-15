import yaml


def make_book(book=[]):
    return book


def add_address(book, addr):
    book.append(addr)


def find_by_name(book, name):
    return [u for u in book if u[0] == name]


def find_by_number(book, number):
    return [u for u in book if u[1] == number]


def delete_by_name(book, name):
    to_remove = [i for i, u in enumerate(book) if u[0] == name]
    return [u for i, u in enumerate(book) if i not in to_remove]


def print_result(result):
    if result:
        print(result)
    else:
        print("no result")


def main():
    book = make_book()
    print_result(book)

    add_address(book, ("Park", "010-2455-2044"))
    add_address(book, ("Khim", "010-4435-9897"))
    add_address(book, ("Lee", "010-8644-1124"))
    print_result(book)

    print_result(find_by_name(book, "Lee"))
    print_result(find_by_name(book, "Park"))
    print_result(find_by_name(book, "Choi"))

    print_result(find_by_number(book, "010-8644-1124"))
    print_result(find_by_number(book, "010-2455-2044"))
    print_result(find_by_number(book, "010-0000-0000"))

    print_result(delete_by_name(book, "Park"))
    print_result(delete_by_name(book, "Choi"))

    with open('address_book.yaml', 'w') as f:
        yaml.dump(book, f)

    with open('address_book.yaml', 'r') as f:
        print_result(yaml.load(f))


if __name__ == "__main__":
    main()
