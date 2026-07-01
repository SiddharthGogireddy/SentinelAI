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
