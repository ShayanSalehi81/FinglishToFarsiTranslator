# FinglishToFarsiTranslator

This repository is a Natural Language Processing (NLP) project focused on translating "Finglish" (Persian written in Latin script) to proper Persian (in Farsi script) using various NLP and Machine Learning techniques. The project includes utilities for tokenization, lemmatization, biword analysis, and semantic similarity, leveraging models like BERT for optimal translation accuracy.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Scripts and Code Details](#scripts-and-code-details)
- [Dataset](#dataset)
- [Documentation](#documentation)
- [License](#license)

## Overview

This project focuses on processing Finglish input and converting it into proper Persian text. It makes extensive use of:
- **BERT** models for semantic similarity scoring,
- **Hazm** (a Persian NLP library) for lemmatization,
- **Custom biword dictionaries** to improve translation accuracy.

The core functionality involves transforming Finglish inputs into corresponding Farsi representations by analyzing both individual word and phrase patterns and calculating the most probable accurate translations.

## Project Structure

```plaintext
FinglishToFarsiTranslator
├── Code/
│   ├── accept_invite.py            # Handles auto-acceptance of bot invites for chat interactions
│   ├── chose_best_sentence.py       # Selects the best sentence match based on semantic similarity using BERT
│   ├── configuration.yaml           # Configuration file for Matrix bot connections
│   ├── consider_biwords.py          # Identifies and considers biwords (two-word sequences) for accurate translation
│   ├── convert.py                   # Main translation script for Finglish to Farsi conversion
│   ├── dictionary_lemmatizer.py     # Lemmatizes dictionary files to optimize word lookup
│   ├── generate_mapping_json.py     # Generates mapping for Finglish to Persian letters
│   ├── help.py                      # Helper script providing usage instructions
│   ├── make_persian_biwords_dataset.py # Script to generate a biword dataset from Persian text sources
│   ├── test.py                      # Testing script for verifying the functionality
│
├── Dataset/
│   ├── first_letters_mapping.json   # Mapping of Finglish to Farsi for the first letters
│   ├── letters_mapping.json         # Mapping of Finglish letters to Farsi letters
│   ├── make_persian_biwords_dataset.ipynb # Jupyter Notebook for biword dataset creation
│   ├── persian-wikipedia_lemmatized.txt   # Lemmatized Persian text from Wikipedia
│   ├── persian-wikipedia.txt               # Raw Persian text from Wikipedia
│
├── Documentation/
│   ├── NLP-HW2-Documentation.pdf    # Detailed documentation for the project
│
├── LICENSE                          # License file
└── README.md                        # Project README
```

## Installation

### Prerequisites

- **Python 3.7+**
- **Transformers library** for BERT-based models
- **Hazm** for Persian text processing
- **gdown** for file downloading
- **scikit-learn** for cosine similarity calculations

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ShayanSalehi81/FinglishToFarsiTranslator.git
   cd FinglishToFarsiTranslator
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download necessary resources and models as specified in individual scripts.

## Usage

### Finglish to Farsi Conversion

To use the main conversion functionality, you can run the `convert.py` script, which takes a Finglish sentence and returns the most probable Persian sentence based on the pre-trained models and dictionaries.

Example:
```python
from convert import convert

# Convert a Finglish sentence to Farsi
sentence = "forsat ha, mesle aber 123.541 migozarand; bayad ghadreshan ra bedanim."
result = convert(sentence)
print(result[:10])  # Show top 10 possible translations
```

### Biword Dataset Creation

You can create or update the biword dictionary by running the `make_persian_biwords_dataset.py` script, which processes a raw Persian text file and generates biwords, storing their counts.

### Configuration

The `configuration.yaml` file defines settings for the Matrix chat bot integration, allowing Finglish to Farsi conversion to be triggered within chat rooms.

**Example configuration:**
```yaml
connectors:
  matrix:
    mxid: "@bot_finglish2persian:bot.parsi.ai"
    password: "YOUR_PASSWORD"
    rooms:
      'main': '#NLP_HW2:bot.parsi.ai'
    homeserver: "https://bot.parsi.ai"
    enable_encryption: True

skills:
  test:
    path: ./test.py
  accept_invite:
    path: ./accept_invite.py
  help:
    path: ./help.py
```

## Scripts and Code Details

- **accept_invite.py**: Accepts bot invitations for interacting in chat rooms.
- **chose_best_sentence.py**: Uses a BERT model to pick the most semantically similar sentence from a set of options.
- **consider_biwords.py**: Considers biword sequences to improve translation accuracy and checks against a biword dictionary.
- **convert.py**: Main script for Finglish to Farsi conversion using word mappings, biwords, and dictionary-based lookups.
- **dictionary_lemmatizer.py**: Lemmatizes a Persian word frequency dictionary for efficient lookup and processing.
- **generate_mapping_json.py**: Creates JSON mappings for Finglish letters to Farsi equivalents.
- **make_persian_biwords_dataset.py**: Generates a biword frequency dataset for Persian by processing a large text corpus.

## Dataset

The **Dataset** folder contains essential resources, including:
- **first_letters_mapping.json**: Maps initial Finglish letters to probable Farsi equivalents.
- **letters_mapping.json**: Maps Finglish letters to Farsi letters.
- **persian-wikipedia.txt**: Raw Persian text corpus.
- **persian-wikipedia_lemmatized.txt**: Lemmatized version of the Persian corpus.

The biword dataset, `biword_counts.txt`, is generated through `make_persian_biwords_dataset.py` or downloaded automatically if missing.

## Documentation

Detailed documentation for this project, including algorithm explanations and methodology, is available in `NLP-HW2-Documentation.pdf` within the **Documentation** folder.

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file in this repository.