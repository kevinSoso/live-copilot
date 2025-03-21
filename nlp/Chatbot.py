import requests

API_URL = "https://api.302.ai/v1/chat/completions"
API_KEY = "sk-ClrYt98HaY7PJ9A7kzjwLwY56iqjg2udA9Xp5B5VXALi05mq"  

def chatbot_response(user_question, retrieved_info=""):
    """
    直播电商智能客服机器人
    输入：用户问题 + 知识库内容（可选）
    输出：问题分类 + 细化情感分析 + 问题回答
    """

    prompt = f"""
    你是一名专业的直播电商智能客服机器人，你的任务是分析用户问题，并提供准确的分类、情感分析和回答。

    ### 用户问题：
    "{user_question}"

    ### 已检索到的相关知识（可选）：
    {retrieved_info}

    ### 任务要求：
    请根据用户问题和检索到的知识，按照以下格式输出：
    1. **问题分类**（从以下类别中选择最合适的一项）：
       - 商品咨询
       - 价格询问
       - 物流问题
       - 售后问题
       - 促销活动
       - 其他

    2. **情感分析**（从以下类别中选择最合适的一项）：
       - **愉悦（Excited）**
       - **满意（Satisfied）**
       - **中性（Neutral）**
       - **疑惑（Confused）**
       - **焦虑（Anxious）**
       - **愤怒（Angry）**
       - **失望（Disappointed）**
       - **抱怨（Complaining）**
       - **惊讶（Surprised）**
       - **讽刺（Sarcastic）**

    3. **问题回答**（精准简洁地回答用户问题）

    ### 示例输入：
    用户问题：
    "这款衣服的尺码偏大还是偏小？"

    检索到的相关知识：
    "该品牌衣服尺码偏小，建议选择比平时大一码。"

    ### 示例输出：
    1. **问题分类**：商品咨询  
    2. **情感分析**：疑惑（Confused）  
    3. **问题回答**：这款衣服尺码偏小，建议您选择比平时大一码哦！

    现在请根据用户问题作答：
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }


    data = {
        "model": "gpt-3.5-turbo", 
        "temperature": 0.5,
        "messages": [
            {"role": "system", "content": "你是一个专业的电商客服机器人。"},
            {"role": "user", "content": prompt}
        ],
        
    }

    response = requests.post(API_URL, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"错误: {response.status_code} - {response.text}"

# # **测试**
# user_question = "我的快递怎么还没到啊？"
# retrieved_info = "一般情况下，快递会在 3-5 天内送达，若有延误请联系客服。"
# result = chatbot_response(user_question, retrieved_info)
# print(result)
