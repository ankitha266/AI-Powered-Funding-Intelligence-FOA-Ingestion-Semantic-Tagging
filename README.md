# AI-Powered-Funding-Intelligence-FOA-Ingestion-Semantic-Tagging
Contributor: Ankitha Ammu

Project: GSoC 2026 Screening Task – ISSR (University of Alabama)

Overview
This repository contains a modular ETL (Extract, Transform, Load) Pipeline designed to automate the discovery and categorization of Funding Opportunity Announcements (FOAs). By shifting from traditional keyword searches to Semantic Vector Space analysis, this tool identifies research funding based on conceptual relevance rather than exact terminology.

Key Technical Features
Resilient Ingestion: Uses BeautifulSoup4 and PyMuPDF with custom headers and request throttling to handle federal domains like NSF, NIH, and Grants.gov.

Data Normalization: Implements Pydantic for strict schema validation, ensuring all ingested data is stored in a clean, ISO-8601 compliant JSON/CSV format.

Semantic Tagging: Leverages the all-MiniLM-L6-v2 transformer model to generate 384-dimensional vector embeddings.

Human-in-the-Loop (HITL): Implements a 0.75 Hard Threshold for Cosine Similarity. Any tag with lower confidence is flagged as "Pending Review" to ensure Scientific Verification.

System Architecture
The system follows a decoupled four-stage architecture:

Extraction: Specialized parsers for HTML and PDF sources.

Transformation: Data sanitization via Regex and schema enforcement.

Enrichment: Semantic alignment using vector similarity.

Loading: Export to JSON, CSV, and ChromaDB vector index.

Setup & Execution
1. Install Dependencies
Bash
pip install -r requirements.txt
2. Run the Multi-Source Demo
To verify the system's ability to normalize data from NSF, NIH, and Grants.gov simultaneously:

Bash
python main.py --demo --out_dir ./out
3. Process a Single URL
Bash
python main.py --url "YOUR_URL_HERE" --out_dir ./out
Technical Stack
Language: Python 3.10+

NLP: sentence-transformers, PyTorch

Parsing: BeautifulSoup4, PyMuPDF

Data: Pandas, Pydantic
