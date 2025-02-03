# Data Analyst Client Simulator (DACS)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/Python-3.11.7-blue.svg)
![Flask Version](https://img.shields.io/badge/Flask-3.0.0-blue.svg)
![Version](https://img.shields.io/badge/Version-1.3.1-green.svg)

## Overview
The Data Analyst Client Simulator (DACS) is a web application designed to provide aspiring data analysts with a realistic environment to practice their skills. It generates simulated client interactions and corresponding datasets, allowing users to engage in practical data analysis tasks.

**Purpose:** To offer a dynamic and challenging environment for improving data analysis skills, building portfolios, and developing communication abilities through realistic scenarios.

**Value Proposition:** DACS bridges the gap between theoretical knowledge and real-world application, providing aspiring data analysts with the practical experience needed for professional roles.

**Target Audience:** Aspiring and entry-level data analysts, data science students, and individuals building a data analysis portfolio.

### Key Features
* **Scenario Generation:** Creates realistic business scenarios with client profiles and problems using Google Gemini API
* **Dataset Generation:** Produces corresponding datasets with diverse data types and realistic quality issues
* **Web Interface:** Simple UI for generating and downloading scenarios and datasets

### Future Enhancements
* Interactive AI client for guidance and context
* AI-powered feedback on analysis approaches
* Portfolio building tools

## Quick Start

### Prerequisites
* **Python:** Version 3.11.7 or higher
* **Git:** For version control ([git-scm.com](https://git-scm.com/))
* **Google Cloud API Key:** Required for Gemini API integration ([Google Cloud Console](https://console.cloud.google.com/))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pauloarayasantiago/dacs_webapp.git
cd dacs_webapp
```

2. Create and activate a virtual environment:
```bash
# Windows with Git Bash
python -m venv .venv
source .venv/Scripts/activate

# Unix/macOS
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Windows
echo GOOGLE_API_KEY=your_api_key_here > .env

# Unix/macOS
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

5. Run the application:
```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000/`.

### Using the Application

1. Open `http://127.0.0.1:5000/` in your web browser
2. Click "Generate Scenario" to create a new client case
3. Review the generated scenario and business problem
4. Download the corresponding dataset
5. Begin your analysis!

## Development

### Code Style
```bash
# Format code
black src/

# Type checking
mypy src/

# Linting
flake8 src/
```

### Testing
```bash
# Run tests
pytest

# Generate coverage report
pytest --cov=src tests/
```

## Project Structure
```
dacs_webapp/
├── src/                    # Source code
├── docs/                   # Documentation
├── trials/                 # Generated client data
├── archive/               # Archived files
├── requirements.txt       # pip requirements
├── run.py                # Entry point
├── dockerfile            # Docker configuration
├── SECURITY.md          # Security guidelines
├── VERSION              # Version file
├── CHANGELOG.md         # Version history
└── README.md            # This file
```

## API Integration

### Google Gemini API
* Uses `google-generativeai` library for scenario generation
* Requires API key set as `GOOGLE_API_KEY` environment variable
* Uses `gemini-1.5-pro-latest` model for text generation
* Supports both text and multimedia inputs
* Includes robust error handling for API interactions

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Versioning
This project follows [Semantic Versioning](https://semver.org/) and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

* See [CHANGELOG.md](CHANGELOG.md) for version history
* Version format: MAJOR.MINOR.PATCH
  * MAJOR: Incompatible API changes
  * MINOR: New backwards-compatible features
  * PATCH: Backwards-compatible bug fixes

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or issues, please [open an issue](https://github.com/pauloarayasantiago/dacs_webapp/issues) on GitHub.

## Acknowledgements
* [Flask](https://flask.palletsprojects.com/): Web framework
* [Google Generative AI](https://ai.google.dev/): Text generation
* [Pandas](https://pandas.pydata.org/): Data manipulation
* [Faker](https://faker.readthedocs.io/): Test data generation

## Security
Please review our [Security Policy](SECURITY.md) for guidelines on reporting security vulnerabilities.

## Docker Support
A Dockerfile is provided for containerized deployment. Build and run instructions:

```bash
# Build the image
docker build -t dacs-webapp .

# Run the container
docker run -p 5000:5000 -e GOOGLE_API_KEY=your_api_key_here dacs-webapp
```

