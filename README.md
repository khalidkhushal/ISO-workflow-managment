# ISO Workflow System (Multi-Organization)

A full-stack web application for managing ISO workflows across multiple organizations. Built with Flask backend and React frontend in a mono repo structure.

## Features
- Multi-organization support
- User authentication and authorization
- Organization management
- Workflow creation and tracking
- Step-based workflow progression
- MongoDB database integration

## Tech Stack

### Backend
- Python Flask
- MongoDB with PyMongo
- Flask-CORS
- bcrypt for password hashing

### Frontend
- React 18
- Vite
- Axios for API calls

## Project Structure
```
iso-workflow-system/
├── backend/                 # Flask application
│   ├── app/                 # Application package
│   ├── models/              # Data models
│   ├── routes/              # API routes
│   ├── utils/               # Utilities
│   ├── requirements.txt     # Python dependencies
│   └── run.py              # Application entry point
├── frontend/                # React application
│   ├── src/                 # Source code
│   ├── public/              # Static assets
│   ├── package.json          # Node dependencies
│   ├── vite.config.js        # Vite configuration
│   └── index.html           # HTML template
├── docs/                   # Documentation
│   ├── BACKEND_README.md    # Backend documentation
│   └── FRONTEND_README.md   # Frontend documentation
├── .env.example            # Environment variables template
└── README.md              # This file
```

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- MongoDB
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd iso-workflow-system
   ```

2. Set up backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up frontend:
   ```bash
   cd ../frontend
   npm install
   ```

4. Configure environment:
   ```bash
   cp ../.env.example ../.env
   # Edit .env with your MongoDB URI and secret key
   ```

5. Start MongoDB service

### Running the Application

1. Start backend server:
   ```bash
   cd backend
   python run.py
   ```
   Backend runs on http://localhost:5000

2. Start frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```
   Frontend runs on http://localhost:3000

## API Documentation

See detailed API documentation in:
- `docs/BACKEND_README.md` - Backend API endpoints and models
- `docs/FRONTEND_README.md` - Frontend components and usage

## Usage

1. **Register a new user** through the registration form
2. **Login** with your credentials
3. **Create organizations** to manage different entities
4. **Create workflows** within organizations
5. **Manage workflow steps** and track progress

## Development

### Backend Development
- The Flask app uses blueprints for route organization
- MongoDB is used as the primary database
- Password hashing with bcrypt
- CORS enabled for frontend communication

### Frontend Development
- React hooks for state management
- Axios for API communication
- Vite for fast development builds
- Proxy configuration for API calls

## Deployment

### Backend Deployment
1. Set production environment variables
2. Use production WSGI server (Gunicorn)
3. Configure MongoDB Atlas or production MongoDB instance

### Frontend Deployment
1. Build production version: `npm run build`
2. Serve static files from `dist/` directory
3. Configure reverse proxy for API calls

## Contributing

1. Follow the existing code structure and patterns
2. Add appropriate documentation
3. Test both backend and frontend changes
4. Update relevant README files

## License

This project is developed as a take-home assignment. All rights reserved.