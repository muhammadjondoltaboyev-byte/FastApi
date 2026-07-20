from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "Toxir Toxirov", "address": "Fergana", "phone": "+99890"},
    {"id": 2, "name": "Sobir Toxirov", "address": "Tashkent", "phone": "+99891"},
    {"id": 3, "name": "Toxir Sobirov", "address": "Andijan", "phone": "+99892"},
    {"id": 4, "name": "Jalil Toxirov", "address": "Fergana", "phone": "+99899"},
    {"id": 5, "name": "Bakir Sobirov", "address": "Namangan", "phone": "+99877"}
]

@app.get('/users')
def get_users():
    return users

@app.get('/users/{user_id}')
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"xatolik": "Bunaqa foydalanuvchi topilmadi!!!"}

@app.get('/users/address/{address}')
def get_user_by_address(address: str):
    result = []
    for user in users:
        if user["address"] == address:
            result.append(user)
    if not result:
        return {"xatolik": "Bu manzilda user yo'q"}
    return result

@app.post('/users')
def add_user(name: str, address: str, phone: str):
    new_id = len(users) + 1
    new_user = {
        "id": new_id,
        "name": name,
        "address": address,
        "phone": phone
    }
    users.append(new_user)
    return {"message": "Yangi foydalanuvchi qo'shildi", "user": new_user}