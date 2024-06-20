
# Employee Management App

`employee-management-app` is a microservices-based CRUD application that provides APIs for managing employee data. This project uses FastAPI for the backend services, Redis for OAuth2 authentication and caching, and SQLite as the database. The application is containerized using Docker and orchestrated with Docker Compose.

## Project Structure

The project consists of two main FastAPI services and a Redis service:
- **fastapi-oauth2**: Handles user authentication using OAuth2.
- **fastapi-employee**: Manages CRUD operations for employee data.
- **redis-queue**: Caches data and handles background tasks.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Environment Variables

Create a `.env` file in the root directory with the following environment variables:

```env
PORT_FASTAPI_OAUTH2=8001
PORT_FASTAPI_EMPLOYEE=8002
PORT_REDIS=6379
REDIS_PASSWORD=your_redis_password
HOST=localhost
API_PATH_FASTAPI_OAUTH2=/api/v1/oauth2
API_PATH_FASTAPI_EMPLOYEE=/api/v1/employee
```

### Building and Running the Application

To build and start the application, run the following command in the root directory of the project:

```bash
docker-compose up --build
```

This command will build the Docker images for the FastAPI services and start the containers along with the Redis service.

### Accessing the Services

- FastAPI OAuth2 Service: `http://localhost:${PORT_FASTAPI_OAUTH2}${API_PATH_FASTAPI_OAUTH2}`
- FastAPI Employee Service: `http://localhost:${PORT_FASTAPI_EMPLOYEE}${API_PATH_FASTAPI_EMPLOYEE}`
- Redis: `redis://localhost:${PORT_REDIS}` (requires password)

### Logs and Data

- Logs for the FastAPI services are stored in `./backend/fastapi-oauth2/logs` and `./backend/fastapi-employee/logs`.
- Redis data is persisted in the `redis_queue_data` volume.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.