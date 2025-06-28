# SiSantri API (DRF) Setup

## 📌 Requirements
Sebelum memulai, pastikan kamu memiliki:
- Python 3.12 atau lebih baru
- Django 5.1
- Django REST Framework (DRF)
- Simple JWT (untuk autentikasi berbasis token JWT)
- Virtual environment untuk isolasi proyek

## 📦 Instalasi Dependencies
```bash
# 1. Buat virtual environment
python -m venv venv

# 2. Aktifkan virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install Django dan DRF
pip install django==5.1 djangorestframework djangorestframework-simplejwt python-dotenv
```

## 📁 Struktur Proyek
```plaintext
project_root/
│── config/  # Direktori untuk settings
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py      # Konfigurasi utama
│   │   ├── dev.py       # Konfigurasi untuk development
│   │   ├── prod.py      # Konfigurasi untuk production
│── app/  # Aplikasi utama Django
│── manage.py
│── .env  # Konfigurasi environment (tidak di-upload ke Git)
│── .gitignore
│── requirements.txt
```

## 🛠️ Konfigurasi `.env`
Buat file `.env` di root proyek untuk menyimpan variabel sensitif:
```ini
# SECURITY
SECRET_KEY='DJANGO_SECRET_KEY'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,teknohole.com,www.teknohole.com
ACCESS_TOKEN_LIFETIME=1
REFRESH_TOKEN_LIFETIME=7

# DATABASE
DB_ENGINE=django.db.backends.postgresql
DB_NAME=db_teknohole
DB_USER=postgres
DB_PASSWORD=admin123
DB_HOST=localhost
DB_PORT=5432

# EMAIL SETTINGS
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=teknohole@gmail.com
EMAIL_HOST_PASSWORD= 16 digit password smtp gmail
DEFAULT_FROM_EMAIL = Teknohole <teknohole@gmail.com>
EMAIL_USE_TLS=True

```

## 🚀 Menjalankan Proyek
### **Development Mode**
```bash
export DJANGO_SETTINGS_MODULE=teknohole.settings.development  # Linux/Mac
set DJANGO_SETTINGS_MODULE=teknohole.settings.development  # Windows
$env:DJANGO_SETTINGS_MODULE="teknohole.settings.development" # Powershell
python manage.py runserver
```

### **Production Mode**
```bash
export DJANGO_SETTINGS_MODULE=teknohole.settings.production  # Linux/Mac
set DJANGO_SETTINGS_MODULE=teknohole.settings.production  # Windows
$env:DJANGO_SETTINGS_MODULE="teknohole.settings.production" # Powershell
python manage.py migrate
python manage.py collectstatic --noinput
```

## 📄 `.gitignore`
Tambahkan `.gitignore` agar tidak mengupload file yang tidak diperlukan:
```gitignore
# Virtual environment
venv/

# File database lokal
db.sqlite3

# Konfigurasi sensitif
.env
config/settings/local.py
config/settings/dev.py

# Cache dan file sementara
__pycache__/
*.pyc
*.pyo
*.log
*.swp

# File statis dan media
staticfiles/
media/
```

## 📄 Catatan
- **Gunakan `.env`** untuk menyimpan variabel penting
- **Gunakan `.gitignore`** agar repository tetap bersih

## 🎯 Petunjuk Kolaborasi
1. **Fork repository ini** ke akun GitHub kamu.
2. **Clone repository** ke lokal:
   ```bash
   git clone https://github.com/ArbathAbdurrahman/teknohole_DRF.git
   ```
3. **Buat branch baru** untuk fitur atau perbaikan:
   ```bash
   git checkout -b nama-fitur
   ```
4. **Install dependencies** dan siapkan environment:
   ```bash
   pip install -r requirements.txt
   cp .env.example .env  # Buat file konfigurasi
   ```
5. **Lakukan perubahan dan commit**:
   ```bash
   git add .
   git commit -m "Deskripsi perubahan"
   ```
6. **Push branch ke GitHub**:
   ```bash
   git push origin nama-fitur
   ```
7. **Buka Pull Request (PR)** untuk ditinjau oleh tim.
8. **Tunggu review** dan lakukan perubahan jika diperlukan.
