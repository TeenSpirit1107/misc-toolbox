# Rosalind's Misc Toolbox

## ☺️ Introduction

- This toolbox is originally designed for my personal use. It contains a miscellaneous collection of tools, including system cleaning, media handling and calculating. Not focused on a specific topic.

- I use it in ubuntu 22.04, but most tools probably works for other systems as well.

## 🧠 Utilites

### `calculator/machine_learning.py`

- **Entropy Calculator**: Interactively computes binary entropy.
- **Partition Entropy**: Computes weighted entropy across partitions (e.g., for decision trees).
- **Cross Entropy Loss**: Implements cross-entropy loss for model evaluation.

### `media/pdf_handling.py`

- **Merge PDFs to One Page**: Guides the user through selecting PDFs from the `input/` directory and merges them into a single file in the `output/` directory.

### `media/console_effect.py`

- **Typing Simulation**: Creates either word-wise or character-wise typewriter-style output with adjustable speed—ideal for CLI storytelling or dramatic logging.

### `sys/clean.sh`

- system clean-up for **ubuntu 22.04**. Can choose to clean:

    - cache
    - log
    - apt cache and unnecessary packages
    - conda cache and unnecessary packages

---

## 🚀 Getting Started

1. Install the dependencies

    ```shell
    pip install -r requirements.txt
    ```

2. for a bash file named `file_name.sh`, you may have to run this before executing it:

    ```shell
    chmod +x file_name.sh
    ```

3. some bash files need to be run as root:

    ```shell
    sudo ./file_name.sh
    ```
