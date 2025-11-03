# 🌙 Storyland - AI Bedtime Story Generator

An AI-powered personalized bedtime story generator that creates unique, engaging stories for children using DeepSeek API.

## ✨ Features

- 🤖 **AI-Powered**: Uses DeepSeek's advanced language model
- 🌏 **Multilingual**: Auto-detects and responds in English or Chinese
- 🎨 **Personalized**: Stories tailored to child's name, age, interests, and theme
- 📖 **Multiple Modes**: 
  - Regular bedtime stories
  - Interactive choose-your-own-adventure stories
- 💾 **Save Stories**: Export generated stories to text files

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- DeepSeek API key ([Get one here](https://platform.deepseek.com/))

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yma97/storyland.git
cd storyland
```
2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create .env file:
```bash
echo "DEEPSEEK_API_KEY=your-api-key-here" > .env
```
5. Run the program:
```bash
python src/main.py
```
