Questa ramificazione del progetto di costruzione del DB nasce affinché, parallelamente al setup di quest'ultimo, e con scale temporali anche più diradate, si possa iniziare un reinforcement loop tramite parere umano esperto sui dati che sto generando artificiosamente. Credo quindi che la soluzione migliore sia predisporre uno strumento che sia sempre utilizzabile dai piloti, a distanza, e con workload minimo, perché questi possano contribuire a una seconda versione del dataset. Diciamo che la prima versione sarà quella che costruirò con zero supporto. Con la seconda versione, avremo dei "reward" calcolati su ogni riga del csv files. Questi reward pensiamoli come punteggi che sono computati a partire dai giudizi dati sul NOTAM rispetto a credibilità, affinità col reale. 

Quindi l'app Streamlit consente di:
- determinare quanto un pilota ci dà il check sul NOTAM
- consentirgli contestualmente di cambiare la category dove lo ritiene opportuno e cambiare gli score di rilevanza per HAWKEYE

Potenzialmente il file:

notam_db_extract.csv 

corrisponde all'intero DB.


- Inserire logica all'interno di APP tale per cui:
Ciascun pilota abbia accesso a una fetta del DB, complementare a quella dell'altro pilota. 