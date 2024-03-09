# WhatsUpWhatsApp - WhatsApp Chat Analyzer

## Overview

WhatsUpWhatsApp is a versatile Python-based tool designed to analyze and provide insights into WhatsApp chat data. Whether you're curious about the dynamics of a group chat, individual conversations, or just interested in statistical patterns, this program helps you make sense of your WhatsApp interactions. The tool is built to be user-friendly, offering both data analysis and visualization features.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

### Data Loading

Load your WhatsApp chat data effortlessly by providing the file path.

### Cleaning

Clean and preprocess the chat data for accurate analysis, ensuring a smooth and error-free process.

### Data Extraction

Extract relevant information from your chat data to create a structured dataset ready for analysis.

### Analysis and Visualization

Gain insights into your chat data through various analysis and visualization tools, allowing you to interpret the information effectively.

### User-Friendly

The program provides a simple and intuitive interface, making it accessible for users with varying technical backgrounds.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (>=3.6)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/WhatsUpWhatsApp.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd WhatsUpWhatsApp
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

4. **Run the Program:**

    ```bash
    python main.py
    ```

5. **Enter WhatsApp Chat File Path:**

    Enter the path to your WhatsApp chat file when prompted.

6. **Explore the Insights:**

    Sit back and let WhatsUpWhatsApp analyze and visualize your chat data.

## Example Usage

```python
if __name__ == "__main__":
    # File path input
    file_path = input("Enter the path to the WhatsApp chat file: ")

    # Load and clean data
    chats = load_chat_data(file_path)
    chats = clean_data(chats)

    # Extract and analyze data
    df = extract_chat_data(chats)
    analyze_and_visualize(df)
```

## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.

## Acknowledgments

Special thanks to the open-source community for inspiration and support.

Happy analyzing with WhatsUpWhatsApp! 🚀
