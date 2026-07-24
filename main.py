from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

class UserCreate(BaseModel):
    name: str
    address: str
    phone: str

class UserUpdate(BaseModel):
    name: str
    address: str
    phone: str


users = [
    {"id": 1, "name": "Toxir Toxirov", "address": "Fergana", "phone": "+99890"},
    {"id": 2, "name": "Sobir Toxirov", "address": "Tashkent", "phone": "+99891"},
    {"id": 3, "name": "Toxir Sobirov", "address": "Andijan", "phone": "+99892"},
    {"id": 4, "name": "Jalil Toxirov", "address": "Fergana", "phone": "+99899"},
    {"id": 5, "name": "Bakir Sobirov", "address": "Namangan", "phone": "+99877"}
]

@router.get('/users')
def get_users():
    return users

@router.get('/users/{user_id}')
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"xatolik": "Bunaqa foydalanuvchi topilmadi!!!"}

@router.get('/users/address/{address}')
def get_user_by_address(address: str):
    result = []
    for user in users:
        if user["address"] == address:
            result.append(user)
    if not result:
        return {"xatolik": "Bu manzilda user yo'q"}
    return result

@router.post('/users')
def add_user(user: UserCreate):
    new_id = len(users) + 1
    new_user = {
        "id": new_id,
        "name": user.name,
        "address": user.address,
        "phone": user.phone
    }
    users.append(new_user)
    return {"message": "Yangi foydalanuvchi qo'shildi", "user": new_user}

@router.put('/users/{user_id}')
def update_user(user_id: int, user: UserUpdate):
    for u in users:
        if u["id"] == user_id:
            u["name"] = user.name
            u["address"] = user.address
            u["phone"] = user.phone
            return {"message": "Foydalanuvchi yangilandi", "user": u}
    return {"xatolik": "Bunaqa foydalanuvchi topilmadi!!!"}

@router.delete('/users/{user_id}')
def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i]["id"] == user_id:
            deleted = users.pop(i)
            return {"message": "Foydalanuvchi o'chirildi", "user": deleted}
    return {"xatolik": "Bunaqa foydalanuvchi topilmadi!!!"}

app.include_router(router)