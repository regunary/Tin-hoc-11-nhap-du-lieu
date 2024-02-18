B1: Khởi tạo môi trường ảo
    python -m venv .venv

B2: Active môi trường ảo
    .venv/Scripts/Activate -> Window

B3: Cài thư viện
    python -m pip install -r requirements.txt

B4: Cd vào thư mục demo
    cd demo

B5: Chạy makemigration
    python manage.py makemigrations

B6: Chạy migrate
    python manage.py migrate

B7: Tạo superuser
    python manage.py createsuperuser

B8: Chạy web
    python manage.py runserver

B9: Truy cập vào admin bằng tài khoản superuser vừa tạo
    localhost:8000/admin/
