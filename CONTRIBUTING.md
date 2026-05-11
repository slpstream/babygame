# Contributing to Baby Game

Thank you for your interest in contributing to the Baby's First Computer project! This document provides guidelines and instructions for contributing.

## Project Structure

```
babygame/
├── python/           # Python implementation
│   ├── babycolor.py  # Main Python game script
│   ├── requirements.txt
│   └── SPEC.md
├── web/              # Web implementation
│   ├── babygame.html # Main web game
│   ├── index.html    # Landing page
│   └── SPEC.md
├── LICENSE
├── README.md
├── setup.py
├── requirements.txt
└── CONTRIBUTING.md
```

## Development Setup

### Python Version
1. Clone the repository:
   ```bash
   git clone https://github.com/slpstream/babygame.git
   cd babygame
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Python game:
   ```bash
   python python/babycolor.py
   ```

### Web Version
1. The web version requires no installation
2. Open `web/babygame.html` in a web browser
3. Or use the development server:
   ```bash
   python -m http.server 8000
   ```
   Then open `http://localhost:8000/web/babygame.html`

## Making Changes

1. **Fork the repository** and create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes** following the existing code style.

3. **Test your changes**:
   - For Python: Run the game and ensure it works
   - For Web: Test in at least one modern browser

4. **Commit your changes** with descriptive commit messages:
   ```bash
   git commit -m "Add amazing feature"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**

## Coding Standards

### Python
- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Add docstrings for functions and modules
- Keep imports organized

### JavaScript/HTML/CSS
- Use modern ES6+ JavaScript features
- Use semantic HTML
- Follow responsive design principles
- Comment complex logic

### General Guidelines
- Keep the code simple and maintainable
- Write clear, descriptive variable and function names
- Add comments for non-obvious logic
- Ensure backward compatibility when possible

## Testing

- Test on different platforms (Windows, macOS, Linux)
- Test on different browsers for web version
- Ensure no regressions in existing functionality
- Test with both keyboard and touch input (for web)

## Reporting Issues

When reporting issues, please include:
1. Description of the problem
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Screenshots (if applicable)
6. Platform/browser information
7. Error messages or logs

## Feature Requests

Feature requests are welcome! Please:
1. Check if the feature already exists
2. Explain the use case
3. Describe the expected behavior
4. Consider if it aligns with the project's scope (simple baby game)

## Documentation

- Update README.md if adding new features
- Update SPEC.md files if changing specifications
- Add comments for new complex functionality
- Keep installation instructions up to date

## Questions?

Feel free to open an issue for questions about the project or contribution process.
