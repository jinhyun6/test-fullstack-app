# Test Fullstack App

간단한 풀스택 Todo 애플리케이션입니다.

## 구조

- **Frontend**: Next.js (React)
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (또는 SQLite for testing)

## 기능

- Hello World API 엔드포인트
- Todo CRUD 기능
- 데이터베이스 연동
- CORS 설정

## 로컬 실행

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 환경변수

### Backend (.env)
```
DATABASE_URL=postgresql://user:pass@localhost/dbname
ALLOWED_ORIGINS=http://localhost:3000,https://myapp.vercel.app
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 배포 준비 완료!

이 앱은 다음 플랫폼에 배포할 수 있습니다:
- Frontend → Vercel
- Backend → Google Cloud Run
- Database → Supabase