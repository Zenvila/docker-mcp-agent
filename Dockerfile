FROM python:3.10-slim
WORKDIR /app
RUN pip install "mcp[cli]"
COPY server.py .
CMD ["python", "server.py"]