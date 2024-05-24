# Šablona

Tento repozitář je šablonou pro Flask aplikaci s vizualizacemi pomocí Plotly.

## Použité technologie
- Flask
- Plotly
- Jinja2
- Pandas

## Struktura repozitáře

├── app
│ ├── data
│ │ ├── zpracovani.py # Skripty pro zpracování dat
│ │ └── kraje
│ │ └── info.txt # Informace o regionech
│ ├── grafy
│ │ └── grafy.py # Funkce pro vizualizaci grafů
│ ├── templates
│ │ ├── index.html # Šablona hlavní stránky
│ │ ├── graf.html # Šablona stránky s grafem
│ │ └── template.html # Základní šablona
│ └── main.py # Hlavní soubor aplikace
├── .gitignore # Soubory a adresáře ignorované gitem
├── DockerFile # Konfigurace Dockeru
├── docker-compose.yml # Konfigurace Docker Compose
├── requirements.txt # Python závislosti
├── LICENSE # Informace o licenci
└── activate.sh # Skript pro aktivaci virtuálního prostředí



## Instrukce k nastavení

1. **Klonování repozitáře:**
```sh
git clone https://github.com/matav5/template.git
cd template
```
2. **Vytvoření a aktivace virtuálního prostředí:**

```sh
python -m venv .venv
source .venv/bin/activate 
Na Windows použijte: .venv\Scripts\activate
```

3. **Instalace závislostí:**
```sh
pip install -r requirements.txt
```
4. **Spuštění aplikace (doporučuju Docker):**

```sh
python app/main.py
```
5. **Použití Dockeru:**
```sh
docker-compose up
```
## Použití

- Přístup na hlavní stránku na `http://localhost:5000/`
- Přístup na stránku s grafem na `http://localhost:5000/graf`


## Odkazy
Jenom třeba něco co by se mohl ohodit
- [Vytvoření prvního dashboardu s Superset](https://superset.apache.org/docs/using-superset/creating-your-first-dashboard/)
- [MongoDB Compass](https://www.mongodb.com/try/download/compass)