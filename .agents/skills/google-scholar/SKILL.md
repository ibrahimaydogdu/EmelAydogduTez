---
name: google-scholar
description: >-
  Google Scholar search and academic literature retrieval. Use this skill when the user
  wants to find academic papers, articles, citations, authors, abstracts, or BibTeX references
  via Google Scholar.
---

# Google Scholar Skill

This skill provides integration with Google Scholar via the `google_scholar` MCP tool and the `google-scholar` CLI.

## MCP Tool

- **`search_google_scholar`**:
  - `query` (string, required): Search query string (paper title, topic, or keywords)
  - `author` (string, optional): Author name to filter results
  - `year_low` (integer, optional): Start year for filtering (e.g. 2020)
  - `year_high` (integer, optional): End year for filtering (e.g. 2024)
  - `num_results` (integer, default: 5): Number of results to return

### Returns
- `bib`: Title, author, year, venue, publisher, pages, booktitle, etc.
- `abstract`: Paper abstract / summary
- `pub_url`: Publication link
- `num_citations`: Number of citations
- `citedby_url`: Link to citing papers
- `eprint_url`: PDF / preprint URL if available

## CLI Commands

```bash
# Basic paper search
google-scholar search "deep learning" --num-results 5

# Search with author filter
google-scholar search "convolutional neural networks" --author "Yann LeCun"

# Search with publication year range
google-scholar search "transformer" --year-low 2020 --year-high 2024

# Get BibTeX citation
google-scholar bibtex "attention is all you need"
```
