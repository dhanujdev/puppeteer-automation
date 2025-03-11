# Puppeteer Automation with Python

This repository contains examples of web automation using Puppeteer with Python through the `pyppeteer` package.

## What is Puppeteer?

Puppeteer is a Node.js library that provides a high-level API to control Chrome/Chromium over the DevTools Protocol. `pyppeteer` is a Python port of Puppeteer.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/dhanujdev/puppeteer-automation.git
cd puppeteer-automation
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Examples

This repository includes the following examples:

### 1. Screenshot Example

Takes a screenshot of a webpage:

```bash
python3 screenshot_example.py
```

### 2. Form Automation

Demonstrates how to fill out and submit a form:

```bash
python3 form_automation.py
```

## Common Use Cases

- Web scraping
- Automated testing
- Generating screenshots and PDFs of pages
- Automating form submission
- Performance testing
- Creating automated workflows

## Additional Resources

- [Pyppeteer Documentation](https://miyakogi.github.io/pyppeteer/)
- [Puppeteer Documentation](https://pptr.dev/)

## License

MIT