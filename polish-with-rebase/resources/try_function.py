if __name__ == "__main__":
    if add_two_numbers(5, 5) != 10:
        print("❌ `add_two_numbers` is not correctly implemented")
        raise SystemExit(1)

    validations()

    raise SystemExit(0)
