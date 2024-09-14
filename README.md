

```markdown
# Langchain Chatbot with FastAPI and Streamlit

This project showcases a chatbot that generates essays and poems based on user input. It utilizes FastAPI for the backend, which integrates with the Ollama and OpenAI models, and Streamlit for the frontend user interface.

## Project Structure

- `app.py`: FastAPI backend application.
- `client.py`: Streamlit frontend application.
- `.env`: Contains environment variables such as API keys.
- `requirements.txt`: Python package dependencies.

## Features

- **Essay Generation**: Uses OpenAI's model to generate essays on given topics.
- **Poem Generation**: Uses Ollama's model (Llama2) to generate poems suitable for children on given topics.
- **User Interface**: Streamlit-based UI for interacting with the chatbot and displaying results.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-chatbot.git
cd langchain-chatbot
```

### 2. Set Up Environment

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project with the following content:

```
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

## Running the Project

### 1. Start the FastAPI Backend

```bash
uvicorn app:app --reload
```

This will start the FastAPI server at `http://127.0.0.1:8000`.

### 2. Start the Streamlit Frontend

Open a new terminal or command prompt and run:

```bash
streamlit run client.py
```

This will open the Streamlit interface in your default web browser.

## Endpoints

- **Essay Generation**: `POST /essay`
  - Request body: `{ "topic": "your_topic" }`
  - Response: Generated essay based on the topic.

- **Poem Generation**: `POST /poem`
  - Request body: `{ "topic": "your_topic" }`
  - Response: Generated poem based on the topic.

## Troubleshooting

- **Service Errors**: Ensure the FastAPI server is running and accessible.
- **API Key Issues**: Verify that the API keys in the `.env` file are correct.
- **Dependencies**: Ensure all required packages are installed by checking `requirements.txt`.

## Deployment

For deploying the FastAPI backend, you can use services like [Railway](https://railway.app/) for hosting. 

Refer to Railway's documentation for specific steps on deployment.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, you can reach out to:

- **Email**: libberajkeerthy001@gmail.com

---



### Notes

1. **Replace Placeholder Information**: Be sure to replace placeholders like `your_openai_api_key`, `yourusername`, and `your-email@example.com` with your actual details.
2. **Adjust Instructions**: Depending on the exact setup or additional configurations you have, you might need to adjust the instructions accordingly.
3. **Add License File**: If you include a license file in your repository, make sure to mention it correctly in the `README.md`.
