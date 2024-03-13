import modules


def launch_app():
    passwords_count = modules.get_passwords_count()
    password_len = modules.get_password_len(passwords_count)
    should_add_digits = modules.should_add_digits()
    should_add_uppers = modules.should_add_uppers()
    sould_add_lowers = modules.should_add_lowers()
    should_add_spec_chars = modules.should_add_spec_chars()
    should_add_ambiguous_chars = modules.should_add_ambiguous_chars()

    chars = modules.sanitize_password_chars(should_add_digits, should_add_uppers, sould_add_lowers,
                                            should_add_spec_chars, should_add_ambiguous_chars)

    for _ in range(passwords_count):
        print(modules.generate_password(password_len, chars))


launch_app()
