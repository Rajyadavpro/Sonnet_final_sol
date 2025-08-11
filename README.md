# AI-Powered Support Ticket Processing System

## Overview

This production-ready system uses Google Gemini AI to automatically process support tickets and generate tailored solutions. It extracts structured information from raw tickets, identifies the issue, matches the best Standard Operating Procedure (SOP), and outputs results in JSON format for easy integration and analysis.

## 🚀 Key Features

- **🤖 AI-Powered Ticket Analysis**: Uses Gemini 2.5 Pro (temperature=0) for deterministic, structured information extraction
- **🧠 Intelligent SOP Matching**: Automatically finds the most relevant SOP from 107+ procedural documents using semantic analysis
- **🔄 Dynamic Content Processing**: Outputs results in JSON format, including ticket issue, SOP title, SOP content, and step modifications
- **👥 Personalized Response Generation**: Creates tailored solutions addressing specific ticket issues and SOP steps
- **🛡️ Comprehensive Fallback System**: Gracefully handles missing data, API failures, and edge cases
- **📁 Clean Architecture**: Professional project structure with organized source code, data separation, and output management
- **⚡ Convenience Scripts**: One-click workflow execution with error handling, progress reporting, and clear output messages
- **🔐 Secure Configuration**: API keys and sensitive data properly protected with .gitignore

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Raw Ticket    │───▶│  ticket_info.py  │───▶│ Structured JSON │───▶│ Gemini Analysis │
│  (ticket_data)  │    │ (AI Extraction)  │    │  (ticket_info)  │    │   (Matching)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘    └─────────────────┘
                                │                                                │
                                ▼                                                ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Final Solution  │◀───│solution_generator│◀───│  sop_loader.py  │◀───│  sop_matcher.py │
│  (Personalized) │    │     .py (AI)     │    │ (Content Load)  │    │  (AI Analysis)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📂 Project Structure

```
├── 📁 config/
│   ├── .env                          # 🔐 API keys and configuration (gitignored)
│   └── .env.example                  # 📋 Environment template
├── 📁 outputs/
│   └── ticket_dataX/
│       └── result.json               # 📝 AI-generated structured output for each ticket
## Usage

1. Place your Gemini API key in `config/.env` as `GEMINI_API_KEY=your_key_here`.
2. Add ticket files to `data/ticket/ticket_data/` and SOP file to `data/consolidated/consolidated_documents.txt`.
3. Run `python test.py` to process all tickets in parallel.
4. Find results in `outputs/ticket_dataX/result.json` for each ticket, containing:
   - Issue mentioned in the ticket
   - Title of the SOP
   - Content of the SOP
   - Step-by-step modification instructions
├── 📁 data/
│   ├── 📁 consolidated/
│   │   └── consolidated_documents.txt # 📚 Knowledge base (107 SOP files)
│   ├── 📁 source_documents/          # 📄 Individual SOP files
│   ├── 📁 ticket/
│   │   ├── 📁 ticket_data/           # 📥 Raw ticket files (.gitkeep preserved)
│   │   │   ├── .gitkeep
│   │   │   └── ticket_data.txt       # 🎫 Input tickets (gitignored)
│   │   └── 📁 ticket_info_json/      # 🔄 Processed JSON files (.gitkeep preserved)
│   │       ├── .gitkeep
│   │       └── ticket_info.json      # 📊 Structured data (gitignored)
│   └── 📁 SOP_content/               # 📖 Extracted SOP content (.gitkeep preserved)
│       ├── .gitkeep
│       └── content.txt               # 📝 SOP procedures (gitignored)
├── 📁 outputs/
│   ├── 📁 sop/                       # 🎯 File matching results (.gitkeep preserved)
│   │   ├── .gitkeep
│   │   └── ticket_data.txt           # 🔍 Best match (gitignored)
│   └── 📁 final_solution/            # ✅ Generated solutions (.gitkeep preserved)
│       ├── .gitkeep
│       └── ticket_data.txt           # 💡 Tailored solutions (gitignored)
├── 📁 src/                           # 💻 Source code directory
│   ├── ticket_info.py                # 🎫 Ticket information extractor
│   ├── sop_matcher.py                # 🔍 SOP file matcher (renamed from simple_gemini_matcher.py)
│   ├── sop_loader.py                 # 📖 SOP content loader
│   └── solution_generator.py         # ✨ Solution generator (renamed from final.py)
├── 🚀 run_workflow.bat               # 🪟 Windows convenience script
├── 🚀 run_workflow.sh                # 🐧 Unix/Linux/Mac convenience script
├── 📋 requirements.txt               # 📦 Python dependencies
├── 🚫 .gitignore                     # 🔒 Comprehensive ignore rules
└── 📖 README.md                      # 📚 This documentation
```
```

## 🔐 Security & Git Configuration

### Protected Files & Directories
The `.gitignore` is configured to protect sensitive data and temporary files:

**🚫 Never Committed:**
- `config/.env` - API keys and sensitive configuration
- `outputs/**/*.txt` - Generated solutions and matches
- `data/ticket/**/*.txt` - Raw and processed ticket data
- `data/SOP_content/*.txt` - Extracted SOP content
- AI cache, logs, and temporary files

**✅ Always Committed:**
- Source code in `src/`
- Knowledge base in `data/consolidated/` and `data/source_documents/`
- Project configuration files
- `.gitkeep` files to preserve directory structure

### Environment Setup
1. Copy `config/.env.example` to `config/.env`
2. Add your Google AI API key to the `.env` file
3. The `.env` file is automatically gitignored for security

## 📋 Prerequisites

- **Python 3.7+**
- **Google AI API key** (Gemini) - [Get one here](https://makersuite.google.com/app/apikey)
- **Dependencies**: `google-generativeai`, `python-dotenv`

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aiadmin-provana/Sonnet-full-context-2.git
   cd Sonnet-full-context-2
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**
   Create `config/.env` file:
   ```env
   GOOGLE_AI_API_KEY="your-gemini-api-key-here"
   ```

## 💻 Usage

### 🎯 Quick Start (Recommended)

**Windows:**
```batch
run_workflow.bat
```

**Unix/Linux/Mac:**
```bash
chmod +x run_workflow.sh
./run_workflow.sh
```

### ⚙️ Manual Execution

The system requires scripts to be run in a specific sequence:

#### 1. Extract Ticket Information
```bash
python src/ticket_info.py
```
- **Input**: `data/ticket/ticket_data/ticket_data.txt`
- **Output**: `data/ticket/ticket_info_json/ticket_info.json`
- **Purpose**: Extracts structured information (user, company, Sonnet IDs, issue description)

#### 2. Find Best Matching SOP
```bash
python src/sop_matcher.py
```
- **Input**: `data/ticket/ticket_info_json/ticket_info.json`
- **Output**: `outputs/sop/ticket_data.txt`
- **Purpose**: Identifies the most relevant SOP file from knowledge base

#### 3. Load SOP Content
```bash
python src/sop_loader.py
```
- **Input**: `outputs/sop/ticket_data.txt`
- **Output**: `data/SOP_content/content.txt`
- **Purpose**: Extracts the actual SOP procedure content

#### 4. Generate Tailored Solution
```bash
python src/solution_generator.py
```
- **Input**: `data/ticket/ticket_info_json/ticket_info.json` + `data/SOP_content/content.txt`
- **Output**: `outputs/final_solution/ticket_data.txt`
- **Purpose**: Creates personalized customer response

### Quick Start Example

1. **Place your ticket in the system**:
   ```
   data/ticket/ticket_data/ticket_data.txt
   ```

2. **Run the complete workflow**:
   ```bash
   python src/ticket_info.py
   python src/sop_matcher.py
   python src/sop_loader.py
   python src/solution_generator.py
   ```

   **Or use the convenience scripts**:
   - Windows: `run_workflow.bat`
   - Unix/Linux/Mac: `./run_workflow.sh`

3. **Get your tailored solution**:
   ```
   outputs/final_solution/ticket_data.txt
   ```

## Script Details

### ticket_info.py
- **Purpose**: AI-powered ticket information extraction
- **AI Model**: Gemini 1.5 Flash (temperature=0)
- **Features**:
  - Extracts user names, company names, Sonnet IDs, IP addresses
  - Handles multiple Sonnet IDs
  - Flexible field detection
  - JSON output with proper formatting

### sop_matcher.py
- **Purpose**: Intelligent SOP file matching
- **AI Model**: Gemini 1.5 Flash (temperature=0)
- **Features**:
  - Processes 13,568+ lines of knowledge base
  - Uses structured ticket data for better matching
  - Fallback to raw text if JSON unavailable
  - Confidence-based file selection

### sop_loader.py
- **Purpose**: SOP content extraction and storage
- **Features**:
  - Parses file matching results
  - Loads content from source documents
  - Saves to standardized location
  - Error handling and validation

### solution_generator.py
- **Purpose**: Personalized solution generation
- **AI Model**: Gemini 1.5 Flash (temperature=0)
- **Features**:
  - Combines SOP procedures with ticket specifics
  - Dynamic field processing (no hardcoded fields)
  - Professional response formatting
  - Includes customer names, IDs, and specific details

## 🎯 Recent Improvements

### ✅ Version 2.0 Updates (August 2025)

**🏗️ Project Structure Optimization:**
- Moved all Python files to `src/` directory for better organization
- Added comprehensive `.gitignore` with 60+ protected file patterns
- Created `.gitkeep` files to preserve essential directory structure
- Updated all path references for the new structure

**📝 File Naming Standardization:**
- `simple_gemini_matcher.py` → `sop_matcher.py` (removed implementation details)
- `final.py` → `solution_generator.py` (descriptive functionality name)
- All files now use professional, clear naming conventions

**🚀 Convenience Enhancements:**
- Added `run_workflow.bat` for Windows with error handling
- Added `run_workflow.sh` for Unix/Linux/Mac systems
- Both scripts provide step-by-step progress reporting
- Automatic error detection and user-friendly messages

**🔐 Security Improvements:**
- Comprehensive `.gitignore` protecting sensitive data
- API keys and credentials never committed to git
- Generated outputs and temporary files properly excluded
- Knowledge base and source code properly preserved

**📚 Documentation Updates:**
- Enhanced README with emoji-based navigation
- Added security and git configuration sections
- Comprehensive installation and usage instructions
- Clear project structure visualization

## 🛠️ Configuration

### Environment Variables
```env
# Required
GOOGLE_AI_API_KEY=your_gemini_api_key_here

# Optional (with defaults)
TEMPERATURE=0
MAX_OUTPUT_TOKENS=unlimited
```

### AI Model Settings
- **Provider**: Google Gemini
- **Model**: `gemini-1.5-flash`
- **Temperature**: `0` (deterministic responses)
- **Context Window**: Full knowledge base + structured ticket data
- **Output Format**: Structured JSON and formatted text

## 🧪 Testing & Validation

### Sample Workflow Test
```bash
# Test with provided sample ticket
echo "User: Sneha Yadav
Company: Continental Finance Company
Sonnet ID: 65025643
Issue: Remove LCS disputes from Sonnet" > data/ticket/ticket_data/ticket_data.txt

# Run workflow
./run_workflow.sh  # or run_workflow.bat on Windows

# Check results
cat outputs/final_solution/ticket_data.txt
```

### Expected Output
- ✅ Extracted ticket information as JSON
- ✅ Matched to "FILE 36: Removing LCS Disputes.txt"
- ✅ Generated personalized solution with customer details
- ✅ Professional formatting with step-by-step instructions

## Sample Input/Output

### Input Ticket (ticket_data.txt)
```
From: sneha.yadav@example.com
Subject: LCS Dispute Removal Request

Hi,
I need to remove LCS disputes from Sonnet for Continental Finance Company.
Sonnet ID: 65025643
Please help with this ASAP.

Thanks,
Sneha Yadav
```

### Extracted Information (ticket_info.json)
```json
{
  "user": "Sneha Yadav",
  "IP address": null,
  "sonnet ID or Id": ["65025643"],
  "company_name": "Continental Finance Company",
  "issue_description": "Remove LCS disputes from Sonnet."
}
```

### Matched SOP (outputs/sop/ticket_data.txt)
```
FILE 36: Removing LCS Disputes.txt
```

### Final Solution (outputs/final_solution/ticket_data.txt)
```
Subject: Solution for Ticket 65025643

Hello Sneha Yadav,

Here is the tailored step-by-step solution for removing LCS disputes for Continental Finance Company (Sonnet ID: 65025643):

1. Access Sonnet and select Continental Finance Company...
2. Search for dispute using Sonnet ID "65025643"...
3. Execute SQL query: UPDATE dispute SET sonnet_status = 'Worked' WHERE id = 65025643...

[Complete detailed procedure]
```

## Features

### Dynamic Field Processing
- **No Hardcoded Fields**: System adapts to any JSON structure
- **Flexible Extraction**: Handles varying ticket formats
- **Intelligent Formatting**: Converts field names (user_name → User Name)
- **Type Handling**: Processes strings, lists, and null values appropriately

### Fallback Mechanisms
- **JSON to Raw Text**: Falls back to raw ticket if structured data unavailable
- **API Failure Handling**: Provides default responses if AI services fail
- **File Not Found**: Graceful error handling with informative messages

### AI Optimization
- **Temperature 0**: Ensures consistent, deterministic responses
- **Context-Aware**: Uses full knowledge base for accurate matching
- **Structured Prompts**: Optimized prompts for reliable AI responses

## 🔧 Troubleshooting

### Common Issues

**🔑 API Key Errors**
```bash
Error loading config: [API key issue]
```
- Solution: Check `config/.env` file exists and contains valid `GOOGLE_AI_API_KEY`
- Verify API key has Gemini API access enabled

**📁 File Not Found Errors**
```bash
Error loading ticket data: [Errno 2] No such file or directory
```
- Solution: Ensure `data/ticket/ticket_data/ticket_data.txt` exists
- Check file has content and proper encoding (UTF-8)

**🤖 AI Response Issues**
```bash
Error parsing JSON response: [JSON decode error]
```
- Solution: Check API key quota and internet connection
- Retry the operation - temporary API issues are common

**📂 Path Issues (After Moving Files)**
```bash
ModuleNotFoundError or path not found errors
```
- Solution: Run scripts from project root directory
- Use `python src/script_name.py` format

### Debug Mode
Enable detailed logging by setting environment variable:
```bash
export DEBUG=true  # Unix/Linux/Mac
set DEBUG=true     # Windows
```

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Follow existing code style and naming conventions
4. Test with sample tickets before submitting
5. Update documentation if adding new features

### Code Standards
- **Naming**: Use descriptive, professional file/function names
- **Documentation**: Include docstrings for all functions
- **Error Handling**: Implement graceful error handling
- **Security**: Never commit API keys or sensitive data

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/aiadmin-provana/Sonnet-full-context-2/issues)
- **Documentation**: This README and inline code comments
- **API Documentation**: [Google Gemini API Docs](https://ai.google.dev/docs)

## 🙏 Acknowledgments

- **Google Gemini AI** for powerful language processing capabilities
- **Open Source Community** for Python libraries and tools
- **Contributors** who helped improve the project structure and documentation

---

**📊 Project Stats:**
- 🧠 **Knowledge Base**: 107 SOP documents (13,568+ lines)
- 🤖 **AI Model**: Gemini 1.5 Flash (Temperature: 0)
- 📁 **Project Structure**: 4 core Python modules, organized source code
- 🔐 **Security**: Comprehensive .gitignore with 60+ protected patterns
- 🚀 **Convenience**: One-click workflow execution scripts
- 📈 **Success Rate**: Deterministic AI responses for consistent results
   Error: GOOGLE_AI_API_KEY not found
   ```
   - Check `config/.env` file exists
   - Verify API key is valid and active

2. **File Not Found**
   ```
   Error loading ticket data
   ```
   - Ensure `data/ticket/ticket_data/ticket_data.txt` exists
   - Check file permissions

3. **JSON Parse Errors**
   ```
   Error parsing JSON response
   ```
   - Usually temporary AI response formatting issue
   - Re-run the script

### Debug Mode
Enable verbose logging by modifying script headers:
```python
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:
- Create an issue in the repository
- Check existing documentation
- Review troubleshooting section

## Changelog

### v1.0.0
- Initial release with core functionality
- AI-powered ticket processing
- Dynamic field handling
- Organized folder structure
- Comprehensive fallback mechanisms

---

**Built with ❤️ using Google Gemini AI**
