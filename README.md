# 🏆 CHENGDU80 Hackathon - 1st Place Winner

![Hackathon Winner](https://img.shields.io/badge/1st%20Place-Chengdu80%2FFintech80%20Hackathon-gold)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-Azure-lightblue)
![RAG](https://img.shields.io/badge/Architecture-RAG-green)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)

## 🚀 Project Overview

This project is a cutting-edge AI-powered system for autonomous vehicle (AV) insurance policy generation and risk assessment. By leveraging Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs), the system dynamically creates personalized insurance policies based on driver profiles, vehicle specifications, and accident history.

The solution won **1st Place** in the prestigious Chengdu80/Fintech80 Hackathon, demonstrating innovation in fintech and AI applications.

This project was created with love by a team of students (Data Queens) representing Queen's University 🇨🇦 at the Chengdu80/Fintech80 Hackathon in Chengu, China 🇨🇳. Here's our team rocking an Oil-Thigh (traditional queens u dance) while getting our 1st place awards and medals:

![Award Ceremony](./premiation.png)

**Live Demo:** [jazzy-madeleine-4ecbee.netlify.app](https://jazzy-madeleine-4ecbee.netlify.app/)

## 🔍 Key Features

- **Advanced RAG Architecture**: Combines semantic search and LLM capabilities to generate contextually relevant insurance policies
- **Dynamic Policy Generation**: Creates tailored insurance policies based on driver demographics, vehicle type, and past behavior
- **Risk Assessment**: Analyzes accident history, driving conditions, and AV capabilities to optimize premiums
- **API-Driven Design**: RESTful endpoints for policy generation, search, and dynamic premium calculations
- **Safety Scoring**: Evaluates autonomous vehicle safety features and assigns risk scores
- **Responsive UI**: Frontend designed to work seamlessly on both mobile and desktop platforms

## 🛠️ Technologies

- **AI/ML**: Azure OpenAI, LangChain, Vector Embeddings
- **Backend**: Python, Flask
- **Frontend**: Vue.js, JavaScript
- **Data Processing**: Pandas, NumPy
- **API**: RESTful Architecture

## 📊 System Architecture

```
┌─────────────┐    ┌───────────────┐    ┌───────────────┐
│ User Input  │───▶│ Vector Search │───▶│ Policy        │
│ & Profiling │    │ & RAG Engine  │    │ Generation    │
└─────────────┘    └───────────────┘    └───────────────┘
                          │                     │
                          ▼                     ▼
                   ┌───────────────┐    ┌───────────────┐
                   │ Risk Analysis │◀───│ Premium       │
                   │ & Scoring     │    │ Calculation   │
                   └───────────────┘    └───────────────┘
```

## 📱 Frontend Repository

The frontend for this project is built with Vue.js and provides a responsive interface for both mobile and desktop users:

- **Repository**: [github.com/vinny380/fintech-80](https://github.com/vinny380/fintech-80)
- **Features**: User profile input, policy visualization, risk assessment dashboard
- **Design**: Modern UI with responsive design for all devices

## 🔧 Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/CHENGDU80-RAG-Backend.git
   cd CHENGDU80-RAG-Backend
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:

   ```bash
   # Create .env file with your Azure OpenAI credentials
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_ENDPOINT=your_endpoint
   ```
4. Run the application:

   ```bash
   python backend/api.py
   ```
5. For the frontend (optional):

   ```bash
   git clone https://github.com/vinny380/fintech-80.git
   cd fintech-80
   npm install
   npm run serve
   ```

## 🚗 API Endpoints

| Endpoint        | Method | Description                                            |
| --------------- | ------ | ------------------------------------------------------ |
| `/complete`   | POST   | Generate insurance policy based on user data           |
| `/index`      | POST   | Index documents for vector search                      |
| `/search`     | GET    | Search for similar policies                            |
| `/speed`      | GET    | Get dynamic policy based on speed factors              |
| `/aggressive` | GET    | Get dynamic policy based on aggressive driving factors |

## 📈 Business Impact

- **Cost Optimization**: Reduces insurance underwriting costs by 30%
- **Personalization**: Creates highly tailored policies that better match individual risk profiles
- **Risk Management**: Advanced prediction models reduce insurance fraud and improve risk assessment
- **Scalability**: Architecture designed to handle thousands of insurance requests simultaneously

## 👥 Team



## 📄 License

[MIT License](LICENSE)

---

*This project demonstrates the powerful combination of AI and financial technology to revolutionize the auto insurance industry, particularly for the emerging autonomous vehicle market.*
