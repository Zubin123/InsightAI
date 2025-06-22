# 🧠 InsightAI – GenAI-Powered Enterprise Ticket Analyzer

InsightAI is an end-to-end, production-grade AI system designed to process, cluster, summarize, and visualize enterprise tickets using state-of-the-art NLP and clustering techniques. It enables teams to gain operational insights from unstructured support data (e.g., emails, chat logs, tickets).

---

## 🚀 Features

- ✅ Real-world ticket data simulation using synthetic text generator
- 🧹 Preprocessing + PII masking using spaCy NER
- 📊 Unsupervised clustering using UMAP → SOM → HDBSCAN
- 📌 GenAI-based summarization of ticket content (MiniLM + Transformers)
- 🍃 MongoDB integration to persist ticket insights (summary, cluster, embedding)
- 🖼️ UMAP scatter plots for cluster exploration (Plotly)
- 🧾 Streamlit UI to filter tickets by cluster, search, and inspect details
- 🏷️ Cluster labeling interface to assign human-readable tags to clusters

---

## 🏗️ Project Structure
insightai/
├── app.py # Streamlit UI
├── .env # Environment variables (Mongo URI)
├── requirements.txt
├── data/
│ └── summarized_tickets.csv # Final processed ticket dataset
├── notebooks/
│ ├── 1_generate_dataset.ipynb
│ ├── 2_clustering.ipynb
│ ├── 3_ner_masking.ipynb
│ └── 4_summarization.ipynb
├── src/
│ └── utils/
│ └── mongodb_ops.py # MongoDB read/write helper functions


---

## 🧰 Tech Stack

| Category       | Tools/Frameworks                                      |
|----------------|--------------------------------------------------------|
| Language       | Python                                                |
| NLP            | SpaCy, Transformers (MiniLM), Hugging Face            |
| Clustering     | UMAP, HDBSCAN, Self-Organizing Maps (SOM)             |
| Summarization  | Sentence Transformers                                 |
| Database       | MongoDB (Local or Atlas)                              |
| Visualization  | Streamlit, Plotly                                     |
| Dev Tools      | Git, dotenv                                           |

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Zubin123/InsightAI.git
   cd InsightAI
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Configure .env**
   ```bash
   MONGO_URI=mongodb://localhost:27017
   MONGO_DB=insightai

4. **Run Streamlit App**
   ```bash
   streamlit run app.py
   
## 🧪 Notebooks Overview
| Notebook                   | Purpose                                    |
| -------------------------- | ------------------------------------------ |
| `1_generate_dataset.ipynb` | Generate or ingest ticket data             |
| `2_clustering.ipynb`       | Embed + cluster using UMAP → SOM → HDBSCAN |
| `3_ner_masking.ipynb`      | Detect and mask PII using spaCy            |
| `4_summarization.ipynb`    | Summarize masked content using MiniLM      |

## 🗂️ MongoDB Collections

- ticket_summaries: All ticket metadata (summary, cluster, UMAP coords)
- cluster_labels: Human-assigned labels for each cluster ID

## 🙌 Acknowledgements

- Hugging Face Transformers
- SentenceTransformers
- spaCy
- Streamlit
- MongoDB
## Built by 
**Mohammed Zubin Essudeen**
