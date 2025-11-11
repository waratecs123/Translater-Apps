# Text Network Translator (Russian-Chinese)

## Project Overview

A desktop application designed for bidirectional translation between Russian and Chinese languages, incorporating text-to-speech functionality for enhanced usability. This tool serves as a practical solution for linguistic communication, educational purposes, and cross-cultural interactions.

## Functional Specifications

### Core Translation Capabilities
- **Bidirectional Language Support**: Seamless translation between Russian and Chinese
- **Real-time Translation Processing**: Instant conversion of text between selected languages
- **Language Direction Configuration**: 
  - Source language selection (default: Russian)
  - Target language selection (default: Chinese)

### Audio Features
- **Integrated Text-to-Speech Engine**: 
  - Russian language vocalization
  - Chinese language vocalization
- **Instant Audio Playback**: One-click pronunciation assistance
- **Native Speech Synthesis**: Utilization of system-level text-to-speech libraries

### User Interface Utilities
- **Clipboard Integration**: 
  - Copy source text to system clipboard
  - Copy translated text to system clipboard
- **Text Management**:
  - Instant text field clearing
  - Large, readable text areas for comfortable typing
- **Visual Design**: Clean, intuitive interface optimized for extended use

## Technical Requirements

### Prerequisites
- Python 3.7 or higher
- Operating System: Windows, macOS, or Linux
- Internet connection for translation services

### Dependencies
- **tkinter**: Standard Python GUI toolkit
- **pyttsx3**: Cross-platform text-to-speech library
- **googletrans**: Google Translate API interface
- **pyperclip**: Cross-platform clipboard operations

## Installation Procedure

### Step 1: Repository Acquisition
```bash
git clone https://github.com/yourusername/translator-app.git
cd translator-app
```

### Step 2: Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv translator_env

# Activate virtual environment
# Windows:
translator_env\Scripts\activate
# Linux/macOS:
source translator_env/bin/activate
```

### Step 3: Dependency Installation
```bash
pip install -r requirements.txt
```

### Alternative: Manual Dependency Installation
```bash
pip install tkinter pyttsx3 googletrans==3.1.0a0 pyperclip
```

## Operational Instructions

### Initial Setup
1. Launch the application:
```bash
python TRANSLATER.py
```

### Translation Workflow
1. **Language Configuration**:
   - Select source language from top dropdown menu
   - Select target language from bottom dropdown menu

2. **Text Input**:
   - Enter or paste source text into the upper text area
   - Text can be typed directly or pasted from clipboard

3. **Translation Execution**:
   - Click the "Перевести" (Translate) button to initiate translation
   - Translated text appears in the lower text area

### Functional Controls
- **Copy Source Text**: Transfers original text to system clipboard
- **Copy Translated Text**: Transfers translated text to system clipboard
- **Clear Text**: Empties both text areas for new input
- **Speak Text**: Activates text-to-speech for respective text fields

## Technical Architecture

### Application Structure
- **Main Window**: Primary GUI container with responsive layout
- **Text Areas**: Scrollable text fields with adjustable sizing
- **Control Panel**: Organized button grid for user operations
- **Language Selectors**: Dropdown menus for language configuration

### Translation Engine
- **Backend Service**: Google Translate API integration
- **Error Handling**: Network failure management and timeout protocols
- **Encoding Support**: Full Unicode compliance for Cyrillic and Chinese characters

### Audio System
- **Speech Synthesis**: Platform-independent text-to-speech engine
- **Language Detection**: Automatic voice selection based on text content
- **Playback Control**: Concurrent speech prevention and audio queue management

## Troubleshooting

### Common Issues and Solutions

**Translation Failures**:
- Verify internet connectivity
- Check for API service limitations
- Confirm text encoding compatibility

**Audio Function Issues**:
- Validate system text-to-speech capabilities
- Check audio output device configuration
- Verify language pack installation for respective languages

**Interface Problems**:
- Ensure display scaling compatibility
- Confirm system theme compatibility
- Verify Python tkinter library installation

## System Compatibility

### Supported Platforms
- **Windows**: 7, 8, 10, 11 (32-bit and 64-bit)
- **macOS**: 10.14 (Mojave) and newer
- **Linux**: Ubuntu 16.04+, Fedora 28+, CentOS 7+

### Language Support
- **Russian**: Complete Cyrillic character set support
- **Chinese**: Simplified Chinese character support (GB2312, UTF-8)

## Performance Characteristics

- **Translation Speed**: Dependent on network latency and text length
- **Memory Usage**: Optimized for standard desktop environments
- **Startup Time**: Minimal initialization requirements

## Development and Customization

The application architecture supports potential enhancements including:
- Additional language pairs
- Custom translation engine integration
- Advanced text formatting options
- Translation history and favorites
- Keyboard shortcut implementation

## License and Distribution

This project is available under open-source licensing provisions. Please refer to the LICENSE file in the project repository for complete distribution terms and conditions.

## Support and Maintenance

For technical support, please refer to the project's issue tracking system. Regular updates will address compatibility requirements and feature enhancements based on user feedback.
