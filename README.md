# 🎅 Secret Santa Web Application

A festive Secret Santa application with real-time chat, polls, and a beautiful Christmas-themed UI. Participants can join rooms, exchange gift preferences, send secret messages, and reveal their Secret Santa pairs with a fun countdown animation.

## ✨ Features

- 🎄 **Christmas-themed UI** with festive design
- 🎁 **Secret Santa Assignment** with 5-second countdown reveal
- 💬 **Real-time Chat** with WhatsApp-style reactions and emojis
- 📊 **Interactive Polls** for group decisions
- 🔒 **Secret Messages** for gift recipients
- 🎯 **Custom Room Names** for better organization
- 📱 **Mobile-Responsive** design
- 👥 **Host Controls** to manage participants

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- MongoDB (local or MongoDB Atlas)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Santa
   ```

2. **Set up Python environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and update with your MongoDB connection string
   # For local MongoDB: MONGO_URL=mongodb://localhost:27017
   # For MongoDB Atlas: See DEPLOYMENT.md for instructions
   ```

5. **Run the application**
   ```bash
   # From the project root directory
   uvicorn backend.main:app --reload
   ```

6. **Open in browser**
   ```
   http://localhost:8000
   ```

## 🗄️ MongoDB Setup

### Option 1: Local MongoDB

1. Install MongoDB Community Edition from [mongodb.com](https://www.mongodb.com/try/download/community)
2. Start MongoDB service
3. Use default connection string in `.env`: `MONGO_URL=mongodb://localhost:27017`

### Option 2: MongoDB Atlas (Cloud)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed MongoDB Atlas setup instructions.

Quick steps:
1. Create free account at [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Add database user
4. Whitelist your IP address
5. Get connection string and update `.env`

## 📂 Project Structure

```
Santa/
├── backend/
│   ├── __init__.py
│   ├── main.py           # FastAPI application & routes
│   ├── database.py       # MongoDB connection
│   ├── models.py         # Data models
│   ├── santa.py          # Secret Santa assignment logic
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── index.html        # Main HTML
│   ├── script.js         # Application logic
│   └── notifications.js  # Notification system
├── .env                  # Environment variables (gitignored)
├── .env.example          # Environment template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🎮 How to Use

1. **Create a Room**: Host enters their name and optionally sets a custom room name
2. **Share Room Code**: Other participants join using the 6-character room code
3. **Add Preferences**: Everyone adds their gift preferences and optional secret message
4. **Start Game**: Host starts the Secret Santa assignment
5. **View Assignment**: Each participant sees their assigned giftee with a countdown reveal
6. **Chat & Poll**: Use real-time chat and polls to coordinate

## 🔧 Configuration

Edit `.env` file to configure:

- `MONGO_URL`: MongoDB connection string
- `DB_NAME`: Database name (default: secret_santa_db)
- `CORS_ORIGINS`: Allowed origins for CORS (comma-separated)

## 🚢 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions including:
- MongoDB Atlas setup
- Deploying to Render
- Deploying to Railway
- Deploying to Heroku

## 🛠️ Development

```bash
# Run with auto-reload
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Access API docs
http://localhost:8000/docs
```

## 📝 API Endpoints

- `GET /` - API status
- `GET /health` - Health check
- `POST /api/rooms` - Create room
- `GET /api/rooms/{code}` - Get room details
- `POST /api/rooms/join` - Join room
- `POST /api/rooms/{code}/start` - Start game
- `WebSocket /ws/{room_code}/{user_name}` - Real-time chat

Full API documentation at `/docs` when running.

## 🤝 Contributing

Feel free to open issues or submit pull requests!

## 📄 License

MIT License - feel free to use this project for your own Secret Santa events!

## 🎄 Happy Holidays! 🎅
