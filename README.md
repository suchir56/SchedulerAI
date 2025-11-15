# SchedulerAI

An AI-powered course scheduling chatbot designed to help students plan their next semester's schedule at Carnegie Mellon University.

## Quick Start

### Backend Setup:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Frontend Setup (in new terminal):
```bash
cd frontend
npm install
npm run dev
```

### Access the App:
- **Frontend**: http://localhost:5174
- **API Docs**: http://localhost:8000/docs

---

## Features

- **PDF Upload**: Upload degree requirements and course audit documents
- **AI Chatbot**: Interactive conversation to help plan your schedule
- **CMU Course API Integration**: Access real-time course information
- **Smart Recommendations**: Get course suggestions based on your requirements and completed courses
- **Prerequisite Checking**: Automatic validation of course prerequisites

## Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **CMU Course API**: Real-time CMU course data
- **OpenAI API**: AI-powered chatbot (placeholder key included)
- **PyPDF2**: PDF text extraction

### Frontend
- **React**: Modern UI framework
- **Vite**: Fast build tool
- **Axios**: HTTP client

## Project Structure

```
SchedulerAI/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── models/       # Data schemas
│   │   ├── services/     # Business logic
│   │   ├── config.py     # Configuration
│   │   └── main.py       # FastAPI app
│   ├── uploads/          # PDF uploads (auto-created)
│   ├── requirements.txt  # Python dependencies
│   ├── .env             # Environment variables
│   └── run.py           # Run script
├── frontend/
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── App.jsx      # Main app
│   │   └── main.jsx     # Entry point
│   ├── package.json     # Node dependencies
│   └── index.html       # HTML template
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - The `.env` file is already created with a placeholder API key
   - To use a real OpenAI API key, edit `backend/.env`:
     ```
     OPENAI_API_KEY=your-actual-api-key-here
     ```

5. **Run the backend**:
   ```bash
   python run.py
   ```

   The API will start at `http://localhost:8000`

   API Documentation: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory** (in a new terminal):
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the development server**:
   ```bash
   npm run dev
   ```

   The app will start at `http://localhost:5174`

## Usage Guide

### 1. Start Both Servers

Make sure both backend (port 8000) and frontend (port 5174) are running.

### 2. Open the Application

Navigate to `http://localhost:5174` in your web browser.

### 3. Upload Documents

- **Degree Requirements PDF**: Upload your major's degree requirements
- **Course Audit PDF**: Upload your transcript/course audit showing completed courses

### 4. Chat with the Assistant

Start a conversation with the chatbot:
- Ask about course recommendations
- Inquire about prerequisites
- Request schedule planning help
- Get information about specific courses

### Example Conversations

**Example 1:**
```
You: I'm planning for Spring 2025. What courses should I take?
Bot: I'd be happy to help! Based on your degree requirements, what year
     are you in, and what areas are you most interested in?
```

**Example 2:**
```
You: Can I take 15-213 next semester?
Bot: Let me check the prerequisites for 15-213 (Introduction to Computer
     Systems). According to the course data, you need to have completed
     15-122. Based on your course audit, you have completed this course,
     so you're eligible!
```

**Example 3:**
```
You: I need to fulfill my humanities requirement. What do you recommend?
Bot: Based on your degree requirements and the current course offerings,
     here are some humanities courses that might interest you...
```

## API Endpoints

### Upload Endpoints

- `POST /api/upload/degree-requirements` - Upload degree requirements PDF
- `POST /api/upload/course-audit` - Upload course audit PDF

### Chat Endpoints

- `POST /api/chat` - Send a message to the chatbot

### Course Endpoints

- `GET /api/courses/{semester}/{course_id}` - Get specific course details
- `GET /api/courses/{semester}/search?query={query}` - Search courses

### Documentation

- `GET /docs` - Interactive API documentation (Swagger UI)

## Configuration

### Environment Variables

Edit `backend/.env` to configure:

```env
# AI Provider API Key
OPENAI_API_KEY=your-api-key-here

# Application Settings
BACKEND_PORT=8000
FRONTEND_URL=http://localhost:5174

# Upload Settings
MAX_UPLOAD_SIZE=10485760  # 10MB
UPLOAD_DIR=./uploads
```

### Semester Codes

When querying courses, use these semester codes:
- `S25` - Spring 2025
- `F24` - Fall 2024
- `M124` - Summer 1 2024
- `M224` - Summer 2 2024

## Troubleshooting

### Backend Issues

**Error: "No module named 'app'"**
- Make sure you're running `python run.py` from the `backend/` directory
- Ensure your virtual environment is activated

**Error: "Failed to fetch course data"**
- The CMU Course API might be temporarily unavailable
- Check your internet connection

**Error: "OpenAI API error"**
- Verify your API key is correctly set in `backend/.env`
- Check your OpenAI account has available credits

### Frontend Issues

**Error: "Network Error" or "Cannot connect to backend"**
- Ensure the backend is running on port 8000
- Check that both servers are running

**Error: "Upload failed"**
- Ensure the file is a valid PDF
- Check file size is under 10MB
- Verify uploads directory exists and has write permissions

### PDF Upload Issues

**No text extracted from PDF**
- Some PDFs are image-based and require OCR (not currently supported)
- Try using a different PDF or a text-based version

## Development

### Running Tests

```bash
# Backend tests (if added)
cd backend
pytest

# Frontend tests (if added)
cd frontend
npm test
```

### Building for Production

**Frontend:**
```bash
cd frontend
npm run build
```

The build output will be in `frontend/dist/`

## Future Enhancements

Potential features to add:
- [ ] Schedule visualization (calendar view)
- [ ] Course conflict detection
- [ ] FCE (Faculty Course Evaluation) integration
- [ ] Save and export schedules
- [ ] Multiple semester planning
- [ ] Course rating and difficulty information
- [ ] Mobile responsive design improvements
- [ ] User authentication and saved sessions
- [ ] OCR support for image-based PDFs

## Contributing

This is a local development project. To contribute:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit for review

## License

This project is for educational purposes.

## Support

For issues or questions:
- Check the troubleshooting section above
- Review the API documentation at `http://localhost:8000/docs`
- Ensure all dependencies are properly installed

## Credits

- **CMU Course API** by ScottyLabs
- **FastAPI** framework
- **React** library
- **OpenAI** for AI capabilities