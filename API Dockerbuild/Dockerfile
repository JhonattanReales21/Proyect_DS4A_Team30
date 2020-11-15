FROM dash:latest
COPY . /app
WORKDIR /app
RUN set -ex && \
    python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt
EXPOSE 8050
CMD ["python", "app.py"]