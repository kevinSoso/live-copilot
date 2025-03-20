from fastapi import FastAPI
from nlp.ChatCleaner import clean_comment
from nlp.Faiss_Util import FaissSearch

# 创建 FastAPI 应用实例
app = FastAPI()

# 创建 Faiss 实例
faiss_util = FaissSearch()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


 # 示例路由，接收文本并返回去噪后的文本
@app.post("/clean_text/")
async def clean_text_api(text: str):
    cleaned = clean_comment(text)
    return {"original": text, "cleaned": cleaned}


@app.get("/save_index")
def save_index():
    faiss_util.save_index()
    return {"message": "save_index success"}



@app.get("/test_search")
def test_addQA(question: str):
    results = faiss_util.search(question)
    return {"message": results}




##################TEST_API##################
@app.get("/test_addQA")
def test_addQA():

    # 添加数据
    faiss_util.add_data("如何申请退款？", "您可以在订单详情页申请退款。")
    faiss_util.add_data("如何联系客服？", "您可以拨打客服电话或在线联系。")
    faiss_util.add_data("订单多久发货？", "订单一般会在 24 小时内发货。")
    faiss_util.add_data("如何使用优惠券？", "在结算页面输入优惠券代码即可使用。")
    return {"message": "添加数据成功！"}
    

 