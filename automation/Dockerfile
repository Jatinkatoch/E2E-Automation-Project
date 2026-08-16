# FROM mcr.microsoft.com/playwright/python:v1.61.0-jammy

# WORKDIR /automation

# RUN apt-get update && apt-get install -y \
#     xvfb \
#     xauth \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# RUN playwright install chromium
# RUN playwright install-deps chromium

# COPY . .

# CMD ["pytest", "-v"]



# FROM mcr.microsoft.com/playwright/python:v1.61.0-jammy

# WORKDIR /automation

# COPY requirements.txt .

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . .

# CMD ["pytest", "-v"]


FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

WORKDIR /automation

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    x11vnc \
    fluxbox \
    websockify \
    novnc \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Install Playwright browsers and dependencies
RUN python3 -m playwright install --with-deps chromium

COPY . .

RUN chmod +x run-tests.sh

ENTRYPOINT ["./run-tests.sh"]

CMD ["-v"]