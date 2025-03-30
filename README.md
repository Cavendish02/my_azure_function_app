# Azure Blob Auto-Compressor 🚀

![Azure Functions](https://img.shields.io/badge/Azure_Functions-0062AD?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

A serverless Azure Function that automatically compresses files in Blob Storage using Python's gzip compression.

## 🌟 Features

- ⚡ Real-time file processing with Blob Storage triggers
- 📦 Gzip compression for optimal file size reduction
- 🔍 Detailed logging with Azure Application Insights
- 🔄 Automatic retry on failures
- 🔒 Secure Azure AD integration

## 📦 Prerequisites

- Azure subscription
- Python 3.10+
- Azure Functions Core Tools v4.x
- Azure CLI

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/azure-blob-autocompressor.git

# Navigate to project directory
cd azure-blob-autocompressor

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.\.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
