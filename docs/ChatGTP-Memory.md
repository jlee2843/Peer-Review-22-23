# 🧠 Project Memory Summary

## 📌 Project Focus

You’re building a comprehensive pipeline to analyze the **impact of peer review on academic publishing**, especially
comparing **preprints vs. published versions**. This project includes:

- **Textual comparison**: semantic similarity, thematic shifts, structural changes
- **Metadata tracking**: citations, figures, references, author details, ORCID verification
- **Metric tracking**:
    - Statistical rigor (e.g., confidence intervals, statistical power)
    - Authorship changes and career stage
    - Reviewer sentiment and tone
    - References added/removed
    - Sentiment shift
    - Citation and Altmetric impact
    - Label shift (classification drift)
    - Review quality and timing
    - Longitudinal version tracking
    - Peer-Review Effect Score (PRES)

## 🛠️ Pipeline & Tools

- **Parsing PDFs**: OpenParse (preferred), spaCy, OCR fallback
- **Similarity Analysis**: Sentence-BERT (semantic), difflib, fuzzywuzzy/rapidfuzz (for names, text diffs)
- **Metadata APIs**: CrossRef, Semantic Scholar, BioRxiv, arXiv, EuropePMC, Unpaywall, ORCID
- **Visualization & Dashboarding**: Streamlit
- **Clustering & Topic Modeling**: BERTopic
- **Classification & ML**: Label classifiers, XGBoost, time-series drift
- **Statistical Analysis**: IVs, DiD, multivariate, meta-analysis, geospatial
- **Monitoring**: Prometheus + Grafana
- **ETL Orchestration**: Apache Airflow
- **CI/CD & Testing**: Pytest, GitHub Actions, test coverage reports

## 📦 Automation Features

- Generates:
    - PRES score and report (PDF + CSV)
    - Confusion matrices and Sankey diagrams
    - Full version ZIP archive with logs, reports, metrics
- Upload options:
    - Google Drive (by folder ID)
    - Dropbox (auto-journal-folder naming)
    - Email delivery with `.env` for credentials
    - Telegram notifications

## 🎯 Current Priorities

- Pipeline recoding and restructuring (object-oriented, modular)
- Rebuild test suite in `pytest` with coverage
- Add full project documentation
- Finalize download + packaging logic for all outputs
- Identify and optimize CPU- vs. I/O-bound tasks (considering Spark, threading, asyncio)
