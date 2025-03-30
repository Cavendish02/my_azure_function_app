📁 Auto-Compress Blobs | Azure Functions
A serverless Python function that automatically compresses files in Azure Blob Storage

Azure Functions
Python
License: MIT

🔍 Overview
This Azure Function automatically detects and compresses files uploaded to Azure Blob Storage using Python's gzip. Designed for cost-efficient storage optimization, it processes files in real-time with zero infrastructure management.

✨ Features
Blob Trigger - Instantly processes new files in input container

Gzip Compression - Reduces file sizes by up to 90%

Serverless Architecture - Pay-per-execution pricing

Logging - Integrated with Azure Monitor and Application Insights

Scalable - Handles parallel file processing

🚀 Quick Start
bash
Copy
1. func azure functionapp publish <FUNCTION_APP_NAME>
2. Upload files to your 'input' container
3. Find compressed files in 'output' container
📂 Project Structure
Copy
├── __init__.py            # Main function logic
├── function.json          # Trigger/binding config
├── host.json              # Runtime settings
├── requirements.txt       # Python dependencies
└── README.md              # You're here!
💡 Use Cases
Log file optimization

Pre-processing for data pipelines

Automated backup compression

Serverless file transformation

🛠️ Tech Stack
Runtime: Azure Functions (Python 3.10)

Storage: Azure Blob Storage

Tooling: Azure CLI, VS Code

Monitoring: Azure Application Insights

📝 Bio for GitHub Profile
🔧 Auto-Compress Blobs
Open-source Azure Function that automates file compression in cloud storage. Perfect for developers needing serverless solutions for storage optimization. Features real-time processing, Python integration, and enterprise-grade scalability.

"Because storage costs add up – but your time shouldn't."

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fyour-repo%2Fmain%2Fdeploy.json)
[![Python CI](https://github.com/your-repo/auto-compress-blobs/actions/workflows/python-app.yml/badge.svg)](https://github.com/your-repo/auto-compress-blobs/actions)
