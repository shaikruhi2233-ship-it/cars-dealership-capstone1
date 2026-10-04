# Cars Dealership Capstone
Local starter scaffold for the IBM/Coursera Django + React dealership review capstone.

## Run backend
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver

## Run frontend (second terminal)
cd frontend
npm install
npm run dev

React: http://localhost:5173 | Django API: http://127.0.0.1:8000/api/dealers/ | Admin: http://127.0.0.1:8000/admin/
Create admin account with `python manage.py createsuperuser`.
This is a local starter with demo data. It does not include your real GitHub fork, deployment, lab screenshots, or verified grading evidence. Capture genuine outputs and configure deployment yourself.
