# words_counter Django Project

This is the **words_counter** Django project, a simple web application that counts words in a given text. It's built using Django and Docker Compose for easy development and deployment.

## Getting Started

These instructions will help you set up and run the project locally.

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/CHRNVpy/words_counter.git
   cd words_counter

2. Build and start the Docker containers:

    ```bash
   docker-compose up -d
   
This command will download the necessary Docker images, build the project, and start the containers in detached mode.

3. Migrate the database and create a superuser:

    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
4. Replace example ssl keys in Words_counter/ssl with your own.
   
5. Access the application in your web browser:

Open your web browser and go to http://localhost or you domain

### Usage
1. Access the home page at http://localhost or your domain

2. Upload PDf or docx file to file upload form to get document words count.

### Deployment

For production deployment, copy project files on your server, edit allowed hosts(settings/prod.py, config/nginx/template), 
env path (docker_compose.yml), and run:
   ```bash
   docker-compose up -d
