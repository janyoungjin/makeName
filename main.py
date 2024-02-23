from fastapi import *
from fastapi.responses import *
from faker import Faker

fake=Faker('ko-kr')
app=FastAPI()
@app.get('/')
def index():
    return FileResponse('index.html')

@app.get('/blank')
def blank():
    return HTMLResponse("")

@app.post('/name')
def get_name(firstname: str = Form(...), name: str = Form(default=""), sex: str = Form(...)):
    if name == firstname:
        return HTMLResponse("<center>돌림자와 성이 일치합니다<br>다시 입력해주세요</center>")
    
    count = 0
    while count < 10000:
        generated_name = (fake.name_male() if sex == "남자" else fake.name_female())
        if (generated_name.startswith(firstname)) and (name in generated_name):
            return HTMLResponse(f"<center><h2>{generated_name}</h2></center>")
        count += 1
    return HTMLResponse(f"<center>이름을 못지었습니다<br>다시 시도해주세요</center>")