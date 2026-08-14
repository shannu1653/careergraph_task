🚀 CareerGraph

<p align="center">
  <strong>Graph-Powered Career Exploration & Skill Recommendation Platform</strong>
</p>

<p align="center">
  Discover suitable careers from your skills, identify skill gaps, and get practical learning and project recommendations.
</p>

<p align="center">
  <a href="https://careergraph-task-v3m0.onrender.com"><img src="https://img.shields.io/badge/🌐%20Live%20Demo-CareerGraph-5B4CE2?style=for-the-badge" alt="Live Demo"></a>
  <a href="https://github.com/shannu1653/careergraph_task"><img src="https://img.shields.io/badge/💻%20GitHub-Repository-black?style=for-the-badge&logo=github" alt="GitHub"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/Flask-3.x-black?style=flat-square">
  <img src="https://img.shields.io/badge/CognoDB-Graph%20Database-5B4CE2?style=flat-square">
  <img src="https://img.shields.io/badge/Cypher-orange?style=flat-square">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square&logo=javascript">
</p>

📌 Overview

CareerGraph is a graph-based career exploration application built with CognoDB.

It connects a user's existing skills to suitable career roles and uses graph relationships to identify:

🎯 Career matches

🧩 Missing skills

📚 Recommended courses

🏢 Relevant companies

💻 Practical projects

The goal is to turn a career recommendation into an actionable learning roadmap.

💡 Why a Graph Database?

Career recommendations are naturally relationship-driven. A user's skills can connect to multiple careers, while each career connects to required skills, courses, companies, and projects.

A graph model makes these connections explicit and makes multi-hop relationship queries natural compared with repeatedly joining relational tables.

User
 │
 └── HAS_SKILL ──► Skill
                    │
                    └── REQUIRED_FOR ──► Job Role
                                           │
                           ┌───────────────┼───────────────┐
                           ▼               ▼               ▼
                        Course         Company          Project

✨ Key Features

Feature

Purpose

🎯 Career Matching

Finds career roles related to existing skills

📊 Match Percentage

Shows the strength of a career match

🧩 Skill Gap Analysis

Identifies missing skills

📚 Course Recommendations

Suggests learning resources

🏢 Company Recommendations

Shows companies related to a career

💻 Project Recommendations

Suggests practical projects

🔗 Graph Traversal

Uses connected graph relationships

🌐 REST API

Connects frontend and backend

☁️ Hosted Demo

Provides an online application

🧠 Data Model

Nodes

User
Skill
Job Role
Course
Company
Project

Relationships

User ──HAS_SKILL──► Skill
Skill ──REQUIRED_FOR──► Job Role
Job Role ──RELATED_TO──► Course
Job Role ──RELATED_TO──► Company
Job Role ──RELATED_TO──► Project

🔄 Application Flow

User Skills
     ↓
Career Matching
     ↓
Select Career
     ↓
Skill Gap Analysis
     ↓
Courses + Companies + Projects

Example:

Python + SQL + Django + Git
              ↓
       Career Matching
              ↓
      Python Developer
              ↓
        Missing Skills
              ↓
     Courses / Projects
              ↓
       Relevant Companies

🏗️ Architecture

┌──────────────────────┐
│       Frontend       │
│   HTML / CSS / JS    │
└──────────┬───────────┘
           │ HTTP / JSON
           ▼
┌──────────────────────┐
│      Flask API       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Cypher Queries     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Neo4j Driver      │
└──────────┬───────────┘
           │ Bolt
           ▼
┌──────────────────────┐
│       CognoDB        │
│   Graph Database     │
└──────────────────────┘

🛠️ Tech Stack

Backend: Python, Flask, Official Neo4j Python Driver, Cypher
Database: CognoDB, openCypher, Bolt
Frontend: HTML5, CSS3, JavaScript ES6, Fetch API, DOM
Deployment: Render

🔌 Main API Endpoints

Method

Endpoint

Purpose

GET

/api/health

API & database health

GET

/api/skills

Get available skills

GET

/api/jobs

Get career roles

GET

/api/users/<user_id>/skills

Get user skills

GET

/api/users/<user_id>/career-matches

Get career matches

GET

/api/users/<user_id>/missing-skills/<role_id>

Get skill gaps

GET

/api/users/<user_id>/courses/<role_id>

Get recommended courses

GET

/api/jobs/<role_id>/companies

Get related companies

GET

/api/users/<user_id>/projects/<role_id>

Get recommended projects

📁 Project Structure

careergraph_task/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── queries.py
│   └── routes.py
│
├── scripts/
│   ├── __init__.py
│   └── seed_database.py
│
├── static/
│   ├── css/style.css
│   └── js/app.js
│
├── templates/index.html
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
├── test_connection.py
├── test_queries.py
└── README.md

⚙️ Local Setup

1. Clone

git clone https://github.com/shannu1653/careergraph_task.git
cd careergraph_task

2. Virtual Environment

python -m venv venv

Windows PowerShell:

venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment

Create .env in the project root:

NEO4J_URI=your_cognodb_uri
NEO4J_USERNAME=your_username
NEO4J_PASSWORD=your_password

⚠️ Never commit .env or database credentials to GitHub.

5. Seed Data

python -m scripts.seed_database

6. Run

python run.py

Open http://127.0.0.1:5000.

🧪 Testing

python test_connection.py
python test_queries.py

Health check:

http://127.0.0.1:5000/api/health

Expected response:

{
  "success": true,
  "api": "running",
  "database": "connected"
}

☁️ Deployment

Hosted on Render.

Build Command

pip install -r requirements.txt

Start Command

gunicorn run:app

Configure:

NEO4J_URI
NEO4J_USERNAME
NEO4J_PASSWORD

🖥️ Screenshots

The assignment requires UI screenshots in the README. Add 2–3 final screenshots such as:

docs/
├── dashboard.png
├── career-matches.png
└── recommendations.png

Then use:

![CareerGraph Dashboard](docs/dashboard.png)
![Career Matches](docs/career-matches.png)
![Recommendations](docs/recommendations.png)

🌐 Links

Resource

Link

🌐 Live Demo

CareerGraph

💻 GitHub

careergraph_task

🎯 Assignment Highlights

This project demonstrates:

Thoughtful graph data modeling

Realistic seeded graph data

Cypher queries and multi-hop traversal

Parameterized database queries

Functional web application

Clean UI/UX

Environment-based configuration

Database error handling

Hosted application deployment

<p align="center">
  <strong>🚀 CareerGraph</strong><br>
  <sub>Discover where your skills can take you.</sub>
</p>