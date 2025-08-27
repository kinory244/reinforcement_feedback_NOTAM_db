# 🛫 Synthetic NOTAM Reinforcing Pipeline

Applicazione **Streamlit** per raccogliere feedback operativi da piloti su NOTAM sintetici.  
Ogni utente lavora su una copia personalizzata del dataset e i risultati vengono salvati in locale (file CSV individuale).  
Al termine, ciascun pilota potrà inviarti il proprio file CSV per la raccolta finale.

---

## ✨ Funzionalità principali
- **Accesso protetto** → l’app richiede una password iniziale (`st.secrets["APP_PASSWORD"]`).
- **Database congelato** → i NOTAM vengono scaricati da un file su Google Drive (solo lettura).
- **Sessione personale** → ogni pilota inserisce il proprio username → si crea un file CSV dedicato (`feedback_<username>.csv`).
- **Progress tracking** → l’utente può chiudere l’app e riprendere in seguito dallo stesso punto.
- **Feedback guidato**:
  - Correttezza stile ICAO  
  - Correttezza categoria (con eventuale correzione)  
  - Realismo operativo  
  - Impatto percepito (medico, tecnico, atterraggio immediato)  
  - Note libere

---

## 📂 Output
- Per ogni utente viene creato e aggiornato un file locale:  

---

📖 Istruzioni per i piloti

- Apri il link dell’app fornito dall’amministratore.
- Inserisci la password di accesso.
- Inserisci il tuo username (solo minuscole, senza spazi).
- Compila i feedback per i NOTAM presentati.
- Usa Previous / Next per navigare.
- Usa Save Feedback per salvare il progresso.
- Usa Exit for today per uscire e riprendere in seguito.
- Quando avrai completato tutti i NOTAM, vedrai un messaggio di conferma ✅.
- A quel punto invia il file generato (feedback_<username>.csv) all’amministratore.
