# 🛫 Synthetic NOTAM Reinforcing Pipeline

Applicazione **Streamlit** per raccogliere feedback operativi da piloti su NOTAM sintetici.  
Ogni utente lavora su una copia personalizzata del dataset e i risultati vengono salvati automaticamente sia in locale (su Streamlit Cloud) sia in **Google Drive** (CSV individuali).

---

## ✨ Funzionalità principali
- **Autenticazione**: accesso protetto da password (`st.secrets["APP_PASSWORD"]`).
- **Database congelato**: i NOTAM vengono caricati da un file su Google Drive (versione di riferimento).
- **Progress tracking**: ogni pilota può uscire e riprendere da dove aveva lasciato.
- **Feedback guidato**:
  - Correttezza stile ICAO
  - Correttezza categoria
  - Realismo operativo
  - Impatto percepito (medico, tecnico, atterraggio immediato)
  - Note libere
- **Upload automatico su Google Drive**: ogni salvataggio aggiorna il CSV dell’utente in una cartella condivisa.

---

## 🚀 Deploy su Streamlit Cloud
1. Fork/Clona la repo su GitHub.
2. Deploya su [Streamlit Cloud](https://share.streamlit.io).
3. Configura i secrets:
   ```toml
   APP_PASSWORD = "super_password_segreta"
   DB_URL = "https://drive.google.com/uc?id=YOUR_FILE_ID"
   GDRIVE_CREDENTIALS = """
   { ...contenuto JSON del Service Account... }
   """
   GDRIVE_FOLDER_ID = "ID_DELLA_CARTELLA_SU_DRIVE"
