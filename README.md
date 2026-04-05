# 🌍 Multilingual Chatbot with AWS Bedrock

A **Streamlit-based multilingual chatbot** powered by **Amazon Nova Lite** via AWS Bedrock and LangChain. This app allows users to interact with an AI assistant in multiple languages through a simple and clean web interface.

---

## 🚀 Features

- 💬 **Multilingual Support** — Chat in English, Spanish, French, German, Chinese, and Hindi
- 🤖 **Amazon Nova Lite** — Uses AWS Bedrock's `amazon.nova-lite-v1:0` model
- ⚡ **LangChain Integration** — Prompt chaining via `ChatPromptTemplate` and `ChatBedrock`
- 🖥️ **Streamlit UI** — Clean and interactive web interface
- 🔐 **Secure Credentials** — AWS credentials managed via `.env` file

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [LangChain](https://www.langchain.com/) | LLM chaining & prompt management |
| [AWS Bedrock](https://aws.amazon.com/bedrock/) | Managed AI model hosting |
| [Amazon Nova Lite](https://aws.amazon.com/ai/nova/) | Underlying language model |
| [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) | AWS SDK for Python |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📁 Project Structure

```
├── app.py               # Main Streamlit application
├── .env                 # AWS credentials (not committed to git)
├── .env.example         # Example environment variables file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Prerequisites

- Python **3.9+**
- An **AWS Account** with Bedrock access enabled
- AWS IAM user with **`AmazonBedrockFullAccess`** (or equivalent) policy
- Access granted to the **Amazon Nova Lite** model in AWS Bedrock console

---

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multilingual-chatbot-bedrock.git
cd multilingual-chatbot-bedrock
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit the `.env` file with your AWS credentials:

```env
aws_access_key_id=YOUR_AWS_ACCESS_KEY_ID
aws_secret_access_key=YOUR_AWS_SECRET_ACCESS_KEY
aws_region_name=us-east-1
```

> ⚠️ **Never commit your `.env` file to version control.** Make sure `.env` is listed in your `.gitignore`.

### 5. Enable Amazon Nova Lite on AWS Bedrock

1. Log in to the [AWS Console](https://console.aws.amazon.com/)
2. Navigate to **AWS Bedrock → Model access**
3. Request access to **Amazon Nova Lite** (`amazon.nova-lite-v1:0`)
4. Wait for access to be granted (usually instant)

---

## ▶️ Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📦 Requirements

Create a `requirements.txt` with the following:

```txt
streamlit
langchain
langchain-aws
langchain-core
boto3
python-dotenv
```

Install all at once:

```bash
pip install streamlit langchain langchain-aws langchain-core boto3 python-dotenv
```

---

## 🖼️ How to Use

1. **Select a Language** from the sidebar dropdown menu
2. **Type your message** in the text area (max 200 characters)
3. The chatbot will **respond in your selected language** using Amazon Nova Lite
4. View the **AI-generated response** displayed on the main screen

---

## 🌐 Supported Languages

| Language | Code |
|---|---|
| 🇬🇧 English | `en` |
| 🇪🇸 Spanish | `es` |
| 🇫🇷 French | `fr` |
| 🇩🇪 German | `de` |
| 🇨🇳 Chinese | `zh` |
| 🇮🇳 Hindi | `hi` |

---

## 🔒 Security Best Practices

- Store credentials in `.env` — never hardcode them
- Add `.env` to `.gitignore`
- Use **IAM roles** instead of access keys when deploying to AWS infrastructure
- Apply the **principle of least privilege** for your IAM user

```gitignore
# .gitignore
.env
__pycache__/
*.pyc
venv/
```

---

## 🛠️ Configuration

You can adjust the model behavior by modifying `model_kwargs` in `app.py`:

```python
model_kwargs={
    "temperature": 0.7,   # 0.0 (deterministic) → 1.0 (creative)
    "max_tokens": 512     # Maximum response length
}
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| `NoCredentialsError` | Check your `.env` file has correct AWS credentials |
| `AccessDeniedException` | Enable Nova Lite model access in AWS Bedrock console |
| `ResourceNotFoundException` | Verify the `region_name` supports Bedrock (e.g., `us-east-1`) |
| Blank response | Check your IAM user has `AmazonBedrockFullAccess` policy |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- LinkedIn: [Harshit](https://www.linkedin.com/in/iamharshitagarwal/)

---

> Built with ❤️ using AWS Bedrock, LangChain, and Streamlit
