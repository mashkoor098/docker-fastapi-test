# 🚀 FastAPI Dockerized Application — Nimap Machine Test

This repository contains a simple FastAPI application, as per the Nimap Infotech machine test requirements. The application is fully containerized using Docker and supports basic user management functionalities using a `users.json` file for data persistence.

---

## 📌 Project Features

- ✅ **FastAPI** web framework  
- ✅ **Dockerized application** with `Dockerfile` and `docker-compose.yml`
- ✅ **Persistent user data** stored in `app/data/users.json`
- ✅ **Automatic data folder creation** if missing
- ✅ **API Documentation** available at `/docs` endpoint

---

## 🔗 API Endpoints

| Method | Endpoint      | Description                               |
|--------|--------------|-------------------------------------------|
| GET    | `/`           | Returns a hello message                  |
| GET    | `/users`      | Returns list of users from `users.json`   |
| POST   | `/users`      | Accepts and stores user data in `users.json` |

---

## 🐳 How to Run (Using Docker)

1. **Clone this repository:**
   ```bash
   git clone https://github.com/mashkoor098/docker-fastapi-test.git
   cd docker-fastapi-test
   ```

2. **Build and start the container:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - Open: [http://localhost:8000](http://localhost:8000)
   - API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

4. **Test persistence:**
   - After adding users, stop and remove the containers:
     ```bash
     docker-compose down
     ```
   - Restart containers:
     ```bash
     docker-compose up
     ```
   - ✅ Confirm data in `data/app/users.json` is still available.

---

## 🛠️ Project Structure

```
docker-fastapi-test/
│
├── app/
│   ├── main.py            # FastAPI app entry point
│   ├── services.py        # Logic to handle file operations
│   └── data/              # Contains users.json
│       └── users.json     # Auto-created when user data is posted
├── Dockerfile             # Docker image instructions
├── docker-compose.yml     # Docker Compose file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
---
## User Payload
```
{
  "data": [
    {
      "first_name": "Mashkoor",
      "last_name": "Patel",
      "age": 23
    },
    {
      "first_name": "Mukesh",
      "last_name": "Patil",
      "age": 23
    },
    {
      "first_name": "Rohit",
      "last_name": "Koli",
      "age": 23
    }
  ]
}
```
---
## Docker Compose File
```
version: '3.9'

services:
  fastapi-app:
    build: .
    container_name: fastapi-app
    ports:
      - "8000:8000"
    volumes:
      - .:/app
      - ./app/data:/app/app/data
    restart: always
```

