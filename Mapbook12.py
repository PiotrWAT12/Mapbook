# name: str = input("Enter your name: ")
# print(f'WITAJ {name}')

data_of_users: list = [
    {'name': 'Piotr', 'surname': 'Tomaszewski', 'posts': 5, 'location': 'Kielce'},
    {'name': 'Norbert', 'surname': 'Szeliga', 'posts': 15, 'location': 'Rzeszów'},
    {'name': 'Kacper', 'surname': 'Skrzczypczak', 'posts': 8, 'location': 'Legnica'},
    {'name': 'Sebastian', 'surname': 'Wątroba', 'posts': 6, 'location': 'Szynwałd'},
]
print(f'Witaj {data_of_users[0]['name']}')


def read(users: list) -> None:
    """
    this is a function to show users from a list
    :param users:
    :return:
    """
    for user in users[1:]:
        print(f'Twój znajomy: {user['name']},opublikował: {user["posts"]} ')


read(data_of_users)
