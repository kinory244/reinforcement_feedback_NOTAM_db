import json

# path al file originale scaricato da Google Cloud
with open("reinforcement-notam-db-023bdfe91077.json", "r") as f:
    creds = json.load(f)

# converte la chiave privata in una stringa con \n escapati
creds["private_key"] = creds["private_key"].replace("\n", "\\n")

# converte l'intero JSON in una stringa minificata
secrets_string = json.dumps(creds)

print("👇 Copia e incolla questa stringa in Streamlit secrets.toml:")
print()
print(f'GDRIVE_CREDENTIALS = "{secrets_string}"')
