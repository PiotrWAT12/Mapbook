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


# read(data_of_users)

def add_user(users: list) -> None:
    """
    add user to a list
    :param users:
    :return:
    """
    name: str = input("Enter your name: ")
    surname: str = input("Enter your surname: ")
    posts: int = int(input("Enter your number of posts: "))
    location: str = input("Enter your location: ")
    new_user: dict = {'name': name, 'surname': surname, 'posts': posts, 'location': location},
    users.append(new_user)

# add_user(data_of_users)
# read(data_of_users)
def delete_user(users: list) -> None:
    name:str = input('Enter a name of user to remove: ')
    for user in users:
        if user['name'] == name:
            users.remove(user)


# delete_user(data_of_users)
# read(data_of_users)