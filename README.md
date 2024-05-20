# UnblankObfV2: A BlankObfV2 Deobfuscator

![GitHub](https://img.shields.io/github/license/lululepu/UnblankObfV2)
![Python](https://img.shields.io/badge/Python-3.11%3C3.x-blue)

UnblankObfV2 is a Python script designed to deobfuscate scripts that have been obfuscated using the BlankObfV2 obfuscation method. This tool is useful for developers who need to analyze or reverse engineer obfuscated code.

## Features

- Detects the layer of obfuscation used by BlankObfV2.
- Deobfuscates code obfuscated with BlankObfV2, handling multiple layers of obfuscation.

## Requirements

- Python 3.11 or higher

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/lululepu/UnblankObfV2.git
cd UnblankObfV2
pip install -r requirements.txt
```

## Usage
The script can be run from the command line. Below are the available command-line options:
```
python unblankobfv2.py --input PATH_TO_OBFUSCATED_FILE [--output PATH_TO_OUTPUT_FILE]
```

## Arguments
- `--input`, `-i`: (Required) Path to the file that needs to be deobfuscated.
- `--output`, `-o`: (Optional) Path to the file where the deobfuscated script will be written. If not provided, the output file will be named deobfuscated_(filename).py.

## Script Details
### Functions
- `get_layer(code: str) -> dict`: Determines the obfuscation layer of the given code.
- `l1(code) -> str`: Deobfuscates code that is obfuscated using layer 1.
- `l2(code) -> str`: Deobfuscates code that is obfuscated using layer 2.
- `l3(code) -> str`: Deobfuscates code that is obfuscated using layer 3.
- `deobf(code: str) -> str`: Recursively deobfuscates the code based on its obfuscation layer.
- `main() -> None`: Main function that handles command-line arguments and file operations.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/lululepu/UnblankObfV2/blob/main/LICENSE) file for details.

