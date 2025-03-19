修改代码之后重新打镜像
docker build -t live-copilot-app .


启动docker镜像
docker run -d --name live-copilot-app -p 8000:80 live-copilot-app


