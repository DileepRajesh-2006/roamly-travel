# 🌍 Roamly – AI-Powered Travel Companion

> **Explore Smarter. Travel Better.**

Roamly is an AI-powered travel planning platform that helps travelers discover destinations, generate personalized itineraries, analyze travel preferences, optimize budgets, and receive intelligent travel recommendations.

Built using **React**, **FastAPI**, **MongoDB**, and **Google Gemini AI**, Roamly combines modern web technologies with artificial intelligence to create a smarter and more personalized travel experience.

---

# ✨ Features

## 🤖 AI Travel Assistant

* Interactive AI travel concierge
* Personalized travel recommendations
* Smart travel planning assistance
* Context-aware travel suggestions

## 🧬 Travel DNA Analysis

* Analyze travel personality and preferences
* Generate unique traveler profiles
* Personalized destination matching
* AI-driven travel insights

## 🗺️ Destination Explorer

* Explore destinations worldwide
* Discover nearby attractions and landmarks
* Country information lookup
* Geolocation-based recommendations

## 📅 AI Itinerary Generator

* Generate complete travel plans instantly
* Day-wise activity schedules
* Attraction recommendations
* Customized trip planning

## 💰 Budget Truth Analyzer

* Realistic travel cost estimation
* Budget breakdown analysis
* Expense optimization suggestions

## ⚔️ Destination Battle

* Compare destinations side-by-side
* AI-generated recommendations
* Travel decision support

## 🔥 Trip Roast

* Fun AI-powered travel critiques
* Entertainment-focused travel analysis

## 🤔 Travel What-If Simulator

* Explore alternative travel scenarios
* Dynamic itinerary suggestions
* Flexible travel planning

## 📊 Analytics Dashboard

* User travel statistics
* Activity tracking
* Personalized travel insights
* Historical travel analysis

## 🔐 Authentication System

* JWT-based authentication
* Secure user registration and login
* Protected routes
* Profile management

---

# 🏗️ Project Architecture

```text
Roamly
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── context/
│   │   └── api/
│
├── backend/
│   ├── routes/
│   ├── models/
│   ├── middleware/
│   ├── services/
│   ├── utils/
│   └── main.py
│
└── README.md
```

---

# 🛠️ Technology Stack

## Frontend

| Technology      | Purpose                    |
| --------------- | -------------------------- |
| React 18        | User Interface Development |
| Vite            | Build Tool                 |
| Tailwind CSS    | Styling                    |
| React Router    | Routing                    |
| Axios           | API Communication          |
| Framer Motion   | Animations                 |
| Leaflet         | Maps Integration           |
| Google Maps API | Location Services          |

## Backend

| Technology       | Purpose              |
| ---------------- | -------------------- |
| FastAPI          | API Framework        |
| MongoDB          | Database             |
| Beanie ODM       | MongoDB ODM          |
| Motor            | Async MongoDB Driver |
| JWT              | Authentication       |
| bcrypt           | Password Hashing     |
| Google Gemini AI | AI Features          |
| HTTPX            | Async HTTP Requests  |
| SlowAPI          | Rate Limiting        |

---

# 📋 Prerequisites

Before running the project, ensure you have:

* Python 3.10+
* Node.js 18+
* MongoDB
* Google Gemini API Key
* Git

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/roamly.git
cd roamly
```

---

## 2. Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Create virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
MONGODB_URI=your_mongodb_uri
JWT_SECRET=your_jwt_secret
GEMINI_API_KEY=your_gemini_api_key
```

Run backend server:

```bash
python main.py
```

Backend URL:

```text
http://localhost:5000
```

---

## 3. Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# 📡 API Endpoints

## Authentication

| Endpoint         | Method |
| ---------------- | ------ |
| /api/auth/signup | POST   |
| /api/auth/login  | POST   |
| /api/auth/me     | GET    |
| /api/auth/logout | POST   |

## AI Services

| Endpoint              | Method |
| --------------------- | ------ |
| /api/ai/chat          | POST   |
| /api/ai/vibe-search   | POST   |
| /api/ai/trip-roast    | POST   |
| /api/ai/battle        | POST   |
| /api/ai/what-if       | POST   |
| /api/ai/itinerary     | POST   |
| /api/ai/budget-truth  | POST   |
| /api/ai/analyze-dna   | POST   |
| /api/ai/packing-list  | POST   |
| /api/ai/culture-coach | POST   |

## Destination Services

| Endpoint                        | Method |
| ------------------------------- | ------ |
| /api/destinations/explore       | POST   |
| /api/destinations/places-nearby | GET    |
| /api/destinations/geocode       | GET    |
| /api/destinations/country-info  | GET    |

## Weather Services

| Endpoint     | Method |
| ------------ | ------ |
| /api/weather | GET    |

## User Services

| Endpoint           | Method              |
| ------------------ | ------------------- |
| /api/user/profile  | GET / PATCH         |
| /api/user/trips    | GET / POST / DELETE |
| /api/user/autopsy  | POST                |
| /api/user/dna      | PATCH               |
| /api/user/wishlist | POST                |
| /api/user/history  | GET                 |

---

# 📖 API Documentation

FastAPI automatically generates interactive Swagger documentation.

Visit:

```text
http://localhost:5000/docs
```

---

# 🔒 Security Features

* JWT Authentication
* Password Hashing with bcrypt
* Protected API Routes
* Environment Variable Protection
* Rate Limiting using SlowAPI
* Secure User Session Management

---

# 🚀 Deployment

## Frontend

* Vercel
* Netlify
* Cloudflare Pages

## Backend

* Render
* Railway
* AWS
* DigitalOcean
* Azure App Services

---

# 🌐 Live Demo

### Frontend

https://roamly-travel-iota.vercel.app/

### Backend API

https://roamly-api.onrender.com

### API Documentation

https://roamly-api.onrender.com/docs

---

# 📈 Future Enhancements

* Flight Search Integration
* Hotel Recommendations
* Real-Time Booking Support
* AI Voice Travel Assistant
* Offline Itinerary Access
* Multi-Language Support
* Travel Community Features
* Collaborative Trip Planning

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 👨‍💻 Author

**Dileep Rajesh**

B.Tech – Computer Science Engineering
ANITS (Anil Neerukonda Institute of Technology and Sciences)

---

# 📄 License

This project is licensed under the MIT License.

---

## 🌟 Roamly – Your Intelligent Travel Companion
