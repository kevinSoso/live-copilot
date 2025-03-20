# 基于 tiangolo/uvicorn-gunicorn-fastapi 镜像
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim-2025-03-17

# 设置工作目录为 /app
WORKDIR /app

# 复制你的代码到容器中的 /app 目录
COPY . /app


COPY [".model_cache", "/root/.cache/huggingface/hub/"]

# 设置环境变量，使 Transformers 从本地加载模型
ENV HF_HOME=/root/.cache/huggingface/hub/


# **安装 SQLite**
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置 FastAPI 应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
