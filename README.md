Requirements
================
- Python 3 
- OpenAI Python package
- An OpenAI API key

Setup Instructions:
====================
1. Install the OpenAI Python package to interact with the OpenAI API. You can do this by running the following command in your terminal:

```bash
pip install openai
```

2. Export your OpenAI API key as an environment variable in the terminal, remember to replace your API key with the actual key you received from OpenAI:

```bash
EXPORT OPENAI_API_KEY='YOUR_API_KEY'
```

3. Run the script with the prompt and specify the output file where the response will be saved. 

```bash
Usage:
```bash
python main.py <your input> <output_file>
```

Example: 
```
python main.py "What is the capital of France?" output.txt
```

