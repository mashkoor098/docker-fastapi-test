# 🚀 FastAPI Dockerized Application — Nimap Machine Test

This repository contains a simple FastAPI application, as per the Nimap Infotech machine test requirements. The application is fully containerized using Docker and supports basic user management functionalities using a `users.json` file for data persistence.

## 📂 Forked From  
Original Repository: [docker-fastapi-test](https://github.com/RohitPatil18/docker-fastapi-test)

---

## 📌 Project Features

- ✅ **FastAPI** web framework  
- ✅ **Dockerized application** with `Dockerfile` and `docker-compose.yml`
- ✅ **Persistent user data** stored in `data/app/users.json`
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
│   ├── main.py            # FastAPI application
│   └── models.py          # Data models
│
├── data/
│   └── app/
│       └── users.json       # Persistent user data (working!)
|
├── Dockerfile             # Docker build configuration
├── docker-compose.yml     # Docker Compose setup
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🚀 Deployment Notes

- ✅ Ensure Docker is installed and running.
- ✅ The app does not use a database — all user data is saved in a flat file `data/app/users.json`.
- ✅ Data is persistent even after container restart, thanks to Docker volumes.

---
