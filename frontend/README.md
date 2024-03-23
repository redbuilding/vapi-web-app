
# Frontend for Vapi AI Voice Assistant

This Vue.js application provides a user interface for interacting with the Vapi Voice Assistant, allowing users to start and stop voice calls.

Note that each time you start a call, an Assistant is created with Vapi through interaction with the app's backend. You may want to alter this depending on your app's requirements.

Each time a call is ended, an end-of-call report will be sent to your external server, as identified in the Assistant creation.

## Getting Started

These instructions will guide you through setting up and running the project on your local machine for development and testing purposes.

### Prerequisites

- Node.js and npm
- Vue CLI

### Installing

Clone the repository to your local machine:

```bash
git clone <repository-url>
```

Navigate into the frontend directory:

```bash
cd frontend
```

Install the required npm packages:

```bash
npm install
```

### Configuration

1. Create a `.env` file in the root directory of the project with the following variables, replacing the placeholders with your actual values:

```
VUE_APP_VAPI_PUBLIC_KEY=your_vapi_public_key_here
VUE_APP_POST_URL=http://localhost:5000/create-assistant
VUE_APP_SERVERURL=your_server_url_here
VUE_APP_SERVER_SECRET=your_server_secret_here
```

2. Add your AI Assistant's prompt in the /src/assets/systemPrompt.js file.

### Running the Application

To serve the application with hot reloads, run:

```bash
npm run serve
```

The application will be available at `http://localhost:8080`.

### Building for Production

To build the application for production, run:

```bash
npm run build
```

## Interacting with the Vapi API

The frontend interacts with the Vapi API indirectly through our Flask backend. However, understanding the API's capabilities can be beneficial for extending the frontend functionality or debugging.

- To get acquainted with the features and possibilities offered by Vapi, visit the [Vapi Documentation](https://docs.vapi.ai/introduction).
- For a comprehensive look at the API endpoints and their specifications, refer to the [Vapi API Reference](https://docs.vapi.ai/api-reference/swagger).

### License

This project is licensed under the MIT License.
