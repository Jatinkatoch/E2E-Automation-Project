# # =========================
# # Layer 1: Ubuntu Base
# # =========================

# FROM ubuntu:22.04


# # =========================
# # Layer 2: System Setup
# # =========================

# ENV DEBIAN_FRONTEND=noninteractive


# RUN apt-get update && apt-get install -y \
#     python3 \
#     python3-pip \
#     python3-venv \
#     curl \
#     wget \
#     git \
#     && apt-get clean


# RUN ln -s /usr/bin/python3 /usr/bin/python



# # =========================
# # Layer 3: Application Setup
# # =========================

# WORKDIR /app


# COPY requirements.txt .


# RUN pip3 install --upgrade pip

# RUN pip3 install -r requirements.txt



# # =========================
# # Layer 4: Copy Project
# # =========================

# COPY . .



# # =========================
# # Layer 5: Automation Setup
# # =========================

# WORKDIR /app/automation


# RUN pip3 install -r requirements.txt


# RUN playwright install

# RUN playwright install-deps



# # =========================
# # Layer 6: Run Tests
# # =========================

# CMD ["pytest", "-v"]

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]


