# 🏥 AarogyaX Cure - Next-Gen Emergency Response & Digital Healthcare Ecosystem

**AarogyaX Cure** is an advanced, high-performance web platform designed to streamline emergency medical response, real-time healthcare resource discovery, AI-driven symptom triage, and clinical management across multiple healthcare roles.

---

## 🌟 Key Features & Architecture

### 1. 🎨 Official Brand Logo & Favicon
- Integrated official **AX** medical logo emblem (`favicon.png`, `favicon.ico`, `logo.png`) across browser tab headers and navigation bars.

### 2. 🚨 Emergency SOS Dispatch & 5 Emergency Contacts
- **Live GPS Broadcasting**: Transmits high-precision GPS coordinates (`latitude`, `longitude`) to nearest ER desks and up to **5 Emergency Contacts** simultaneously.
- **WhatsApp & SMS Emergency Dispatch**: Pre-fills Google Maps navigation links in instant emergency alerts.

### 3. 🧪 Realtime Diagnostic Laboratories & Pathology Finder
- Queries live pathology laboratories and diagnostic testing centers via Geoapify Places API (`healthcare.clinic,healthcare`).
- Lists popular diagnostic test packages (*CBC Blood Count, Lipid Profile, Thyroid, HbA1c*), home sample collection availability, and interactive Leaflet map pins.

### 4. 🏥 "Hospitals Near Me" & Bed Availability Engine
- Powered by **Geoapify Places API** (`healthcare.hospital` category) and **Leaflet Vector Maps**.
- Displays real-time hospital distances (Haversine formula), available ER bed counts, standby ambulance fleets, and 1-click call buttons.
- Distance filter pill controls (**Within 3 km**, **Within 5 km**, **Within 10 km**, **All Nearby**).

### 5. 🩸 Real-Time Blood Donor Network
- **Live Contact Numbers**: Direct dial button (`📞 Call Donor`) and instant WhatsApp chat button (`💬 WhatsApp`).
- **Cloud Firestore Real-Time Listener (`db.collection("blood_donors").onSnapshot`)**: Streams newly registered blood donors dynamically across active sessions.
- **Donor Registration Modal**: Allows users to register as active blood donors with contact info and location.

### 6. 🔐 Multi-Role Firebase Authentication & Portals
- Integrated with Firebase Auth project `data-d3a3e` (Email/Password, Google Sign-In with popup & redirect fallbacks, SMS Phone Verification, and Forgot Password recovery).
- Clean input forms with zero hardcoded credential values.
- Specialized Portals & Registrations:
  - 👤 **Patient Portal**: Personal medication tracking, emergency contacts, and Digital Health Card.
  - 👨‍⚕️ **Doctor Portal**: Clinical staff view for patient assignments, AI symptom triage escalations, and report reviews.
  - 🏥 **Hospital Admin Portal**: ER Command Center for live bed counters, ambulance fleet dispatch, and inbound SOS alerts.

### 7. 🤖 Gemini 3.7 Flash AI Health Assistant
- Powered by Google's official `google-genai` SDK using `gemini-3.7-flash`.
- Provides structured first-aid guidance, educational symptom analysis, and strict medical disclaimer safety guardrails.

### 8. 💳 Digital Health Card & Scannable QR Code
- Generates a physical-style emergency medical card with scannable QR Code containing blood group, emergency allergies, and up to 5 emergency contact numbers.

### 9. ☀️ / 🌙 Persistent Light & Dark Mode System
- High-contrast midnight dark theme (`#090d16`) and clean minimalist light theme (`#f8fafc`).
- Choice stored in `localStorage` (`aarogyax_theme`) with anti-flash script execution.

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, Vanilla CSS3 (Custom CSS Design Tokens), ES6+ JavaScript, Leaflet.js, Firebase JS SDK v10.12.0.
- **Maps & Location Services**: Geoapify Places API, Geoapify Carto HD Tiles, Browser Geolocation API.
- **Backend API**: Python 3.11, Flask, Flask-CORS.
- **AI Integration**: Google GenAI SDK (`google-genai` package using `gemini-3.7-flash`).
- **Database & Auth**: Cloud Firestore (`data-d3a3e`), Firebase Authentication.

---

## 📂 Project Structure

```
AarogyaX Cure/
├── backend/
│   ├── app.py                   # Main Flask Application Entrypoint (Port 5000)
│   ├── config.py                # Environment Configuration
│   ├── test_api.py              # Backend Unit & Integration Test Suite (10/10 Passing)
│   ├── routes/                  # API Route Blueprints
│   │   ├── auth.py              # Multi-Role Authentication & Registration
│   │   ├── assistant.py         # Gemini AI Assistant Endpoint
│   │   ├── emergency.py         # Emergency SOS Dispatch Endpoint
│   │   ├── hospitals.py         # Geoapify Hospitals API Endpoint
│   │   ├── blood.py             # Real-Time Blood Donor Network & Matcher
│   │   ├── labs.py              # Diagnostic Laboratories API Endpoint
│   │   └── records.py           # Health Records API Endpoint
│   └── services/                # Core Services
│       ├── gemini_service.py    # Google GenAI Gemini 3.7 Flash Integration
│       ├── location_service.py  # Haversine Distance & Proximity Calculations
│       └── notification_service.py # SMS & WhatsApp Alert Dispatchers
├── frontend/
│   ├── favicon.png              # Official Brand Favicon (PNG Format)
│   ├── favicon.ico              # Official Browser Tab Icon
│   ├── logo.png                 # Official AX Brand Emblem
│   ├── index.html               # Public Landing Page
│   ├── login.html               # Multi-Role Sign-In & Forgot Password Page
│   ├── signup.html              # Multi-Role Profile Registration Page
│   ├── dashboard.html           # Multi-Role Adaptive Dashboard
│   ├── emergency.html           # Instant Emergency SOS Command Center
│   ├── hospitals.html           # Interactive Geoapify Hospital Map & List
│   ├── labs.html                # Realtime Diagnostic Labs & Pathology Center
│   ├── blood.html               # Real-Time Blood Donor Network & Requests
│   ├── assistant.html           # AI Health Assistant Chat Interface
│   ├── records.html             # Digital Health Records Vault
│   ├── reminders.html           # Automated Medication Dosage Tracker
│   ├── profile.html             # Digital Health Card & Scannable QR Code
│   ├── css/                     # Design System & Stylesheets
│   │   ├── style.css            # Base Utility & Light/Dark Theme Tokens
│   │   ├── dashboard.css        # Minimalist Dashboard & Card Matrix
│   │   └── responsive.css       # Mobile, Tablet & Widescreen Adaptations
│   └── js/                      # Frontend Logic & Controllers
│       ├── theme.js             # Global Light/Dark Theme Switcher
│       ├── firebase-config.js   # Firebase App & SDK Config (Project: data-d3a3e)
│       ├── demo-data.js         # Offline Persistence & Mock Storage Engine
│       ├── auth.js              # Multi-Role Auth Controller & Firestore Sync
│       ├── dashboard.js         # Adaptive Role Dashboard Controller
│       ├── emergency.js         # GPS SOS Broadcast Controller
│       ├── hospitals.js         # Geoapify Hospital Map Controller
│       ├── labs.js              # Diagnostic Laboratories Controller
│       ├── blood.js              # Real-Time Blood Network Controller
│       ├── assistant.js         # Gemini AI Chat Controller
│       ├── records.js           # Health Records Vault Controller
│       ├── reminders.js         # Medication Dosage Tracker Controller
│       └── profile.js           # Digital Health Card QR Controller
├── firebase.json                # Firebase Project Rules & Hosting Config
├── firestore.rules              # Cloud Firestore Security Rules
├── .env                         # Root Environment Configuration (API Keys)
└── README.md                    # Project Documentation
```

---

## 🚀 Quick Start Guide

### 1. Start the Flask Backend Server
```bash
python backend/app.py
```
*Backend runs on `http://127.0.0.1:5000`.*

### 2. Run the Test Suite
```bash
python backend/test_api.py
```

### 3. Open the Frontend Application
Simply open `frontend/index.html` or `frontend/dashboard.html` in any modern web browser!

---

## 📄 License
Developed for **AarogyaX Cure Healthcare Ecosystem**. All rights reserved.
