# PROJECT: Medication Reminder

Project Medication Reminder is an application that allows users to manage and track their medication schedules.

The project is a full stack FastAPI, PostgreSQL and React application that is built to run on Docker.

## Team:

- Onkur Lal
- Michael Zinzun
- Dennie Chan

### Database Models Design

The diagram below showcases the various database models utilized in our project and their relationship to one another.

![](docs/images/API-Design.png)

### Backend API Endpoints

Here are diagrams of the API endpoints serving our project:

**Medications API**
![](docs/images/Medications-endpoints.jpg)

**Pharmacy API**
![](docs/images/Pharmacy-endpoints.jpg)

**Doctors API**
![](docs/images/Doctors-endpoints.jpg)

**User Account API**
![](docs/images/user-account-endpoints.jpg)

**User Profile API**
![](docs/images/user-profile-endpoints.jpg)

### Steps to Run the Project

1. Fork the project located at [Module3 Project Gamma](https://gitlab.com/Onkurlal/module3-project-gamma)
2. Once the project is forked, close via git clone https link.
3. Once cloned, cd into app directory and run the following commands:
4. docker volume create example_db
5. docker-compose build
6. docker-compose up
