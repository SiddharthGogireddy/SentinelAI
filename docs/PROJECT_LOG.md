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