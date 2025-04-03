from faker import Faker

faker = Faker()


def get_random_10_digits():
    return faker.random_number(10, fix_len=True)


def get_random_last_name():
    return faker.last_name()


def gen_user_agent():
    return faker.user_agent()
