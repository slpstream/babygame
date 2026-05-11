# Changelog

All notable changes to the Baby Color Game project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Open-source release preparation
- MIT License file
- Comprehensive documentation (README, CONTRIBUTING)
- Python packaging (setup.py, pyproject.toml)
- Web package.json for web version
- Git ignore file for Python projects
- Landing page for web version
- Changelog file

### Changed
- Restructured babycolor.py to have proper main() function for packaging
- Updated project structure documentation
- Renamed web files for clarity (babygame.html → game.html, index.html → babygame.html)

### Fixed
- Proper entry point for Python package installation
- Updated all documentation with correct file paths

## [1.0.0] - 2026-05-11

### Added
- Initial open-source release
- Python desktop implementation using PyGame
- Web browser implementation using HTML/CSS/JavaScript
- 8 high-contrast colors with musical tones
- Fullscreen support for both versions
- Touch support for web version
- Simple keyboard/touch controls
- Parental supervision hints

### Technical Details
- Python: PyGame + NumPy for audio generation
- Web: Pure HTML/CSS/JS with Web Audio API
- Cross-platform compatibility
- No external dependencies for web version