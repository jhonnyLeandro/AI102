mkdir ai102-study && cd ai102-study
python -m venv .venv

# Activar
source .venv/bin/activate          # macOS/Linux
.venv\Scripts\activate             # Windows PowerShell

# Instalar
pip install --upgrade pip
pip install azure-identity `
            azure-ai-vision-imageanalysis `
            azure-ai-documentintelligence `
            azure-ai-formrecognizer `
            azure-cognitiveservices-vision-customvision `
            python-dotenv