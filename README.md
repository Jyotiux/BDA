
# Stress Detection from Social Media Posts

## 🧠 Objective

To build a **scalable machine learning pipeline** using Apache Spark to detect stress in social media messages. This system integrates **ensemble models** like Hard Voting and Stacking to boost classification accuracy and leverages **transformer-based deep learning models** for improved results.

---

## 🚀 Technologies Used

- **Apache Spark (PySpark)** – For scalable data processing and model training
- **Spark MLlib** – For ML models and pipeline components
- **Streamlit** – For simple user interface to input messages
- **HDFS (Hadoop Distributed File System)** – For distributed data storage
- **Python** – Development language

---

## 📦 Project Structure

```

📁 stress-detection-spark/
├── models.py                # Spark ML pipeline, training, evaluation
├── input.py                 # Streamlit UI for message input
├── output\_messages.csv      # New user-entered messages (Streamlit)
├── dreaddit\_StressAnalysis.csv # Training data (stored on HDFS)
├── README.md                # Project documentation

````

---

## 📥 Data Flow

1. **Input**:
   - New messages via `Streamlit` UI → saved to `output_messages.csv`
   - Training dataset (`dreaddit_StressAnalysis.csv`) stored on HDFS

2. **Preprocessing**:
   - Label cleaning and integer conversion
   - Tokenization → TF → IDF
   - Train/Test Split (80/20)

3. **Model Training** (`models.py`):
   - Trains base models: Decision Tree, GBT, SVM, Logistic Regression
   - Hard Voting: Combines model predictions via majority vote
   - Stacking: Uses meta-model (Logistic Regression) on base outputs

4. **Evaluation**:
   - Metrics: Accuracy, F1-score, Precision, Recall, AUC-ROC

5. **Prediction**:
   - Reads new messages → Applies preprocessing → Outputs results

---

## ⚙️ Running the Application

### 1. Launch Streamlit Input UI

```bash
streamlit run input.py
````

* Enter text messages
* Data gets saved to `output_messages.csv`

### 2. Train & Run Models (on Spark)

```bash
spark-submit models.py
```

* Loads training data from HDFS
* Trains base and ensemble models
* Applies predictions to new data in `output_messages.csv`

---

## 🤖 Models and Performance

### 🧪 Traditional ML Models

| Model                   | Accuracy | F1-score | Precision | Recall |
| ----------------------- | -------- | -------- | --------- | ------ |
| Decision Tree           | 62.62%   | 61.19%   | 64.53%    | 62.62% |
| Gradient Boosted Trees  | 59.81%   | 58.95%   | 60.54%    | 59.81% |
| SVM                     | 60.75%   | 60.44%   | 61.21%    | 60.75% |
| Logistic Regression     | 60.75%   | 60.64%   | 60.93%    | 60.75% |
| **Voting Classifier**   | 61.68%   | 60.86%   | 65.79%    | 47.17% |
| **Stacking Classifier** | 62.62%   | 62.52%   | 61.02%    | 67.92% |

### 🔍 Transformer-Based Models

| Model      | Accuracy | F1-score | Precision | Recall |
| ---------- | -------- | -------- | --------- | ------ |
| XLNet      | 78.03%   | 79.14%   | 71.43%    | 88.71% |
| BERT       | 83.33%   | 83.82%   | 85.07%    | 82.61% |
| DistilBERT | 76.52%   | 76.69%   | 71.83%    | 82.26% |
| RoBERTa    | 82.58%   | 82.96%   | 76.71%    | 90.32% |
| Electra    | 66.67%   | 69.86%   | 60.71%    | 82.26% |

---

## ✅ Output Example

```
Text: I can't take this anymore
Prediction: Stressed
ALERT: The text is classified as 'Stressed'!
```

---

## 🌟 Key Features

* ✔️ **Scalable** ML pipeline using Spark
* ✔️ **Ensemble Learning** for robust prediction
* ✔️ **Streamlit UI** for easy data entry
* ✔️ Real-time prediction alerts

---

## 🔮 Future Enhancements

* Integrate **TensorFlow on Spark** for scalable deep learning
* Enable **real-time streaming** via Spark Streaming
* Add **dashboards** for visualizing stress trends

---

## 🛠️ Deployment Notes

* Models can be saved in **HDFS** or local filesystem
* Streamlit app runs independently from Spark pipeline
* Use `cron` or `airflow` to schedule periodic predictions


