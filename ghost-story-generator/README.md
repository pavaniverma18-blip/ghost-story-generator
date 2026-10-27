# 👻 Ghost Story Generator

A beginner-friendly Streamlit app that creates spooky, mysterious, funny, or folklore-inspired stories using the open-weight **google/flan-t5-small** model with Hugging Face Transformers.

## Features
- Generate a story from your own idea
- Choose a mood and approximate length
- Add an optional setting
- Download the generated story as a `.txt` file
- Run inference locally after the model has been downloaded and cached

## Tech stack
- Python
- Streamlit
- Hugging Face Transformers
- `google/flan-t5-small`
- PyTorch

## Requirements
- Python 3.10 or 3.11 recommended
- Internet connection for the first run to download the model
- Free disk space for dependencies and model files

## Run on Windows

1. Extract the ZIP.
2. Open the extracted folder in VS Code.
3. Open Terminal in VS Code.
4. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

5. Activate it:

   ```powershell
   .venv\\Scripts\\activate
   ```

6. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

7. Start the app:

   ```powershell
   python -m streamlit run app.py
   ```

8. Open the local address Streamlit prints, usually `http://localhost:8501`.

## Why open-source AI matters

The app uses an openly available model instead of sending each story prompt to a closed, paid text-generation API. After the model files are cached, generation can run on the user's machine, giving the user more control over prompts. The first setup still requires internet to download dependencies and model files. Speed and output quality depend on the hardware and model.

## Notes
- Generated stories may be repetitive or inaccurate; review before sharing.
- Check the model's license and terms before redistributing model weights or using the project commercially.
- This is a learning project, not a production application.

## Project structure
```text
ghost-story-generator/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
