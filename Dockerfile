FROM python:3.12-slim

WORKDIR /FLASK_iFile

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY final_select.py .

EXPOSE 5000

CMD ["python", "final_select.py"]
