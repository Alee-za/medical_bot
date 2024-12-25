# Medical Diagnosis Expert System

This project is a **Medical Diagnosis Expert System** built using Python and Streamlit. It allows users to input symptoms and receive a potential diagnosis based on predefined rules stored in an Excel file. The system can handle minor spelling and spacing errors in the symptoms provided.

---

# Features
- **Symptom Matching**: Matches user symptoms against a set of predefined rules.
- **Fuzzy Matching**: Corrects minor spelling and spacing errors in user input.
- **Partial Matches**: Provides a probability-based diagnosis for partial symptom matches.
- **Web-Based Interface**: User-friendly interface powered by Streamlit.

---

## Requirements

To run this project, install the following Python libraries:

- `pandas`
- `openpyxl`
- `streamlit`

Install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

---

## File Structure

- **`medicalbot.py`**: Main application file containing the code for the diagnosis system and Streamlit interface.
- **`rules.xlsx`**: Excel file containing predefined diagnosis rules (Symptoms and Diagnosis columns).
- **`requirements.txt`**: File containing the list of dependencies.

---

## How to Run

1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd medical_bot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run medicalbot.py
   ```
5. Open the URL displayed in the terminal (usually `http://localhost:8501/`) in your web browser.

---

## Usage

1. Open the application in your web browser.
2. Enter your symptoms, separated by commas, in the input field.
3. Click the "Diagnose" button to get a diagnosis.
4. If partial matches are found, probabilities for each diagnosis will be displayed.
5. Optionally, enter more symptoms for further diagnosis or exit the system.

---

## Input File Format

The `rules.xlsx` file should have the following format:

| Symptoms          | Diagnosis       |
|-------------------|-----------------|
| fever,cough       | Flu             |
| headache,nausea   | Migraine        |

- **Symptoms**: Comma-separated list of symptoms.
- **Diagnosis**: Corresponding diagnosis for the symptoms.

Ensure the file is saved in `.xlsx` format.

---

## Error Handling
- If the `rules.xlsx` file is missing or incorrectly formatted, the system will display an error message.
- Handles exceptions gracefully to guide the user on how to proceed.

---

## License
This project is open-source and available under the MIT License.

---

## Acknowledgements
- Built using [Streamlit](https://streamlit.io/) for the web interface.
- Uses [pandas](https://pandas.pydata.org/) for data processing.



