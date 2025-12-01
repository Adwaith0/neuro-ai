# Neuro AI - Comprehensive Health Assessment Platform

A full-stack web application that integrates multiple machine learning models for disease prediction and autism assessment, featuring cognitive games, speech tools, and professional center submission capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Machine Learning Models](#machine-learning-models)
- [Cognitive Assessment Tools](#cognitive-assessment-tools)
- [Accessibility Tools](#accessibility-tools)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## 🎯 Overview

Mindful Link AI is an advanced health assessment platform that combines multiple disease prediction models with comprehensive autism screening tools. The application provides a user-friendly interface for early detection and assessment of various health conditions, along with cognitive games and accessibility features.

### Key Highlights

- **4 ML-powered disease prediction models** (Diabetes, Heart Disease, Parkinsons, Autism)
- **20-question autism screening assessment** based on M-CHAT-R
- **5 interactive cognitive games** for developmental assessment
- **Speech-to-Text and Text-to-Speech** accessibility tools
- **Professional center submission** system for follow-up care
- **Modern, responsive UI** with glassmorphism design
- **Real-time predictions** with RESTful API architecture

---

## ✨ Features

### 1. Medical Disease Prediction

Predict risk levels for multiple diseases using validated machine learning models:

#### **Diabetes Prediction**

- **Input Features (8):**
  - Pregnancies
  - Glucose Level
  - Blood Pressure
  - Skin Thickness
  - Insulin Level
  - BMI (Body Mass Index)
  - Diabetes Pedigree Function
  - Age
- **Model:** Support Vector Machine (SVM)
- **Output:** Binary classification (0 = No Diabetes, 1 = Diabetes)

#### **Heart Disease Prediction**

- **Input Features (13):**
  - Age
  - Sex
  - Chest Pain Type (cp)
  - Resting Blood Pressure (trestbps)
  - Serum Cholesterol (chol)
  - Fasting Blood Sugar (fbs)
  - Resting ECG (restecg)
  - Maximum Heart Rate (thalach)
  - Exercise Induced Angina (exang)
  - ST Depression (oldpeak)
  - Slope of Peak Exercise
  - Number of Major Vessels (ca)
  - Thalassemia (thal)
- **Model:** Logistic Regression
- **Output:** Binary classification (0 = No Disease, 1 = Disease)

#### **Parkinsons Disease Prediction**

- **Input Features (22):** Voice and speech-related features
  - MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz)
  - MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP
  - MDVP:Shimmer, MDVP:Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5
  - MDVP:APQ, Shimmer:DDA
  - NHR, HNR
  - RPDE, DFA
  - Spread1, Spread2
  - D2, PPE
- **Model:** Support Vector Machine (SVM)
- **Output:** Binary classification (0 = Healthy, 1 = Parkinsons)

#### **Autism Risk Assessment**

- **Input Features (11):** A1-A10 screening scores + Age
- **Model:** Random Forest Classifier (auto-generated)
- **Output:** Risk level classification (Low/Medium/High)

---

## 🧠 Cognitive Assessment Tools

### 1. Autism Screening Questionnaire

- **20 carefully curated questions** based on validated M-CHAT screening tools
- **Categories covered:**
  - Social Communication (eye contact, name response, conversation)
  - Gestural Communication (pointing, waving, showing)
  - Imaginative Play
  - Social Awareness and Empathy
  - Repetitive Behaviors
  - Sensory Sensitivity
  - Motor Behaviors
  - Restricted Interests
  - Behavioral Flexibility
  - Communication Patterns
- **Scoring System:** 5-point scale (Always/Usually/Sometimes/Rarely/Never)
- **Risk Assessment Algorithm:**
  - Low Risk: < 35% score
  - Medium Risk: 35-55% score
  - High Risk: > 55% score
- **Features:**
  - Progress tracking
  - Category-based question grouping
  - Visual progress indicators
  - Results stored for dashboard viewing

### 2. Number Memory Game

- **Purpose:** Test short-term memory and number retention
- **Mechanics:**
  - Players match pairs of cards with numbers (0-7)
  - 8 pairs total (16 cards)
  - Cards flip with animation
  - Tracks moves and matched pairs
- **Cognitive Skills Tested:**
  - Working memory
  - Concentration
  - Pattern recognition
  - Visual memory

### 3. Image Memory Game

- **Purpose:** Test visual memory using emoji symbols
- **Mechanics:**
  - Match pairs of emoji cards
  - 8 different emoji pairs
  - Visual feedback on matches
  - Move counter
- **Cognitive Skills Tested:**
  - Visual recognition
  - Short-term memory
  - Attention span
  - Symbol processing

### 4. Word Memory Game

- **Purpose:** Test verbal/semantic memory
- **Mechanics:**
  - Match pairs of word cards
  - 8 word pairs with diverse vocabulary
  - Text-based memory challenge
- **Cognitive Skills Tested:**
  - Verbal memory
  - Word recognition
  - Reading comprehension
  - Semantic processing

### 5. Color Classification Game

- **Purpose:** Test categorization and color recognition
- **Mechanics:**
  - Sort 12 items into blue and green categories
  - Drag-and-drop or click interface
  - Items include: Sky, Ocean, Leaf, Grass, Blueberry, Emerald, etc.
- **Cognitive Skills Tested:**
  - Classification ability
  - Color perception
  - Decision making
  - Categorization skills

### 6. Category Game

- **Purpose:** Test semantic categorization
- **Mechanics:**
  - Sort 16 words into Animals or Foods categories
  - Words: Dog, Cat, Lion, Tiger, Elephant, Bear, Rabbit, Deer (Animals)
  - Words: Apple, Banana, Pizza, Burger, Pasta, Rice, Bread, Chicken (Foods)
- **Cognitive Skills Tested:**
  - Semantic understanding
  - Logical grouping
  - Conceptual thinking
  - Classification reasoning

---

## 🎤 Accessibility Tools

### 1. Speech to Text

- **Technology:** Web Speech API (browser-native)
- **Features:**
  - Real-time speech recognition
  - Continuous listening mode
  - Interim and final transcript display
  - Multi-language support (default: English US)
  - Transcript management:
    - Copy to clipboard
    - Download as .txt file
    - Clear transcript
    - Manual editing capability
- **Visual Indicators:**
  - Recording status with animated indicator
  - Start/Stop button with state changes
- **Use Cases:**
  - Accessibility for users with writing difficulties
  - Voice dictation for form filling
  - Documentation purposes
  - Interview transcription

### 2. Text to Speech

- **Technology:** Speech Synthesis API (browser-native)
- **Features:**
  - Multiple voice options (different languages and accents)
  - Customizable settings:
    - **Speed Control:** 0.5x to 2x
    - **Pitch Adjustment:** 0.5 to 2.0
    - **Volume Control:** 0% to 100%
  - Playback controls:
    - Play, Pause, Resume, Stop
  - Sample text buttons for quick testing
  - Reset settings to defaults
- **Use Cases:**
  - Accessibility for visually impaired users
  - Reading assistance for dyslexic users
  - Language learning
  - Content consumption

---

## 🏥 Professional Center Integration

### Assessment Submission System

- **Purpose:** Connect users with professional assessment centers
- **Features:**
  - Automatic assessment summary display
  - Comprehensive form with sections:
    - **Personal Information:** Name, Age, DOB, Gender
    - **Contact Information:** Phone, Email, Address
    - **Guardian Information:** Name, Phone, Relation
    - **Center Selection:** 6 pre-configured centers
    - **Additional Notes:** Open text for specific concerns
  - **Assessment Summary Includes:**
    - Risk Level (Low/Medium/High)
    - Risk Percentage
    - Total Score
    - Completion Date & Time
  - **Post-Submission:**
    - Confirmation screen
    - Submission summary
    - Print option
    - Stored in localStorage for tracking
  - **HIPAA Privacy Notice:** Included for data protection awareness

---

## 💻 Technology Stack

### Frontend

- **Framework:** React 18.3.1
- **Language:** TypeScript 5.8.3
- **Build Tool:** Vite 5.4.20
- **Styling:**
  - Tailwind CSS (utility-first)
  - Custom glassmorphism design system
  - Responsive design
- **UI Components:**
  - Custom component library
  - Radix UI primitives
  - Lucide React icons
- **Routing:** React Router 6.30.1
- **State Management:** React Hooks (useState, useEffect)
- **Notifications:** Toast notifications (sonner)
- **HTTP Client:** Fetch API

### Backend

- **Framework:** Flask 3.1.2
- **Language:** Python 3.13
- **Machine Learning:** scikit-learn 1.7.2
- **Data Processing:**
  - NumPy
  - Pandas
- **Model Serialization:** pickle
- **CORS:** flask-cors 6.0.1
- **Server:** Flask development server (port 5000)

### Machine Learning

- **Algorithms Used:**
  - Support Vector Machine (SVM) - Diabetes, Parkinsons
  - Logistic Regression - Heart Disease
  - Random Forest Classifier - Autism
- **Training Framework:** scikit-learn
- **Model Storage:** .sav files (pickle format)

### Development Tools

- **Version Control:** Git
- **Package Managers:**
  - npm (frontend)
  - pip (backend)
- **Virtual Environment:** Python venv
- **Code Quality:**
  - ESLint
  - TypeScript compiler
  - Prettier (optional)

---

## 📁 Project Structure

```
multiple-disease-prediction-streamlit-app/
├── data/                              # All datasets
│   ├── autism.csv                     # Autism screening dataset
│   ├── diabetes.csv                   # Diabetes prediction dataset
│   ├── heart.csv                      # Heart disease dataset
│   └── parkinsons.csv                 # Parkinson's disease dataset
│
├── models/                            # Trained ML models (.sav files)
│   ├── autism_model.sav               # Random Forest - Autism
│   ├── diabetes_model.sav             # SVM - Diabetes
│   ├── heart_disease_model.sav        # Logistic Regression - Heart
│   └── parkinsons_model.sav           # SVM - Parkinsons
│
├── notebooks/                         # Jupyter notebooks
│   ├── training/                      # Model training notebooks
│   │   ├── diabetes_training.ipynb
│   │   ├── heart_training.ipynb
│   │   └── parkinsons_training.ipynb
│   ├── autism_prediction.ipynb        # Autism model development
│   └── model_evaluation.ipynb         # All models evaluation
│
├── backend/                           # Flask REST API
│   ├── .venv/                         # Python virtual environment
│   ├── app.py                         # Flask application & endpoints
│   ├── requirements.txt               # Python dependencies
│   ├── test_api.py                    # API testing script
│   └── README.md                      # Backend documentation
│
├── frontend/                          # React + TypeScript frontend
│   ├── src/
│   │   ├── components/                # React components
│   │   │   ├── ui/                    # shadcn/ui primitives
│   │   │   │   ├── button.tsx
│   │   │   │   ├── input.tsx
│   │   │   │   ├── card.tsx
│   │   │   │   └── ...
│   │   │   ├── Layout/
│   │   │   │   └── Navigation.tsx     # Main navigation
│   │   │   └── SubmitToCenter.tsx     # Form component
│   │   │
│   │   ├── pages/                     # Route pages
│   │   │   ├── Home.tsx               # Landing page
│   │   │   ├── Dashboard.tsx          # User dashboard
│   │   │   ├── AutismInfo.tsx         # Autism hub
│   │   │   ├── Questionnaire.tsx      # 20-question assessment
│   │   │   ├── SubmitAssessment.tsx   # Center submission
│   │   │   ├── MedicalPredictor.tsx   # Disease predictions
│   │   │   ├── MemoryGame.tsx         # Cognitive games (5 types)
│   │   │   ├── SpeechToText.tsx       # Speech recognition
│   │   │   ├── TextToSpeech.tsx       # Speech synthesis
│   │   │   └── NotFound.tsx           # 404 page
│   │   │
│   │   ├── hooks/                     # Custom React hooks
│   │   ├── lib/                       # Utilities
│   │   ├── App.tsx                    # Root component
│   │   ├── main.tsx                   # Entry point
│   │   └── index.css                  # Global styles
│   │
│   ├── public/                        # Static assets
│   ├── package.json                   # Node dependencies
│   ├── vite.config.ts                 # Vite configuration
│   ├── tailwind.config.ts             # Tailwind CSS config
│   └── tsconfig.json                  # TypeScript config
│
├── app.py                             # Streamlit application (alternative UI)
├── requirements.txt                   # Root Python dependencies
├── start.ps1                          # Automated startup script
├── README.md                          # This file (main documentation)
└── DIRECTORY_STRUCTURE.md             # Detailed structure guide
```

> **Note:** See [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md) for detailed directory documentation and path references.

---

## 🚀 Installation & Setup

### Prerequisites

- **Node.js** (v18 or higher) - [Download](https://nodejs.org/)
- **Python** (v3.8 or higher) - [Download](https://www.python.org/)
- **npm** (comes with Node.js)
- **Git** (optional, for cloning)

### Quick Start (Automated) ⚡

**Windows PowerShell:**

```powershell
cd "path\to\multiple-disease-prediction-streamlit-app"
.\start.ps1
```

This automated script will:

1. ✅ Check prerequisites (Python, Node.js, npm)
2. ✅ Setup backend virtual environment
3. ✅ Install Python dependencies
4. ✅ Install Node.js dependencies
5. ✅ Start both servers in separate terminals
6. ✅ Open the application in your browser

---

## 🔧 Manual Setup & Run Instructions

### Option 1: Run Both (Frontend + Backend)

#### Step 1: Setup Backend (Flask API)

```powershell
# Navigate to backend directory
cd backend

# Create virtual environment (first time only)
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# .\.venv\Scripts\activate.bat # Windows CMD
# source .venv/bin/activate    # macOS/Linux

# Install dependencies (first time only)
pip install -r requirements.txt

# Start Flask server
python app.py
```

**Backend Status:**

- ✅ Server running on: `http://localhost:5000`
- ✅ API endpoints ready at `/predict/*`
- Keep this terminal running

#### Step 2: Setup Frontend (React App)

Open a **new terminal** window:

```powershell
# Navigate to frontend directory
cd frontend

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

**Frontend Status:**

- ✅ App running on: `http://localhost:5173`
- ✅ Auto-opens in browser
- ✅ Hot reload enabled

**Access the Application:**

- Open browser to: `http://localhost:5173`
- Frontend communicates with backend automatically

---

### Option 2: Run Streamlit App (Alternative)

If you want to use the Streamlit interface instead:

```powershell
# From project root directory
pip install -r requirements.txt
streamlit run app.py
```

**Streamlit Status:**

- ✅ App running on: `http://localhost:8501`
- Simple interface for disease predictions only
- No frontend/backend separation needed

---

### Option 3: Run Individual Components

#### Backend Only (API Server):

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python app.py
```

Test API: `http://localhost:5000/predict/diabetes`

#### Frontend Only (Development):

```powershell
cd frontend
npm run dev
```

Note: Frontend needs backend running on port 5000

---

## 🔄 Daily Development Workflow

### Starting the Application:

**Terminal 1 (Backend):**

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python app.py
```

**Terminal 2 (Frontend):**

```powershell
cd frontend
npm run dev
```

### Stopping the Application:

- Press `Ctrl + C` in both terminals
- Or close terminal windows

---

## 📦 Build for Production

### Backend Production:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
pip install gunicorn  # WSGI server
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Frontend Production:

```powershell
cd frontend
npm run build  # Creates dist/ folder
npm run preview  # Preview production build
```

Deploy the `dist/` folder to:

- Vercel / Netlify / GitHub Pages
- Any static hosting service

---

## 🌐 Port Configuration

| Service            | Default Port | URL                   |
| ------------------ | ------------ | --------------------- |
| **Flask Backend**  | 5000         | http://localhost:5000 |
| **React Frontend** | 5173         | http://localhost:5173 |
| **Streamlit App**  | 8501         | http://localhost:8501 |

### Change Ports (if needed):

**Backend (`backend/app.py`):**

```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Change port here
```

**Frontend (`frontend/vite.config.ts`):**

```typescript
export default defineConfig({
  server: {
    port: 5173, // Change port here
  },
});
```

---

## 🐛 Troubleshooting

### Backend Issues:

**"Port 5000 already in use":**

```powershell
# Find process using port 5000
netstat -ano | findstr :5000
# Kill process (replace PID)
taskkill /PID <PID> /F
```

**"Module not found":**

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt --force-reinstall
```

**"Cannot activate virtual environment":**

```powershell
# Enable script execution (admin PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Frontend Issues:

**"npm command not found":**

- Install Node.js from nodejs.org
- Restart terminal after installation

**"Port 5173 already in use":**

```powershell
# Change port in vite.config.ts or kill process
netstat -ano | findstr :5173
taskkill /PID <PID> /F
```

**"Dependencies error":**

```powershell
cd frontend
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install
```

---

## 🔍 Verify Installation

### Test Backend:

```powershell
# In browser or using curl
curl http://localhost:5000/predict/diabetes -X POST -H "Content-Type: application/json" -d "{\"features\": [2, 120, 70, 30, 0, 25.5, 0.5, 30]}"
```

### Test Frontend:

1. Open `http://localhost:5173` in browser
2. Navigate to "Medical Predictors"
3. Try a prediction
4. Check browser console (F12) for errors

---

## 📝 Environment Variables

No additional environment variables required. The application uses default configurations:

- Backend auto-loads models from `models/` directory
- Frontend API URL: `http://localhost:5000` (hardcoded)
- CORS enabled for local development

---

## 📖 Usage Guide

### 1. Disease Prediction Workflow

1. Navigate to **Dashboard** or click **"Medical Predictors"**
2. Select a disease predictor (Diabetes, Heart, Parkinsons)
3. Fill in required input features
4. Click **"Predict"** button
5. View prediction result and confidence level
6. Results are displayed immediately

### 2. Autism Assessment Workflow

1. Click **"Get Started"** on homepage or navigate to **"Autism Assessment"**
2. Read the autism information and guidelines
3. Click **"Take Assessment"** in the sidebar
4. Answer all 20 questions (5-point scale)
5. Progress bar shows completion status
6. Review results on Dashboard:
   - Risk level (Low/Medium/High)
   - Risk percentage
   - Score breakdown
   - Recommendations
7. Optionally submit to professional center:
   - Click **"Submit to Center"** in sidebar
   - Fill personal and contact information
   - Select preferred assessment center
   - Submit for professional follow-up

### 3. Cognitive Games

**Access via Sidebar → Cognitive Games**

**Number Memory Game:**

- Click cards to flip
- Match pairs of numbers
- Complete all 8 pairs
- View moves and success rate

**Image Memory Game:**

- Match emoji pairs
- Visual recognition challenge
- Track performance

**Word Memory Game:**

- Match word pairs
- Verbal memory test
- Completion tracking

**Color Classification:**

- Drag items to blue/green categories
- Or click items to sort
- 12 items total
- Instant feedback

**Category Game:**

- Sort words into Animals/Foods
- 16 words to categorize
- Logical grouping test

### 4. Accessibility Tools

**Access via Sidebar → Tools**

**Speech to Text:**

1. Click **"Start Recording"**
2. Allow microphone permissions
3. Speak clearly
4. Transcript appears in real-time
5. Copy, download, or clear as needed

**Text to Speech:**

1. Type or paste text
2. Select voice and language
3. Adjust speed, pitch, volume
4. Click **"Speak"**
5. Use pause/resume/stop controls

---

## 🔌 API Documentation

### Base URL

```
http://localhost:5000
```

### Endpoints

#### 1. Diabetes Prediction

```http
POST /predict/diabetes
Content-Type: application/json

{
  "pregnancies": 1,
  "glucose": 85,
  "blood_pressure": 66,
  "skin_thickness": 29,
  "insulin": 0,
  "bmi": 26.6,
  "dpf": 0.351,
  "age": 31
}

Response:
{
  "prediction": 0,  // 0 = No Diabetes, 1 = Diabetes
  "message": "Prediction successful"
}
```

#### 2. Heart Disease Prediction

```http
POST /predict/heart
Content-Type: application/json

{
  "age": 45,
  "sex": 1,
  "cp": 3,
  "trestbps": 120,
  "chol": 200,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 0,
  "thal": 2
}

Response:
{
  "prediction": 0,  // 0 = No Disease, 1 = Disease
  "message": "Prediction successful"
}
```

#### 3. Parkinsons Prediction

```http
POST /predict/parkinsons
Content-Type: application/json

{
  "features": [
    119.992, 157.302, 74.997, 0.00784, 0.00007,
    0.00370, 0.00554, 0.01109, 0.04374, 0.426,
    0.02182, 0.03130, 0.02971, 0.06545, 0.02211,
    21.033, 0.414783, 0.815285, -4.813031,
    0.266482, 2.301442, 0.284654
  ]
}

Response:
{
  "prediction": 0,  // 0 = Healthy, 1 = Parkinsons
  "message": "Prediction successful"
}
```

#### 4. Autism Risk Prediction

```http
POST /predict/autism
Content-Type: application/json

{
  "A1_Score": 1,
  "A2_Score": 0,
  "A3_Score": 1,
  "A4_Score": 0,
  "A5_Score": 1,
  "A6_Score": 1,
  "A7_Score": 0,
  "A8_Score": 1,
  "A9_Score": 0,
  "A10_Score": 1,
  "age": 5
}

Response:
{
  "prediction": 1,  // 0 = Low Risk, 1 = High Risk
  "message": "Prediction successful"
}
```

### Error Handling

All endpoints return appropriate HTTP status codes:

- `200` - Success
- `400` - Bad Request (missing/invalid data)
- `500` - Internal Server Error

---

## 🎨 Design System

### Color Theme

- **Primary:** Beige (#EFECE3) → Grey (#8FABD4) → Blue (#4A70A9)
- **Gradient:** `from-[#EFECE3] via-[#8FABD4] to-[#4A70A9]`
- **Focus:** Ring color #4A70A9

### Glassmorphism Components

- **Background:** `bg-white/30` or `bg-white/80`
- **Backdrop:** `backdrop-blur-md`
- **Border:** `border-white/20` or `border-white/40`
- **Shadow:** `shadow-lg` or `shadow-xl`

### Animations

- **Fade In:** Custom keyframe animation
- **Fade In Up:** Scroll-triggered animations
- **Float:** Subtle hover effects
- **Scroll Down:** Animated indicators

### Responsive Breakpoints

- **sm:** 640px
- **md:** 768px
- **lg:** 1024px
- **xl:** 1280px
- **2xl:** 1536px

---

## 🧪 Testing

### Backend API Testing

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python test_api.py
```

### Manual Testing Checklist

- [ ] All disease predictors return valid results
- [ ] Autism questionnaire saves to localStorage
- [ ] Dashboard displays assessment results
- [ ] All 5 cognitive games are playable
- [ ] Speech-to-Text captures audio correctly
- [ ] Text-to-Speech plays audio with controls
- [ ] Form submission stores data
- [ ] Navigation works across all pages
- [ ] Responsive design on mobile/tablet
- [ ] Browser compatibility (Chrome, Edge, Firefox)

---

## 🔒 Security & Privacy

### Data Storage

- **Client-Side:** localStorage (assessment results, submissions)
- **No Server Storage:** Models run predictions without storing user data
- **Privacy:** No personal health data transmitted to external servers

### HIPAA Considerations

- Privacy notice included in submission form
- Users consent before sharing with centers
- Data handling guidelines provided

### Browser Permissions

- **Microphone:** Required for Speech-to-Text
- **Notifications:** Optional for toast messages

---

## 📊 Model Performance

### Diabetes Model (SVM)

- Training dataset: 768 samples
- Features: 8
- Expected accuracy: ~75-80%

### Heart Disease Model (Logistic Regression)

- Training dataset: 303 samples
- Features: 13
- Expected accuracy: ~80-85%

### Parkinsons Model (SVM)

- Training dataset: 195 samples
- Features: 22
- Expected accuracy: ~85-90%

### Autism Model (Random Forest)

- Training dataset: Custom autism.csv
- Features: 11
- Auto-generated on first run
- Risk classification: Low/Medium/High

---

## 🤝 Contributing

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- **Frontend:** Follow TypeScript/React best practices
- **Backend:** Follow PEP 8 Python style guide
- **Components:** Use existing UI component patterns
- **Styling:** Maintain glassmorphism design consistency

---

## 📝 License

This project is part of an academic final year project. All rights reserved.

---

## 👥 Authors & Acknowledgments

**Project Team:**

- Multiple Disease Prediction System Integration
- Autism Assessment Tools Development
- Cognitive Games Implementation
- UI/UX Design & Implementation

**Technologies & Libraries:**

- React Team (React, React Router)
- Flask Team (Flask framework)
- scikit-learn (Machine Learning)
- Tailwind Labs (Tailwind CSS)
- Radix UI (Component primitives)
- Lucide (Icon library)

---

## 📞 Support & Contact

For issues, questions, or contributions:

- Open an issue on GitHub
- Review documentation files (PROJECT_README.md, SETUP_COMPLETE.md)
- Check API documentation above

---

## 🗓️ Project Timeline & Milestones

### Phase 1: Foundation

- ✅ Backend API with 4 ML models
- ✅ Basic React frontend setup
- ✅ Model integration and testing

### Phase 2: Autism Assessment

- ✅ 20-question questionnaire
- ✅ Risk calculation algorithm
- ✅ Dashboard results display
- ✅ Professional center submission form

### Phase 3: Cognitive Games

- ✅ Number Memory Game
- ✅ Image Memory Game
- ✅ Word Memory Game
- ✅ Color Classification Game
- ✅ Category Sorting Game

### Phase 4: Accessibility & Tools

- ✅ Speech-to-Text functionality
- ✅ Text-to-Speech functionality
- ✅ Sidebar navigation organization
- ✅ Glassmorphism design system

### Phase 5: Polish & Documentation

- ✅ Comprehensive README
- ✅ Setup documentation
- ✅ API documentation
- ✅ Testing scripts

---

## 🔄 Future Enhancements

### Planned Features

- [ ] Backend database integration (PostgreSQL/MongoDB)
- [ ] User authentication and profiles
- [ ] Historical tracking of assessments
- [ ] PDF report generation
- [ ] Email notifications to centers
- [ ] Multi-language support
- [ ] Mobile app (React Native)
- [ ] Advanced analytics dashboard
- [ ] Telehealth consultation booking
- [ ] More cognitive assessment games

### Technical Improvements

- [ ] Model retraining pipeline
- [ ] Automated testing suite
- [ ] CI/CD pipeline setup
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/Azure)
- [ ] Performance optimization
- [ ] SEO optimization
- [ ] Accessibility compliance (WCAG 2.1)

---

## 📚 Additional Resources

### Documentation Files

- `PROJECT_README.md` - Detailed setup instructions
- `SETUP_COMPLETE.md` - Quick start guide
- `backend/README.md` - Backend-specific documentation

### Training Notebooks

Located in `colab_files_to_train_models/`:

- Diabetes prediction training
- Heart disease prediction training
- Parkinsons prediction training
- Autism prediction training

### Datasets

Located in `dataset/` and `Autism/`:

- diabetes.csv
- heart.csv
- parkinsons.csv
- autism.csv

---

**Last Updated:** November 27, 2025  
**Version:** 2.0.0  
**Status:** Active Development
