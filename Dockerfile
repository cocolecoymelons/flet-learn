# Pakai python versi ringan
FROM python:3.9-slim

# Set folder kerja
WORKDIR /app

# Install library dari requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file kode kamu ke server
COPY . .

# Jalankan flet di port 7860 (Wajib buat Hugging Face)
# --web artinya jalan sebagai web, --port 7860 itu syarat HF
CMD ["flet", "run", "main.py", "--web", "--port", "7860"]
