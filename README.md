# 🌍 Roamly – AI-Powered Travel Companion (Backend)

> FastAPI-powered backend for Roamly, an AI-driven travel planning platform that provides personalized recommendations, itinerary generation, travel analytics, budget insights, and intelligent travel assistance.

---

## 🚀 Overview

Roamly is an AI-powered travel companion designed to help users plan smarter trips through personalized recommendations, travel preference analysis, itinerary generation, destination exploration, and budget optimization.

This repository contains the backend services built with **FastAPI**, **MongoDB**, and **Google Gemini AI**, providing secure APIs, authentication, user management, and AI-powered travel features.

---

## ✨ Core Features

### 🤖 AI Travel Assistant

* AI-powered travel concierge
* Smart travel recommendations
* Interactive travel planning support

### 📅 AI Itinerary Generator

* Personalized trip schedules
* Day-wise activity planning
* Destination-specific recommendations

### 🧬 Travel DNA Analysis

* Travel personality assessment
* Preference-based destination matching
* Personalized travel insights

### 💰 Budget Truth Analyzer

* Travel expense estimation
* Budget optimization suggestions
* Cost breakdown analysis

### ⚔️ Destination Battle

* Compare destinations side-by-side
* AI-generated travel recommendations

### 🔥 Trip Roast

* Fun and engaging AI travel critiques

### 🤔 What-If Travel Simulator

* Alternative trip scenarios
* Dynamic travel planning suggestions

### 🗺️ Destination Services

* Destination exploration
* Nearby places discovery
* Country information lookup
* Geolocation support

### 🔐 Secure Authentication

* JWT-based authentication
* User registration and login
* Protected routes
* Password hashing with bcrypt

---

## 🏗️ Technology Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| FastAPI          | API Framework                  |
| MongoDB          | Database                       |
| Beanie ODM       | MongoDB Object Document Mapper |
| Motor            | Async MongoDB Driver           |
| JWT              | Authentication                 |
| bcrypt           | Password Security              |
| Google Gemini AI | AI Services                    |
| HTTPX            | Async HTTP Requests            |
| SlowAPI          | Rate Limiting                  |

---

## 📂 Project Structure

```text
backend/
│
├── routes/             # API Routes
├── models/             # Database Models
├── middleware/         # Authentication & Middleware
├── services/           # Business Logic
├── utils/              # Utility Functions
├── config/             # Configuration
├── main.py             # Application Entry Point
├── requirements.txt
└── README.md
```

---

## 📋 Prerequisites

Before running the application, ensure you have:

* Python 3.10+
* MongoDB
* Google Gemini API Key
* Git

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/roamly.git
cd roamly/backend
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the backend directory:

```env
MONGODB_URI=your_mongodb_uri
JWT_SECRET=your_jwt_secret
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Start the Server

```bash
python main.py
```

Server will run at:

```text
http://localhost:5000
```

---

## 📡 API Endpoints

### Authentication

| Endpoint         | Method |
| ---------------- | ------ |
| /api/auth/signup | POST   |
| /api/auth/login  | POST   |
| /api/auth/me     | GET    |
| /api/auth/logout | POST   |

### AI Services

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

### Destination Services

| Endpoint                        | Method |
| ------------------------------- | ------ |
| /api/destinations/explore       | POST   |
| /api/destinations/places-nearby | GET    |
| /api/destinations/geocode       | GET    |
| /api/destinations/country-info  | GET    |

### Weather Services

| Endpoint     | Method |
| ------------ | ------ |
| /api/weather | GET    |

### User Services

| Endpoint           | Method              |
| ------------------ | ------------------- |
| /api/user/profile  | GET / PATCH         |
| /api/user/trips    | GET / POST / DELETE |
| /api/user/autopsy  | POST                |
| /api/user/dna      | PATCH               |
| /api/user/wishlist | POST                |
| /api/user/history  | GET                 |

---

## 📖 Interactive API Documentation

FastAPI automatically generates Swagger documentation.

Access it at:

```text
http://localhost:5000/docs
```

---

## 🔒 Security Features

* JWT Authentication
* Password Hashing using bcrypt
* Protected API Routes
* Environment Variable Protection
* Rate Limiting with SlowAPI
* Secure User Session Management

---

## 🧪 Development

Run the application in development mode:

```bash
python main.py
```

---

## 🚀 Deployment

Supported deployment platforms:

* Render
* Railway
* AWS
* DigitalOcean
* Azure App Service

---

## 📈 Future Enhancements

* Flight Search Integration
* Hotel Recommendations
* Real-Time Booking Support
* AI Voice Travel Assistant
* Offline Travel Mode
* Multi-Language Support
* Social Travel Community

---

## 👨‍💻 Author

**Dileep Rajesh**

B.Tech – Computer Science Engineering
ANITS (Anil Neerukonda Institute of Technology and Sciences)

---

## 📄 License

This project is licensed under the MIT License.

---

### 🌟 Roamly — Explore Smarter, Travel Better.
