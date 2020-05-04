import requests
import random
import json

with open(r'bot_config.json') as bot_settings:
    data = json.load(bot_settings)
    settings = {'number_of_users': data['number_of_users'],
                'max_posts_per_user': data['max_posts_per_user'],
                'max_likes_per_user': data['max_likes_per_user']}

backend_url = "http://127.0.0.1:8000/"


def register(email, password):
    url = backend_url + 'users/'
    requests.post(url, data={'email': email, 'password': password})
    print(f"Registered user with email {email}")


def login(email, password):
    url = backend_url + 'api/login/'
    r = requests.post(url, data={'username': email, 'password': password})
    print(r.json())
    return r.json()['access']


def create_posts(token, max_number_of_posts, user_email):
    posts_to_create = random.randint(0, max_number_of_posts)
    url = backend_url + 'posts/'
    hed = {'Authorization': 'Bearer ' + token}
    body = {'title': "Standard title made by " + user_email,
            'body': "Standard body made by " + user_email}

    for i in range(posts_to_create):
        requests.post(url, json=body, headers=hed)

    print(f'User {user_email} created {posts_to_create} posts')


def get_posts(token):
    url = backend_url + 'posts/'
    hed = {'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=hed)
    print(r.json()['posts'])
    return r.json()['posts']


def like_posts(token, max_number_of_posts_to_like):
    posts_list = get_posts(token)
    random.shuffle(posts_list)
    posts_to_like = random.randint(0, max_number_of_posts_to_like)

    for i in range(posts_to_like):
        url = backend_url + 'like/'
        hed = {'Authorization': 'Bearer ' + token}
        body = {'post_id': posts_list[i]['id']}
        requests.post(url, json=body, headers=hed)


def work(i):
    email = f"user{i}@gmail.com"
    password = 123456
    register(email, password)
    access_token = login(email=email, password=password)
    create_posts(access_token, settings['max_posts_per_user'], email)
    like_posts(access_token, settings['max_likes_per_user'])
    print(f'Routine for user {email} completed')


if __name__ == "__main__":
    for i in range(settings['number_of_users']):
        work(i)
