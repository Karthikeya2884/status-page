# Status Page Application

This repository contains a **Status Page Application**, built as a tech task for **Plivo**. The application is designed to manage and display the real-time status of services, track incidents, and provide a public-facing status page. It also includes authentication and team management capabilities.

---

## Features

- **Real-time Updates**:
  - WebSocket-based live updates for service statuses and incidents.
- **Public-Facing Status Page**:
  - A user-friendly interface to display service statuses and ongoing incidents.
- **Authentication**:
  - Secure user authentication and team management using Clerk (or your preferred authentication provider).
- **Incident Management**:
  - Create, update, and resolve incidents tied to specific services.
- **API Documentation**:
  - Auto-generated documentation using Swagger, available at the `/docs` endpoint.

---

## Tech Stack

- **Backend**: Python, FastAPI, SQLAlchemy
- **Frontend**: HTML, JavaScript
- **Database**: SQLite (can be replaced with other DBs like PostgreSQL or MySQL)
- **WebSocket**: FastAPI-Socket.IO for real-time updates
- **Deployment**: Uvicorn

---

## Setup Instructions

Follow these steps to set up and run the Status Page Application locally:

### Prerequisites
- Python 3.8+
- Git
- A virtual environment tool (e.g., `venv`)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Karthikeya2884/status-page.git
   cd status-page
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   bash uvicorn_start.sh
   ```

5. **Access the Application**:
   - Open [http://localhost:8000/](http://localhost:8000/) in your browser.
   - Visit `/docs` for API documentation.

---

## Folder Structure

```
status-page/
├── app/
│   ├── __init__.py
│   ├── main.py          # Entry point for the application
│   ├── models.py        # Database models
│   ├── database.py      # Database connection and setup
│   ├── crud.py          # CRUD operations for models
│   ├── auth.py          # Authentication logic
│   ├── sockets.py       # WebSocket integration
│   ├── schemas.py       # Pydantic schemas for request/response validation
│   └── routes.py        # API route definitions
├── templates/           # HTML templates for the frontend
│   └── status_page.html
├── static/              # Static files (e.g., JavaScript)
│   └── status.js
├── tests/               # Unit tests
│   └── test_services.py
├── .gitignore
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── uvicorn_start.sh     # Script to start the server
```

---

## Usage

### **1. Real-Time Updates**
- The app uses WebSocket to broadcast status and incident updates.
- Any changes to services or incidents are reflected in real-time on the public-facing status page.

### **2. Incident Management**
- APIs are provided to create, update, and resolve incidents.
- Incidents are tied to specific services and include details like title, description, and status.

### **3. Authentication**
- The app integrates with Clerk for user authentication.
- Only authenticated users can manage services and incidents.

---

## API Documentation

- The application uses Swagger to auto-generate API documentation.
- Visit `/docs` to explore and test the API endpoints.

---

## Testing

- To run the unit tests:
  ```bash
  pytest tests/
  ```
- Ensure that the environment is set up before running the tests.

---

## Deployment

To deploy the application:
1. Host the backend using platforms like **Render**, **Heroku**, or **AWS**.
2. Host the frontend (if separated) on platforms like **Vercel** or **Netlify**.
3. Update the `DATABASE_URL` in `app/database.py` to use a production-ready database (e.g., PostgreSQL).

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE.md) file for details.

---

## Contact

For questions or feedback, please reach out to **karthikeya@example.com**.
