from fastapi import FastAPI, Request, HTTPException, status

app = FastAPI()

user_list = [
    {
        'username': 'abc',
        'password': 'abc'

    },
    {
        'username': '123',
        'password': '123'
    }
]


@app.get('/')
async def helloword():
    return "hello world"


@app.get('/users')
async def get_users():
    return user_list


@app.get('/user/{username}')
async def get_user(username: str):
    for i in range(len(user_list)):
        if username in user_list[i]['username']:
            return user_list[i]

    return "User not exist!!"

@app.post('/')
async def add_user(username: str, password: str):
    user_name = username
    pass_word = password

    if user_name not in [user_list[i]['username'] for i in range(len(user_list))]:
        user_list.append({'username': user_name, 'password': pass_word})
        return "Successful!!"
    else:
        return "already exist!!"


@app.delete('/')
async def delete_user(username: str):
    user_name = username
    for i in range(len(user_list)):
        if user_name in user_list[i]['username']:
            user_list.remove(user_list[i])
            return f'Remove {user_name} successful!!'
    else:
        return f'{user_name} not exist!!'

