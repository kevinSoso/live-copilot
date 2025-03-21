import re
import emoji
import unicodedata
from cleantext import clean

# 去除文本中的 emoji、标点符号、重复字符等
def clean_comment(text):
    text = text.lower() 
    text = emoji.replace_emoji(text, replace='')  
    text = "".join(c for c in text if unicodedata.category(c)[0] not in ["S", "C"])  # 去掉特殊符号
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)  # 限制重复字符
    text = re.sub(r"[^\w\s]", "", text)  # 去除标点符号
    return clean(text, no_emoji=True, to_ascii=False, no_punct=True)