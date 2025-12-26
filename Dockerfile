FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash vscode

WORKDIR /workspace

RUN pip install --no-cache-dir \
    jupyterlab \
    notebook \
    pandas \
    numpy \
    matplotlib

USER vscode
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
