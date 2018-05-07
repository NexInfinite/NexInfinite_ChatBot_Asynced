FROM python:3.6

# Create user and switch to it
RUN groupadd -r next_infinite && useradd --no-log-init -r -g next_infinite next_infinite
USER next_infinite

# Install requirements
RUN pip install -U asynctwitch

# Copy code into container
COPY . /src

CMD ["python", "main.py"]
