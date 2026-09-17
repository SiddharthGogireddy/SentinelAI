# SentinelAI

> **Understand before you accept.**

SentinelAI is an AI-powered privacy policy and Terms & Conditions analyzer designed to help users understand what they are agreeing to before clicking **"Accept."**

Instead of manually reading lengthy legal documents, users can provide a privacy policy or Terms & Conditions document and analyze it for potentially sensitive permissions and privacy-related risks.

## Features

*  **Document Analysis** — Analyze privacy policies and Terms & Conditions from supported document sources.
*  **Permission Detection** — Detect permissions and sensitive data usage such as Camera, Microphone, Location, Contacts, Photos, Storage, and Clipboard.
*  **Risk Analysis** — Classify detected permissions and generate prioritized risk alerts.
*  **Risk Guidance** — Provide simplified explanations and guidance for detected privacy risks.
*  **Risk Summary** — Generate an overall summary of detected risks.
*  **AI Guidance** — Use an LLM-based layer to provide natural-language explanations of detected risks.

## How It Works

```text
Document / URL
      ↓
Text Extraction
      ↓
Clause Splitting
      ↓
Permission Detection
      ↓
Risk Assessment
      ↓
AI Guidance
      ↓
Risk Summary
      ↓
Frontend Dashboard
```

SentinelAI separates deterministic analysis from AI-generated guidance. Permission detection and risk classification are handled by the analysis pipeline, while the LLM is used to explain detected risks in a more understandable form.

## Tech Stack

### Frontend

* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python

### AI / NLP

* NLP-based text processing
* LLM-based guidance
* Sentence Transformers *(if currently used in the implementation)*

### Data

* CSV-based permission dataset
* PostgreSQL *(if currently connected to the application)*

### Tools

* Git
* GitHub
* Docker

## Project Status

 **In active development**

Core document analysis, permission detection, risk assessment, and AI-assisted guidance are implemented. Additional features such as RAG-based document chat, browser extension support, and deployment are planned.



## Current Pipeline

The current implementation supports the following analysis flow:

1. Extract text from supported input.
2. Split the document into individual clauses.
3. Detect sensitive permissions from each clause.
4. Assign risk levels to detected permissions.
5. Generate alerts for identified risks.
6. Provide AI-assisted guidance for understanding the detected risks.

## Project Structure

```text
SentinelAI/
│
├── backend/
│   ├── app.py
│   ├── api/
│   ├── extractors/
│   ├── services/
│   └── utils/
│
├── frontend/
│
├── ml/
├── docs/
├── architecture/
├── screenshots/
└── README.md
```

## Roadmap

* [x] Project initialization
* [x] Text extraction pipeline
* [x] Clause splitting
* [x] Permission detection
* [x] Risk scoring
* [x] Risk alert generation
* [x] AI-assisted guidance
* [ ] RAG chatbot
* [ ] Advanced frontend dashboard
* [ ] Browser extension
* [ ] PostgreSQL integration
* [ ] Deployment

## Example

Given a clause such as:

> "We may access your camera and microphone during video calls."

SentinelAI can identify:

```text
Camera       → High Risk
Microphone   → High Risk
```

The system can then provide an explanation of why those permissions matter and what the user should consider before accepting the policy.

## License

This project is currently under development.
