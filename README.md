
# 📸 PhotoVerse

> A minimal, dark-themed photography community platform where users can upload, discover, like, save, and comment on beautiful photography.

---

## 📖 Overview

PhotoVerse is a community-driven photography web application inspired by the clean visual experience of Pinterest and Pexels. It focuses on showcasing photography through a responsive masonry layout while providing social features such as likes, comments, and saved photos.

The goal is to create a distraction-free platform where photography remains the center of attention.

---

# ✨ Features

## Authentication

- User Registration
- User Login
- Secure JWT Authentication
- User Logout
- Edit Profile

## User Profile

- Profile Picture
- Username
- Bio
- Personal Gallery

## Photography

- Upload Photos
- Edit Photo Details
- Delete Photos
- Categories
- Tags
- Masonry Gallery

## Community

- Like / Unlike Photos
- Save / Remove Saved Photos
- Comment on Photos
- Delete Own Comments

## UI

- Dark Theme
- Responsive Design
- Infinite Scrolling
- Masonry Image Layout
- Mobile Friendly (PWA)

---

# 🛠 Tech Stack

## Frontend

- React
- Tailwind CSS
- Framer Motion

## Backend

- Python
- Django
- Django REST Framework

## Database

- MongoDB

## Image Storage

- Cloudinary

## Deployment

- Frontend: Vercel
- Backend: Render

---

# 📁 Project Structure

```
PhotoVerse/

│
├── frontend/
│   ├── src/
│   ├── public/
│   └── ...
│
├── backend/
│   ├── authentication/
│   ├── users/
│   ├── photos/
│   ├── comments/
│   ├── categories/
│   └── ...
│
├── docs/
│
└── README.md
```

---

# 🗄 Database Collections

- Users
- Photos
- Categories
- Comments
- Likes
- Saved Photos

---

# 🖼 Image Storage

Images are stored in Cloudinary.

MongoDB stores only metadata such as:

- Image URL
- Title
- Description
- Tags
- Category
- Owner
- Upload Date

---

# 🚀 Installation

## Clone Repository

```bash
git clone <repository-url>
```

---

## Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Backend

```bash
cd backend

python -m venv venv

# Activate virtual environment

pip install -r requirements.txt

python manage.py runserver
```

---

# 🔑 Environment Variables

Backend

```
SECRET_KEY=

DEBUG=

MONGODB_URI=

CLOUDINARY_CLOUD_NAME=

CLOUDINARY_API_KEY=

CLOUDINARY_API_SECRET=

JWT_SECRET=
```

Frontend

```
VITE_API_URL=
```

---

# 📌 Development Roadmap

## Phase 1

- Project Setup
- Authentication
- Database Configuration

---

## Phase 2

- Photo Upload
- Cloudinary Integration
- Gallery
- Categories

---

## Phase 3

- Like System
- Save System
- Comments

---

## Phase 4

- User Profiles
- UI Polish
- Responsive Design

---

## Phase 5

- Deployment
- Performance Optimization
- Bug Fixes

---

# 🎯 MVP Scope

✅ Authentication

✅ User Profiles

✅ Upload Photos

✅ Categories

✅ Likes

✅ Saves

✅ Comments

✅ Masonry Gallery

---

# 🔮 Future Improvements

- Notifications
- Image Collections
- EXIF Camera Information
- AI Generated Tags
- Admin Dashboard
- Content Moderation
- Advanced Filtering
- Light Theme

---

# 📚 API Modules

- Authentication API
- User API
- Photo API
- Category API
- Comment API
- Like API
- Save API

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed as a solo full-stack project using Django REST Framework, React, MongoDB, and Cloudinary.
