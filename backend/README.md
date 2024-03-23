
# Backend Service for Vapi AI Voice Assistant

This Flask application serves as the backend for the Vapi Voice Assistant, handling the creation and management of voice assistants via Vapi's API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip
- Vapi API Key
- Vapi Base URL

### Installing

First, clone the repository to your local machine:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd backend
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

1. Obtain your Vapi API key and base URL by registering or logging in at Vapi's developer portal. Learn more: https://vapi.ai

2. Create a `.env` file in the root directory of the project with the following content, replacing the placeholders with your actual Vapi API Key and Base URL:

```
VAPI_API_KEY=your_vapi_api_key_here
VAPI_BASE_URL=your_vapi_base_url_here
```

### Running the Application

To start the application, run:

```bash
python app.py
```

The application will start on `http://localhost:5000`. The main endpoint `/create-assistant` is used to create or update a voice assistant via a POST request.

## Using the Vapi API

This project makes requests to Vapi's API. For detailed information on the API endpoints and how to use them, check out the [Vapi API Reference](https://docs.vapi.ai/api-reference/swagger).

### License

This project is licensed under the MIT License.
