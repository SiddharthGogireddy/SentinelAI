# SentinelAI - Project Log

## Day 1 (June 29, 2026)

### Objective
Plan the project architecture and define the core workflow before implementation.

### Completed

- Initialized GitHub repository.
- Created project folder structure.
- Added initial README.
- Finalized project vision:
  - AI-powered privacy policy analyzer.
  - Alert-first workflow.
- Decided supported input methods:
  - PDF
  - Website URL
  - Copy-pasted Terms & Conditions
  - Browser extension (future)
- Designed modular AI architecture.
- Decided alerts are generated per clause rather than per permission.
- Decided the system scans the complete document before displaying alerts.

### Key Design Decisions

1. Universal input pipeline.
2. Alert-first user experience.
3. One alert can contain multiple related permissions.
4. AI explains why each alert matters.
5. AI analysis is independent of the input source.

### Next Milestone

Build the document ingestion pipeline and begin dataset creation.

### Status

Day 1 Completed
# SentinelAI - Project Log

## Day 2 (July 1, 2026)

### Objective

Establish the data preprocessing pipeline and prepare the project for machine learning development.

### Completed

* Renamed the `ml` directory to `ai` to better represent the project's scope.
* Finalized the master dataset concept.
* Created the dataset directory structure:

  * `raw/`
  * `processed/`
  * `labeled/`
* Created the initial `clauses.csv` file.
* Designed the first version of the dataset schema.
* Implemented the text extraction module (`text_extractor.py`).
* Implemented the clause splitting module (`clause_splitter.py`).
* Connected preprocessing modules using `pipeline.py`.
* Finalized the recommendation system:

  * No Major Concerns
  * Review Carefully
  * Significant Privacy Concerns
* Decided to provide evidence-based guidance instead of a numerical privacy score.
* Expanded the project vision to include a future browser extension capable of monitoring live browser permission requests.

### Key Design Decisions

1. One dataset row represents one clause.

2. One clause may contain multiple permissions.

3. Alerts are generated per clause rather than per permission.

4. The AI analyzes the entire document before presenting results.

5. The preprocessing pipeline follows:

   Input
   → Text Extraction
   → Clause Splitting
   → Permission Detection
   → Guidance Generation

6. Browser extension support will be developed after the core AI pipeline is complete.

### Files Created

* `backend/text_extractor.py`
* `backend/clause_splitter.py`
* `backend/pipeline.py`
* `ai/datasets/labeled/clauses.csv`

### Current Status

Completed:

* Project planning
* Dataset design
* Text preprocessing pipeline

Next:

* Begin semantic permission detection using Sentence Transformers.

### Status

Day 2 Completed
# Day 3 — Data Preprocessing Pipeline

**Date:** 2026-07-02

## Completed

- Finalized backend folder structure.
- Added dedicated loaders for different input sources.
- Implemented text loading for `.txt` privacy policy documents.
- Built the first preprocessing pipeline.
- Implemented an initial clause splitter.
- Improved clause splitting by filtering common section headings.
- Created the raw → processed → labeled dataset workflow.
- Added sample datasets for Discord:
  - Privacy Policy
  - Cookie Policy
  - Terms of Service
- Fixed CSV formatting issues for the labeled dataset.
- Established the initial permission taxonomy for annotation.

## Challenges

- Sentence splitting produced incorrect clauses for legal documents.
- Section headings were incorrectly treated as clauses.
- CSV parsing failed due to improperly formatted multi-label entries.
- Sentence-transformer baseline produced relatively low similarity scores (~0.41), indicating that semantic similarity alone is insufficient for permission detection.

## Decisions

- Preserve raw documents separately from processed data.
- Use `.txt` files as the intermediate format during development.
- Delay model training until a sufficiently large, real-world labeled dataset is available.
- Build the dataset from real privacy policies instead of synthetic examples.

## Next Steps

- Improve clause splitting for legal documents.
- Expand the dataset using additional companies.
- Build the annotation workflow.
- Begin training the first multi-label classifier after collecting sufficient labeled data.
# Day 5 — Annotation Assistant & Risk Engine

**Date:** 2026-07-03

## Completed

- Improved the annotation workflow.
- Added label validation.
- Designed the rule-based label suggestion system.
- Implemented the initial Risk Engine architecture.
- Created a centralized risk database for permissions.
- Standardized module interfaces for future integration.
- Decided to postpone ML training until a larger labeled dataset is available.

## Challenges

- Manual annotation remains time-consuming.
- Current dataset is too small for effective supervised learning.
- Clause splitting still needs refinement for some legal documents.

## Decisions

- Use rule-based suggestions before ML predictions.
- Keep the Risk Engine independent of the permission detector.
- Build a complete rule-based MVP before introducing machine learning.

## Next Steps

- Integrate all modules into a single analyzer.
- Build the browser extension workflow.
- Expand the labeled dataset using multiple companies.
# Day 6 — Backend API & End-to-End Integration

**Date:** 2026-07-03

## Completed

- Created the FastAPI backend application.
- Added the `/api/analyze` endpoint.
- Connected the analyzer with the backend API.
- Integrated the clause splitter, permission detector, and risk engine.
- Successfully tested the complete analysis pipeline using FastAPI Swagger UI.
- Created the initial `requirements.txt`.
- Fixed import issues across backend modules.
- Configured CORS for frontend integration.

## Challenges

- Resolved multiple package import issues after restructuring the project.
- Fixed broken `uvicorn` launcher caused by an outdated Python installation.
- Standardized backend package imports.

## Decisions

- Keep the backend modular with clearly separated API, services, preprocessing, and risk components.
- Use FastAPI as the backend framework.
- Keep the rule-based permission detector until a sufficiently large labeled dataset is available.

## Next Steps

- Build the React frontend.
- Connect the frontend to the `/api/analyze` endpoint.
- Display analysis results using reusable UI components.
- Improve clause splitting for multi-sentence pasted text.
# Day 7 — Frontend Foundation & Dashboard Setup

Date: 2026-07-04

## Completed

- Created the React frontend using Vite.
- Integrated Tailwind CSS into the frontend project.
- Built the initial dashboard layout.
- Created reusable UI components:
  - Navbar
  - Hero
  - InputCard
  - SummaryCards
  - RiskList
- Implemented the initial glassmorphism design system.
- Added the emerald security/privacy color theme.
- Connected the frontend project structure with the backend API architecture.

## Challenges

- Resolved Tailwind CSS configuration issues with Vite.
- Fixed missing dependency issues including Axios and Lucide React.
- Solved import path problems after restructuring component folders.
- Adjusted frontend styling after the initial blocky design looked too generic.

## Decisions

- Use a glassmorphism-based UI instead of a traditional card layout.
- Keep the dashboard component-driven for easier feature additions.
- Use Tailwind utility classes instead of custom CSS files where possible.
- Maintain a consistent privacy/security visual theme throughout the application.

## Next Steps

- Connect the frontend to the backend API.
- Replace hardcoded data with live API responses.
- Add loading states during analysis.
- Implement dynamic risk summaries and result cards.

# Day 8 — Frontend Backend Integration

Date: 2026-07-05

## Completed

- Connected the React frontend with the FastAPI backend.
- Integrated Axios for API communication.
- Connected the Analyze button to the `/api/analyze` endpoint.
- Implemented dynamic risk summaries.
- Implemented dynamic risk cards.
- Replaced hardcoded frontend data with backend responses.
- Added loading states during analysis.
- Successfully completed the first end-to-end analysis workflow.

## Challenges

- Fixed multiple React prop passing issues.
- Resolved state update bugs preventing UI refreshes.
- Fixed hardcoded summary values causing incorrect outputs.
- Corrected API response handling after backend response structure changes.

## Decisions

- Keep backend responses standardized using:
  ```json
  {
      "success": true,
      "data": {}
  }



# Day 9 — PDF Upload & Document Analysis

Date: 2026-07-06

## Completed

- Added PDF upload support to the backend.
- Created the `/api/upload` endpoint.
- Integrated `python-multipart` for file uploads.
- Implemented PDF text extraction using `pypdf`.
- Connected PDF uploads to the existing analysis pipeline.
- Added frontend PDF upload support.
- Successfully analyzed uploaded privacy policy PDFs.

## Challenges

- Resolved FastAPI multipart dependency errors.
- Fixed module import issues after introducing upload routes.
- Refactored the PDF loader to work with FastAPI `UploadFile`.
- Corrected frontend upload callback issues caused by prop naming mismatches.

## Decisions

- Reuse the existing analysis pipeline for PDFs instead of creating a separate workflow.
- Keep uploaded files in memory using `BytesIO`.
- Continue using rule-based permission detection for consistency across input types.

## Next Steps

- Add source evidence for every detected risk.
- Attach triggering clauses to each alert.
- Improve frontend presentation of analysis results.
- Begin implementing multiple analysis modes.


# Day 10 — Evidence Tracking & Multi-Mode Interface

Date: 2026-07-07

## Completed

- Added evidence tracking to the risk engine.
- Attached triggering clauses to generated alerts.
- Displayed evidence directly in frontend risk cards.
- Added multiple analysis modes:
  - Paste Text
  - Upload PDF
  - Analyze URL
- Implemented interactive mode switching in the frontend.
- Improved dashboard responsiveness and usability.
- Continued refining the glassmorphism interface.

## Challenges

- Fixed React hook placement issues.
- Resolved state synchronization problems between input modes.
- Corrected frontend callback and prop casing issues.
- Refactored the alert generation pipeline to support evidence tracking.

## Decisions

- Store evidence directly inside alert objects.
- Maintain a single analysis pipeline for all input types.
- Prepare the architecture for future page-number tracking and PDF highlighting.

## Next Steps

- Integrate local LLM explanations using Ollama.
- Add page number support for PDF analysis.
- Implement PDF highlighting using PyMuPDF.
- Build URL-based privacy policy analysis.

# Day 11 — Ollama Integration & AI Explanations

Date: 2026-07-12

## Completed

- Decided to adopt a hybrid architecture combining rule-based detection with LLM explanations.
- Selected Ollama instead of cloud APIs to keep the system fully local and privacy preserving.
- Chose local LLM inference to avoid API costs and external data transmission.
- Finalized the architecture for integrating AI explanations into the existing risk pipeline.
- Designed the `llm_explainer.py` service layer.
- Planned integration between the rule engine and local LLM responses.

## Challenges

- Evaluated the tradeoff between deterministic rule-based detection and probabilistic LLM outputs.
- Considered latency implications of local inference.
- Designed a strategy to avoid sending every clause to the LLM unnecessarily.

## Decisions

- Keep rule-based permission detection as the primary detection mechanism.
- Use Ollama only for explanation generation and contextual reasoning.
- Send only clauses containing detected permissions to the LLM.
- Keep the existing risk engine unchanged for consistent risk scoring.
- Use a local model to preserve user privacy.

## Selected Architecture

PDF / Text / URL
    ↓
Clause Splitter
    ↓
Permission Detection
    ↓
Risk Engine
    ↓
Ollama Explanation Layer
    ↓
Frontend Dashboard

## Planned Models

Primary:
- llama3:8b

Fallback:
- gemma3:4b
- mistral:7b

## Planned Backend Changes

New file:
backend/services/llm_explainer.py

Responsibilities:
- Generate human-readable explanations.
- Explain why permissions were flagged.
- Provide contextual recommendations.
- Distinguish between normal and potentially concerning permissions.

Example Output:

{
    "explanation":
        "Camera access is commonly required for video calling features but should only be granted when necessary.",

    "recommendation":
        "Verify that camera access is restricted to active video sessions."
}

## Next Steps

- Install Ollama locally.
- Pull the selected model.
- Implement `llm_explainer.py`.
- Integrate explanations into `analyzer.py`.
- Display AI explanations in `RiskList.jsx`.

# Day 12 — Hybrid AI Integration with Ollama

Date: 2026-07-12

## Completed

- Installed and configured Ollama locally.
- Successfully connected SentinelAI with a local LLM.
- Built the initial `llm_explainer.py` service.
- Integrated AI explanations into the analysis pipeline.
- Generated explanations for detected permissions such as camera and cookies.
- Verified end-to-end communication between FastAPI and Ollama.
- Implemented local inference without requiring external APIs.
- Successfully tested AI explanations on sample privacy policy clauses.

## Challenges

- Encountered Ollama server conflicts due to an already running instance on port `11434`.
- Fixed backend import issues while integrating the explainer service.
- Adjusted response parsing from Ollama API responses.
- Identified latency issues caused by generating explanations for every detected risk.

## Decisions

- Use local LLM inference instead of cloud APIs to preserve privacy.
- Keep Ollama as the primary inference engine for Version 2.
- Separate deterministic risk detection from generative explanations.

## Architecture Introduced

Rule Engine
    ↓
Detected Risks
    ↓
Ollama Local LLM
    ↓
Human-readable Explanation

## Next Steps

- Improve explanation quality.
- Reduce analysis latency.
- Explore on-demand explanations instead of automatic generation.

# Day 13 — PDF Processing & On-Demand AI Explanations

Date: 2026-07-12

## Completed

- Implemented PDF upload functionality in the React frontend.
- Added backend support for multipart file uploads using FastAPI.
- Integrated PDF text extraction using PyPDF.
- Built a PDF analysis pipeline using extracted clauses.
- Added support for tracking clause page numbers during extraction.
- Connected PDF upload results with the existing risk analysis engine.
- Successfully integrated Ollama for local AI-powered explanations.
- Refactored AI explanations from automatic generation to an on-demand model.
- Added an "Explain with AI" button for each detected risk.
- Connected the frontend explain button to the backend explanation endpoint.
- Implemented frontend caching to avoid regenerating explanations for the same risk.
- Improved application responsiveness by separating deterministic analysis from LLM inference.

## Challenges

- Resolved issues with virtual environment activation and package installation.
- Fixed import errors caused by project restructuring.
- Corrected duplicate function definitions in `pdf_loader.py`.
- Fixed premature `return` statements that caused incomplete PDF processing.
- Resolved React component crashes caused by undefined variables such as `Icon`, `index`, and stale references.
- Fixed mismatches between frontend expectations and backend response formats.
- Corrected page metadata handling during PDF analysis.
- Resolved FastAPI upload errors caused by unsupported arguments passed to the risk engine.

## Decisions

- Keep rule-based permission detection as the primary analysis mechanism.
- Use Ollama only when users explicitly request additional context.
- Prioritize responsiveness and instant results over automatic AI generation.
- Keep all LLM inference local to preserve privacy and eliminate API costs.
- Store page numbers separately from risk generation logic to maintain modularity.

## Final Architecture

Text Input / PDF Upload
        ↓
Clause Splitter
        ↓
Permission Detector
        ↓
Risk Engine
        ↓
Frontend Risk Cards
        ↓
Optional "Explain with AI"
        ↓
Ollama Local LLM

## Current Features

- Text policy analysis
- PDF policy analysis
- Risk categorization (High, Medium, Low)
- Evidence extraction
- On-demand AI explanations
- Local LLM inference
- Dynamic summary cards
- Multi-input frontend interface

## Next Steps

- Implement URL analysis support.
- Display page numbers directly in risk cards.
- Add PDF highlighting for detected clauses.
- Structure AI explanations into:
  - Why flagged
  - Commonness
  - User impact
  - Recommendation
- Begin browser extension integration.

## Progress Update

SentinelAI has evolved from a rule-based privacy policy analyzer into a hybrid AI application combining deterministic risk detection with local LLM reasoning while maintaining fast response times and user privacy.# # 
# Day 14 — Advanced URL Extraction

Date: 2026-07-13

## Completed

- Added URL analysis capability to SentinelAI.
- Implemented frontend URL input flow.
- Added backend URL extraction endpoint.
- Integrated URL analysis into the existing analyzer pipeline.
- Tested real-world privacy policies using Discord Privacy Policy.
- Identified false positives caused by webpage navigation content.
- Evaluated production-grade extraction approaches.

## Challenges

- Entire webpages were being treated as a single clause.
- Navigation menus generated numerous false positives.
- Traditional BeautifulSoup extraction was insufficient for privacy policies.

## Decisions

- Adopt Trafilatura for webpage extraction.
- Keep the clause-based risk engine unchanged.
- Continue using local LLM explanations through Ollama.

## Next Steps

- Add clause source references.
- Improve clause splitting.
- Introduce retrieval-based context selection for LLM explanations.
- Begin work on browser extension integration.