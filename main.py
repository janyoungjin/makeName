from fastapi import *
from fastapi.responses import *
from faker import Faker
import clipboard

fake=Faker('ko-kr')
app=FastAPI()
@app.get('/')
def index():
    return FileResponse('index.html')

@app.get('/blank')
def blank():
    return HTMLResponse("")

@app.post('/name')
def get_name(firstname:str=Form(...),name:str=Form(default=""),sex:str=Form(...)):
    result="A"
    while not((result[0]==firstname)and(name in result)):
        result=fake.name_male() if sex=="남자" else fake.name_female() 
    return HTMLResponse(f"""
                        <html>
                        <body>
                            <center>
                            <table>
                                <tr><td colspan="2"><h1>{result}</h1></td></tr>
                                <tr>
                                    <td>
                                        <button style="width: 100%;" onclick="copyToClipboard('{result}')">복사하기</button>
                                    </td>
                                </tr>
                            </table>
                            </center>
                            <script>
                            function copyToClipboard(text) {{
                                navigator.clipboard.writeText(text).then(function() {{
                                    alert('복사완료');
                                }});
                            }}
                            </script>
                        </body>
                        </html>
                        """)