FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=120 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# we need some build tools for installing additional python pip packages
RUN apt-get update \
    && apt-get install --yes \
    software-properties-common \
    build-essential \
    gcc \
    g++ \
    cmake \
    git \
    curl \
    python3-dev \
    nano

WORKDIR /app

# if we have a packages.txt, install it here, uncomment the two lines below
# be aware that packages.txt must have LF endings only!
COPY packages.txt packages.txt
RUN xargs -a packages.txt apt-get install --yes

COPY requirements.txt requirements.txt
RUN pip install --upgrade -r requirements.txt

EXPOSE 8501

COPY . .

CMD ["streamlit", "run", "streamlit_app.py"]

# Some docker commands see below:
# docker build --progress=plain --tag streamlit-rdkit:latest .
# docker run -ti -p 8501:8501 --rm streamlit-rdkit:latest /bin/bash
# docker run -ti -p 8501:8501 --rm streamlit-rdkit:latest
# docker run -ti -p 8501:8501 -v ${pwd}:/app --rm streamlit-rdkit:latest
# docker run -ti -p 8501:8501 -v ${pwd}:/app --rm streamlit-rdkit:latest /bin/bash
