from fastapi import FastAPI
from nlp.ChatCleaner import clean_comment

# 创建 FastAPI 应用实例
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


 # 示例路由，接收文本并返回去噪后的文本
@app.post("/clean_text/")
async def clean_text_api(text: str):
    cleaned = clean_comment(text)
    return {"original": text, "cleaned": cleaned}
    

 