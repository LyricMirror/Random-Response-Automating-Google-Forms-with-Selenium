import random

with open('names.txt', 'r') as file:
    names = [line.strip() for line in file]

with open('surname.txt', 'r') as file:
    surnames = [line.strip() for line in file]

email_domains = ['gmail.com', 'outlook.com']


def generate_random_name():
    random_name = (random.choice(names) + " " + random.choice(surnames))
    return random_name


def generate_random_email():
    random_email = f"{generate_random_name().lower().replace(' ', '')}@{random.choice(email_domains)}"
    return random_email


def select_random_year():
    years = ['//*[@id="i9"]', '//*[@id="i12"]', '//*[@id="i15"]']
    random_year = random.choice(years)
    return random_year


def select_random_gender():
    genders = ['//*[@id="i22"]', '//*[@id="i25"]']
    random_gender = random.choice(genders)
    return random_gender


def select_q1_answer():
    answer = ['//*[@id="i32"]', '//*[@id="i35"]', '//*[@id="i38"]']
    random_answer = random.choice(answer)
    return random_answer
