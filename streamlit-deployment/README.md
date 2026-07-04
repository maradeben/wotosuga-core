# Wotosuga Core Streamlit App

This app mirrors the notebook workflow for diabetes risk prediction using the trained LightGBM model and SHAP explanations.

## Run locally

```bash
cd /home/maradeben/dev/wotosuga-core/streamlit-deployment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app uses the trained model and SHAP explainer from the repository folder at /home/maradeben/dev/wotosuga-core.
