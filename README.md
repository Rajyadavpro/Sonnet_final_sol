# Sonnet AI-Powered Ticket & SOP Solution System

## Overview

This system uses Google Gemini 2.5 Pro to process support tickets, extract issues, match the best SOP, and generate tailored solutions. It outputs structured JSON for each ticket, making integration and analysis easy.

## Key Features

- **AI-Powered Ticket Analysis:** Uses Gemini 2.5 Pro (temperature=0) for deterministic, structured extraction
- **Intelligent SOP Matching:** Finds the most relevant SOP from a large knowledge base
- **JSON Output:** Each ticket's result includes the issue, SOP title, SOP content, and step-by-step modification instructions
- **Parallel Processing:** Handles multiple tickets at once for fast results
- **Progress Reporting:** Clear messages for each step and ticket
- **Secure Configuration:** API keys and sensitive data protected by .gitignore

## Workflow & Architecture

1. **Ticket files** are placed in `data/ticket/ticket_data/` (plain text)
2. **SOP knowledge base** is in `data/consolidated/consolidated_documents.txt`
3. Run `python test.py` to process all tickets in parallel
4. For each ticket, Gemini:
   - Extracts the issue
   - Finds the best SOP title
   - Returns SOP content
   - Lists all SOP steps, noting which need modification
5. Results are saved as `outputs/ticket_dataX/result.json` for each ticket

## Project Structure

```
├── config/
│   ├── .env                # API key (gitignored)
│   └── .env.example        # Template
├── data/
│   ├── consolidated/      # SOP knowledge base
│   ├── source_documents/  # Individual SOP files
│   ├── ticket/
│   │   ├── ticket_data/   # Raw ticket files
│   │   └── ticket_info_json/ # (optional) processed info
├── outputs/
│   └── ticket_dataX/      # JSON output per ticket
├── src/                   # Source code
│   ├── ticket_info.py
│   ├── sop_matcher.py
│   ├── sop_loader.py
│   └── solution_generator.py
├── test.py                # Main Gemini workflow
├── run_workflow.bat       # Windows script
├── requirements.txt       # Python dependencies
├── .gitignore             # Security
└── README.md
```

## Usage

1. Add your Gemini API key to `config/.env` as `GEMINI_API_KEY=your_key_here`
2. Place ticket files in `data/ticket/ticket_data/` and SOP file in `data/consolidated/consolidated_documents.txt`
3. Run:
   ```bash
   python test.py
   ```
4. Find results in `outputs/ticket_dataX/result.json` for each ticket, with fields:
   - `issue`: Issue mentioned in the ticket
   - `sop_title`: Title of the matched SOP
   - `sop_content`: Content of the SOP
   - `sop_steps_modification`: Step-by-step modification instructions

## Example Output

```json
{
  "ticket_file": "ticket_data1.txt",
  "issue": "Remove LCS disputes from Sonnet",
  "sop_title": "FILE 36: Removing LCS Disputes.txt",
  "sop_content": "Step 1: ... Step 2: ...",
  "sop_steps_modification": "Step 1: No change. Step 2: Modify for Jovia. ..."
}
```

## Security

- `.env` and sensitive files are gitignored
- Never commit API keys or customer data

## Requirements

- Python 3.8+
- `google-generativeai`, `python-dotenv`

## Contributing

See the contributing section in this README for standards and setup.
