from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
import streamlit as st
import json

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
MODEL_PATH = REPO_ROOT / "model_building" / "models" / "lgbm_model.pkl"
EXPLAINER_PATH = REPO_ROOT / "model_building" / "models" / "shap_explainer.pkl"
DATASET_PATH = REPO_ROOT / "streamlit-deployment" / "cat-values.json"

FEATURE_FIELDS = [
    "age",
    "height",
    "weight",
    "education",
    "income",
    "gen_health",
    "physical_health_days",
    "mental_health_days",
    "smoked_100_cigarettes",
    "drinks_alcohol",
    "had_coronary_heart_disease",
    "cost_barrier",
    "l_checkup",
    "had_stroke",
    "had_heart_attack",
    "has_personal_doctor",
    "sex",
    "marital_status",
    "employment_status",
    "exercise",
    "high_bp",
    "socioeconomic_tier",
]

# EDUCATION_LEVELS = [
#     "None or KG",
#     "Elementary (1-8)",
#     "Some high school (9-11)",
#     "High school graduate (12 or GED)",
#     "Some college (1-3 years) or Technical school",
#     "College graduate (4+ years)",
# ]


@st.cache_resource(show_spinner=False)
def load_assets():
    model = joblib.load(MODEL_PATH)
    explainer = joblib.load(EXPLAINER_PATH)
    with open(DATASET_PATH, 'r') as f:
        cat_values = json.load(f)
    return model, explainer, cat_values


def map_age(age: int) -> int:
    if age < 18:
        return 0
    elif age <= 24:
        return 1
    elif age >= 80:
        return 13
    return (age // 5) - 3



def map_education(education_level: str) -> int:
    education_map = {
        "None or KG": 1,
        "Elementary (1-8)": 2,
        "Some high school (9-11)": 3,
        "High school graduate (12 or GED)": 4,
        "Some college (1-3 years) or Technical school": 5,
        "College graduate (4+ years)": 6,
    }
    return education_map.get(education_level, 0)

def map_socioeconomic_tier(socioeconomic_tier: str) -> int:
    socioeconomic_map = {
        "Low (barely afford basic necessities)": 1,
        "Middle (comfortably afford basic necessities)": 2,
        "High (can afford luxury)": 3
    }

    return socioeconomic_map.get(socioeconomic_tier, 0)


def clean_feature_name(name: str) -> str:
    clean = name.replace("num__", "").replace("cat__", "")
    mapping = {
        "age": "Age",
        "bmi": "Body Mass Index (BMI)",
        "education": "Education Level",
        "income": "Income Level",
        "gen_health": "General Health Self-Rating",
        "physical_health_days": "Physical Health (Recent Bad Days)",
        "mental_health_days": "Mental Health (Recent Bad Days)",
        "smoked_100_cigarettes": "Smoked >= 100 Cigarettes Lifetime",
        "drinks_alcohol": "Alcohol Consumption",
        "had_stroke": "History of Stroke",
        "had_heart_attack": "History of Heart Attack",
        "had_coronary_heart_disease": "History of Coronary Heart Disease",
        "cost_barrier": "Healthcare Cost Barrier",
        "l_checkup": "Time Since Last Medical Checkup",
        "has_personal_doctor": "Has Personal Healthcare Provider",
        "socioeconomic_tier": "Socioeconomic Tier",
        "sex_Female": "Sex: Female",
        "sex_Male": "Sex: Male",
        "marital_status_Married/Cohabiting": "Marital Status: Married/Cohabiting",
        "marital_status_Previously Married": "Marital Status: Previously Married",
        "marital_status_Single": "Marital Status: Single",
        "employment_status_Employed": "Employment: Employed",
        "employment_status_Retired": "Employment: Retired",
        "employment_status_Student/Homemaker": "Employment: Student/Homemaker",
        "employment_status_Unable to work": "Employment: Unable to Work",
        "employment_status_Unemployed": "Employment: Unemployed",
        "exercise_False": "Physical Exercise: No",
        "exercise_True": "Physical Exercise: Yes",
        "high_bp_Borderline": "Blood Pressure: Borderline High",
        "high_bp_No": "Blood Pressure: Normal/No",
        "high_bp_Yes": "Blood Pressure: Hypertension/Yes",
    }
    return mapping.get(clean, clean)


def build_form_inputs(cat_values_json: json) -> dict:
    inputs = {}

    numeric_cols = [
        "age",
        "height",
        "weight",
        "income",
        "gen_health",
        "physical_health_days",
        "mental_health_days",
        "l_checkup"
    ]
    binary_cols = [
        "smoked_100_cigarettes",
        "drinks_alcohol",
        "had_coronary_heart_disease",
        "cost_barrier",
        "had_stroke",
        "had_heart_attack",
        "has_personal_doctor",
    ]
    categorical_cols = ["sex", "marital_status", "employment_status", "exercise", "high_bp", "socioeconomic_tier"]

    for cat in numeric_cols:
        values = cat_values_json.get(cat)
        if len(values)==0:
            continue
        low = values[0] # the first value is the lower limit
        high = values[1] # the second value is the upper limit
        default = (values[0] + values[1]) // 2 # set default as the mean of upper and lower limits
        inputs[cat] = st.number_input(
            cat.replace("_", " ").title(),
            min_value=low,
            max_value=high,
            value=default,
            step=1,
        )

    for cat in binary_cols:
        values = cat_values_json.get(cat)
        if len(values)==0:
            continue
        default = "No"
        inputs[cat] = st.radio(
            cat.replace("_", " ").title(),
            ["No", "Yes"],
            index=0,
            horizontal=True,
        )

    for cat in categorical_cols:
        values = cat_values_json.get(cat)
        if len(values) != 0:
            default = values[0]
            inputs[cat] = st.selectbox(
                cat.replace("_", " ").title(),
                values,
                index=values.index(default) if default in values else 0,
            )
    return inputs


def build_input_frame(user_inputs: dict) -> pd.DataFrame:
    input_df = pd.DataFrame([user_inputs])
    input_df["bmi"] = input_df["weight"] / ((input_df["height"] / 100) ** 2)
    input_df["age"] = input_df["age"].apply(map_age)
    input_df["education"] = input_df["education"].apply(map_education)
    input_df["socioeconomic_tier"] = input_df["socioeconomic_tier"].apply(map_socioeconomic_tier)

    for col in [
        "smoked_100_cigarettes",
        "exercise",
        "drinks_alcohol",
        "had_coronary_heart_disease",
        "cost_barrier",
        "l_checkup",
        "had_stroke",
        "had_heart_attack",
        "has_personal_doctor",
    ]:
        input_df[col] = input_df[col].apply(lambda value: 1 if str(value).lower() in {"yes", "true", "1"} else 0)

    input_df = input_df.drop(columns=["height", "weight"])
    return input_df


def explain_prediction(model, explainer, input_df: pd.DataFrame):
    preprocessor = model.named_steps["preprocessor"]
    input_processed = preprocessor.transform(input_df)
    shap_values = explainer.shap_values(input_processed)

    if isinstance(shap_values, list):
        sv = shap_values[1]
    else:
        sv = shap_values

    feature_names = preprocessor.get_feature_names_out()
    cleaned_feature_names = np.array([clean_feature_name(name) for name in feature_names])

    shap_df = pd.DataFrame({
        "feature": cleaned_feature_names,
        "shap_value": sv[0],
    }).sort_values("shap_value", key=np.abs, ascending=False)

    shap_explanation = shap.Explanation(
        values=sv[0],
        base_values=explainer.expected_value,
        data=input_processed[0],
        feature_names=cleaned_feature_names,
    )

    return shap_df, shap_explanation


st.set_page_config(page_title="Diabetes Risk Predictor", layout="wide")
st.title("Diabetes Risk Predictor")
st.write("This app mirrors the notebook workflow and uses the trained model plus SHAP explanations.")

st.session_state.setdefault("sample", False)
model, explainer, cat_values_json = load_assets()
# training_df['socioeconomic_tier'] = np.random.randint(1,4, len(training_df))

with st.sidebar:
    st.header("Patient details")
    if st.button("Use sample values"):
        st.session_state["sample"] = True

    if st.session_state.get("sample"):
        user_inputs = {
            "age": 52,
            "height": 175,
            "weight": 80,
            "education": "None or KG",
            "income": 8,
            "gen_health": 4,
            "physical_health_days": 5,
            "mental_health_days": 3,
            "smoked_100_cigarettes": 1,
            "drinks_alcohol": 1,
            "had_coronary_heart_disease": 0,
            "cost_barrier": 0,
            "l_checkup": 1,
            "had_stroke": 0,
            "had_heart_attack": 0,
            "has_personal_doctor": 1,
            "sex": "Male",
            "marital_status": "Married/Cohabiting",
            "employment_status": "Employed",
            "exercise": "False",
            "high_bp": "No",
            "socioeconomic_tier": 1,
        }
    else:
        user_inputs = build_form_inputs(cat_values_json)

    # Keep the app responsive and aligned with the notebook input schema.
    user_inputs = {k: user_inputs.get(k, None) for k in FEATURE_FIELDS}

    with st.expander("Data-driven value ranges and categories"):
        numeric_summary = []
        for col in ["age", "height", "weight", "income", "gen_health", "physical_health_days", "mental_health_days"]:
            values = cat_values_json.get(col)
            print(values)
            if len(values)!=0:
                numeric_summary.append(f"{col}: {values[0]:.0f} to {values[1]:.0f}")
        st.write("Numeric ranges")
        st.write("\n".join(numeric_summary))
        st.write("")
        st.write("Categorical values")
        for col in ["sex", "marital_status", "employment_status", "exercise", "high_bp", "socioeconomic_tier"]:
            values = [str(v) for v in cat_values_json[col] if str(v) != "nan"]
            st.write(f"- {col.replace('_', ' ').title()}: {', '.join(values)}")

    if st.button("Predict"):
        input_df = build_input_frame(user_inputs)
        prediction = model.predict(input_df)
        proba = model.predict_proba(input_df)
        prob_diabetic = float(proba[0][1])
        predicted_class = "Diabetic" if prediction[0] == 1 else "Non-diabetic"

        shap_df, shap_explanation = explain_prediction(model, explainer, input_df)

        st.session_state["prediction_result"] = {
            "predicted_class": predicted_class,
            "prob_diabetic": prob_diabetic,
            "shap_df": shap_df,
            "shap_explanation": shap_explanation,
            "base_value": float(explainer.expected_value),
        }

if "prediction_result" in st.session_state:
    result = st.session_state["prediction_result"]
    st.subheader("Prediction")
    st.metric("Predicted class", result["predicted_class"])
    st.metric("Risk probability", f"{result['prob_diabetic']:.2%}")
    st.metric("Base value", f"{result['base_value']:.4f}")

    st.subheader("Top SHAP contributors")
    st.dataframe(result["shap_df"].head(10), use_container_width=True)

    st.subheader("SHAP Bar Plot")
    plt.figure(figsize=(10,5))
    shap_df = st.session_state["prediction_result"]["shap_df"]
    shap_df["abs_shap"] = np.abs(shap_df["shap_value"])
    top_10 = shap_df.sort_values(by="abs_shap").tail(10)
    plt.barh(width=top_10.shap_value, y=top_10.feature)
    st.pyplot(plt.gcf())

    st.subheader("SHAP waterfall")
    plt.figure(figsize=(10, 5))
    shap.plots.waterfall(result["shap_explanation"], max_display=10, show=False)
    st.pyplot(plt.gcf())
else:
    st.info("Use the sidebar to enter values and click Predict.")
