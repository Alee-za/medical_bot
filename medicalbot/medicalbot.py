import pandas as pd
from difflib import get_close_matches
import streamlit as st


def load_rules_from_excel(file_path):
    """
    Load diagnosis rules from an Excel file.

    Args:
        file_path (str): Path to the Excel file containing rules.

    Returns:
        dict: A dictionary where keys are tuples of symptoms, and values are diagnoses.
    """
    df = pd.read_excel(r"C:\Users\USER\OneDrive\Desktop\medicalbot_rules.xlsx")
    rules = {}
    for _, row in df.iterrows():
        symptoms = tuple(row['Symptoms'].split(","))
        diagnosis = row['Diagnosis']
        rules[symptoms] = diagnosis
    return rules


def get_diagnosis(symptoms, rules):
    """
    Matches user-provided symptoms with predefined rules to return a diagnosis.
    Handles minor spelling and spacing errors.

    Args:
        symptoms (list): A list of symptoms provided by the user.
        rules (dict): A dictionary of rules loaded from an Excel file.

    Returns:
        str: Diagnosis based on the symptoms.
    """
    # Flatten the rules to get all symptoms
    all_possible_symptoms = set(symptom for rule in rules for symptom in rule)

    # Correct user symptoms using fuzzy matching
    corrected_symptoms = []
    for symptom in symptoms:
        match = get_close_matches(symptom, all_possible_symptoms, n=1, cutoff=0.8)
        corrected_symptoms.append(match[0] if match else symptom)

    # Match exact symptoms or provide probability for partial matches
    diagnosis_probabilities = {}
    for rule, diagnosis in rules.items():
        match_count = sum(1 for symptom in rule if symptom in corrected_symptoms)
        if match_count == len(rule):
            return diagnosis
        elif match_count > 0:
            probability = (match_count / len(rule)) * 100
            diagnosis_probabilities[diagnosis] = probability

    if diagnosis_probabilities:
        return "Partial Matches: " + ", ".join(
            [f"{diagnosis} ({prob:.1f}%)" for diagnosis, prob in diagnosis_probabilities.items()]
        )

    return "Unknown"


# Streamlit User Interface
if __name__ == "__main__":
    st.title("Medical Diagnosis Expert System")
    st.write("I can help you diagnose common conditions based on your symptoms.")
    st.write("Please type your symptoms separated by commas.")

    file_path = "rules.xlsx"  # Path to the Excel file containing the rules
    try:
        rules = load_rules_from_excel(file_path)

        symptoms_input = st.text_input("Enter your symptoms, separated by commas:")
        if st.button("Diagnose"):
            if symptoms_input:
                user_symptoms = [symptom.strip().lower() for symptom in symptoms_input.split(",")]
                diagnosis = get_diagnosis(user_symptoms, rules)
                st.write(f"**Diagnosis:** {diagnosis}")

                more_input = st.radio("Would you like to enter more symptoms?", ("Yes", "No"))
                if more_input == "No":
                    st.write("Thank you for using the Medical Diagnosis Expert System. Stay healthy!")

    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
