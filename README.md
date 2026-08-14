🚀 CareerGraph

<p align="center">
  <strong>Graph-Powered Career Exploration & Skill Recommendation Platform</strong>
</p>

<p align="center">
  Discover suitable careers from your existing skills, identify skill gaps,
  and get practical learning and project recommendations.
</p>

<p align="center">
  <a href="https://careergraph-task-v3m0.onrender.com">
    <img src="https://img.shields.io/badge/🌐%20Live%20Demo-CareerGraph-5B4CE2?style=for-the-badge" alt="Live Demo">
  </a>
  <a href="https://github.com/shannu1653/careergraph_task">
    <img src="https://img.shields.io/badge/💻%20GitHub-Repository-black?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/CognoDB-Graph%20Database-5B4CE2?style=flat-square" alt="CognoDB">
  <img src="https://img.shields.io/badge/Cypher-Query%20Language-orange?style=flat-square" alt="Cypher">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square&logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=flat-square&logo=render" alt="Render">
</p>

🌐 Live Application

Live Demo:
https://careergraph-task-v3m0.onrender.com

Source Code:
https://github.com/shannu1653/careergraph_task

📌 About CareerGraph

CareerGraph is a graph-powered career exploration and skill recommendation platform.

The application connects a user's existing skills with suitable career paths and provides actionable recommendations for career development.

Instead of simply displaying a career name, CareerGraph helps users understand:

🎯 Which careers match their current skills

📊 How closely their skills match a career

🧩 Which skills they are missing

📚 Which courses can help them develop those skills

🏢 Which companies are associated with the selected career

💻 Which practical projects can help them improve their skills

The application uses CognoDB as a graph database to represent relationships between users, skills, job roles, courses, companies, and projects.

✨ Key Features

Feature

Description

👤 User Skills

Displays the user's existing skills and proficiency levels

🎯 Career Matching

Finds suitable career paths based on the user's skills

📊 Match Percentage

Shows how closely the user's skills match a career

🧩 Skill Gap Analysis

Identifies missing skills required for a selected career

📚 Course Recommendations

Recommends courses related to missing skills

🏢 Company Recommendations

Displays companies associated with the selected career

💻 Project Recommendations

Suggests practical projects for skill development

🔗 Graph Traversal

Uses connected graph relationships to generate recommendations

🌐 REST API

Flask-based API for frontend and backend communication

☁️ Cloud Deployment

Application deployed using Render

🛠️ Tech Stack

Backend

Python

Flask

Neo4j Python Driver

Cypher

Database

CognoDB

Graph Database

Frontend

HTML5

CSS3

JavaScript ES6

Fetch API

DOM Manipulation

Development & Deployment

Git

GitHub

Render

🧠 Graph Database Model

CareerGraph represents career information as connected graph entities.

Main Entities

User
Skill
Job Role
Course
Company
Project

Main Relationships

User
 │
 └── HAS_SKILL ──────────► Skill
                            │
                            │ REQUIRED_FOR
                            ▼
                         Job Role
                        /    |    \
                       /     |     \
                      ▼      ▼      ▼
                   Course  Company  Project

The graph structure allows CareerGraph to navigate relationships between different entities and generate career recommendations.

🔄 Career Recommendation Flow

The recommendation process follows a simple workflow:

┌─────────────────────┐
│     User Skills     │
│                     │
│ Python              │
│ SQL                 │
│ Django              │
│ Git                 │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Career Matching   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Select Career    │
└──────────┬──────────┘
           │
     ┌─────┼───────────────┬──────────────┐
     ▼     ▼               ▼              ▼
┌────────┐ ┌──────────┐ ┌───────────┐ ┌──────────┐
│Missing │ │ Courses  │ │ Companies │ │ Projects │
│Skills  │ │          │ │           │ │          │
└────────┘ └──────────┘ └───────────┘ └──────────┘

Recommendation Pipeline

Current Skills
      ↓
Career Matching
      ↓
Select Career
      ↓
Skill Gap Analysis
      ↓
Course Recommendations
      ↓
Company Recommendations
      ↓
Project Recommendations

This provides the user with a complete and actionable career-development path.

🏗️ Application Architecture

                         USER
                           │
                           ▼
                ┌────────────────────┐
                │      Frontend      │
                │    HTML / CSS / JS │
                └─────────┬──────────┘
                          │
                      HTTP / JSON
                          │
                          ▼
                ┌────────────────────┐
                │      Flask API     │
                │      Backend       │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   Cypher Queries   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    Neo4j Driver    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │      CognoDB       │
                │   Graph Database   │
                └────────────────────┘

🔌 REST API

CareerGraph provides REST APIs for communication between the frontend, Flask backend, and graph database.

❤️ Health Check

Endpoint

GET /api/health

Checks whether the Flask API and CognoDB connection are available.

Local

http://127.0.0.1:5000/api/health

Production

https://careergraph-task-v3m0.onrender.com/api/health

Expected Response

{
  "success": true,
  "api": "running",
  "database": "connected"
}

🧠 Get All Skills

Endpoint

GET /api/skills

Returns the available skills.

💼 Get All Job Roles

Endpoint

GET /api/jobs

Returns the available career/job roles.

👤 Get User Skills

Endpoint

GET /api/users/<user_id>/skills

Returns the skills associated with a user.

Example

GET /api/users/user_001/skills

🎯 Get Career Matches

Endpoint

GET /api/users/<user_id>/career-matches

Returns career roles that match the user's existing skills.

Example

GET /api/users/user_001/career-matches

🧩 Get Missing Skills

Endpoint

GET /api/users/<user_id>/missing-skills/<role_id>

Returns the skills that the user needs to develop for the selected career.

📚 Get Recommended Courses

Endpoint

GET /api/users/<user_id>/courses/<role_id>

Returns courses related to the skills required for the selected career.

🏢 Get Related Companies

Endpoint

GET /api/jobs/<role_id>/companies

Returns companies associated with the selected career.

💻 Get Recommended Projects

Endpoint

GET /api/users/<user_id>/projects/<role_id>

Returns practical projects related to the selected career.

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
│   ├── favicon.svg
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── app.js
│
├── templates/
│   └── index.html
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── run.py
├── test_connection.py
└── test_queries.py

⚙️ Local Setup

Follow these steps to run CareerGraph locally.

1️⃣ Clone the Repository

git clone https://github.com/shannu1653/careergraph_task.git

Move into the project directory:

cd careergraph_task

2️⃣ Create a Virtual Environment

Windows

python -m venv venv

Linux / macOS

python3 -m venv venv

3️⃣ Activate the Virtual Environment

Windows PowerShell

venv\Scripts\activate

Windows CMD

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

4️⃣ Install Dependencies

pip install -r requirements.txt

🔐 Environment Configuration

CareerGraph uses environment variables for database configuration.

Create a .env file in the project root:

NEO4J_URI=your_cognodb_uri
NEO4J_USERNAME=your_username
NEO4J_PASSWORD=your_password

⚠️ Important: Never upload your .env file to GitHub.

The project includes .env.example as a safe configuration template.

🌱 Seed the Database

Run the database seed script:

python -m scripts.seed_database

This creates the required graph data in CognoDB.

🔍 Test Database Connection

Run:

python test_connection.py

This verifies that the application can connect to the configured graph database.

▶️ Run the Application

Start the Flask application:

python run.py

The application should be available at:

http://127.0.0.1:5000

Open the URL in your browser.

🧪 Testing

Database Connection Test

python test_connection.py

Query Test

python test_queries.py

Local API Health Check

http://127.0.0.1:5000/api/health

Production API Health Check

https://careergraph-task-v3m0.onrender.com/api/health

Expected Response

{
  "success": true,
  "api": "running",
  "database": "connected"
}

☁️ Deployment

CareerGraph is deployed using Render.

Build Command

pip install -r requirements.txt

Start Command

gunicorn run:app

Production Environment Variables

Configure the following variables in the Render dashboard:

NEO4J_URI
NEO4J_USERNAME
NEO4J_PASSWORD

Production database credentials should be stored securely using Render environment variables.

👨‍💻 Example User Journey

Suppose a user has the following skills:

Python
SQL
Django
Git

CareerGraph analyzes these skills and identifies suitable career paths.

The user can then select a career and receive personalized recommendations.

Current Skills
      ↓
Career Match
      ↓
Select Career
      ↓
Missing Skills
      ↓
Recommended Courses
      ↓
Relevant Companies
      ↓
Practical Projects

Example

User Skills
    │
    ├── Python
    ├── SQL
    ├── Django
    └── Git
         │
         ▼
   Career Matching
         │
         ▼
    Python Developer
         │
    ┌────┼───────────────┐
    ▼    ▼               ▼
 Skills Courses       Projects
   Gap

This allows users to understand not only which career suits them, but also what they should learn next.

🎯 Why CareerGraph?

Traditional career recommendation systems may simply suggest a job title.

CareerGraph goes one step further by connecting:

Skills
  ↓
Career Roles
  ↓
Skill Gaps
  ↓
Courses
  ↓
Companies
  ↓
Projects

This graph-based approach helps turn a career recommendation into an actionable learning roadmap.

💡 Key Project Highlights

Graph-based career recommendation

Skill matching

Skill gap analysis

Course recommendations

Company recommendations

Project recommendations

REST API architecture

Flask backend

Graph database integration

Cypher queries

HTML/CSS/JavaScript frontend

Cloud deployment using Render

Environment-based configuration

Database connection and query testing

🔗 Important Links

Resource

Link

🌐 Live Application

CareerGraph

💻 GitHub Repository

careergraph_task

📌 Project Summary

CareerGraph demonstrates the practical use of a graph database for career exploration and skill recommendations.

The application connects users' existing skills with career roles and then uses graph relationships to identify:

Required skills

Missing skills

Recommended courses

Relevant companies

Practical projects

The overall recommendation pipeline is:

User Skills
     ↓
Career Matching
     ↓
Skill Gap Analysis
     ↓
Course Recommendations
     ↓
Company Recommendations
     ↓
Project Recommendations

By combining Python, Flask, JavaScript, REST APIs, Cypher, and graph database technology, CareerGraph provides a practical platform for personalized career exploration.

<p align="center">
  <strong>🚀 CareerGraph</strong>
  <br>
  <sub>Discover where your skills can take you.</sub>
</p>