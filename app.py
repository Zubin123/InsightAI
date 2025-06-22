import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from src.utils.mongodb_ops import get_all_labels, upsert_cluster_label

# Load env variables
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
collection = db.ticket_summaries

st.set_page_config(page_title="InsightAI Explorer", layout="wide")
st.title("📊 InsightAI: Ticket Summary Explorer")

# Load cluster labels
cluster_labels = get_all_labels()

# Sidebar filters
st.sidebar.header("🔍 Filter Tickets")
all_clusters = sorted(collection.distinct("cluster"))
selected_clusters = st.sidebar.multiselect("Select Clusters", all_clusters, default=all_clusters)

query = {"cluster": {"$in": selected_clusters}}

search_term = st.sidebar.text_input("Search Summary/Content")
if search_term:
    query["$or"] = [
        {"summary": {"$regex": search_term, "$options": "i"}},
        {"pii_masked_content": {"$regex": search_term, "$options": "i"}}
    ]

# Load filtered data
docs = list(collection.find(query))
df = pd.DataFrame(docs)

if df.empty:
    st.warning("No tickets found for the selected filters.")
    st.stop()

# Apply cluster label mapping
df["cluster_label"] = df["cluster"].map(cluster_labels).fillna("Unlabeled")

# UMAP Scatter
fig = px.scatter(df, x="umap_x", y="umap_y", color=df["cluster_label"].astype(str),
                 hover_data=["ticket_id", "summary"], title="UMAP Projection by Cluster")
st.plotly_chart(fig, use_container_width=True)

# Ticket Table
st.subheader("📄 Filtered Tickets")
st.dataframe(df[["ticket_id", "cluster","cluster_label", "summary", "pii_masked_content"]], use_container_width=True)

# Ticket Detail
selected_ticket = st.selectbox("📌 View Ticket Details", df["ticket_id"].tolist())
ticket = df[df["ticket_id"] == selected_ticket].iloc[0]

st.markdown(f"""
**🆔 Ticket ID:** `{ticket['ticket_id']}`  
**🗂️ Cluster:** `{ticket['cluster']}`  
**🧠 Summary:** {ticket['summary']}  
**🔒 PII Masked Content:** {ticket['pii_masked_content']}  
**📩 Original Content:**{ticket['content']}""")

st.sidebar.markdown("---")
st.sidebar.header("🏷️ Label Clusters")

for cid in sorted(df["cluster"].unique()):
    default = cluster_labels.get(cid, "")
    new_label = st.sidebar.text_input(f"Cluster {cid}:", value=default, key=f"label_{cid}")
    if new_label and new_label != default:
        upsert_cluster_label(cid, new_label)
        st.sidebar.success(f"Label for cluster {cid} saved: {new_label}")

