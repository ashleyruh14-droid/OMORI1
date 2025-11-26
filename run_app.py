import os
import sys
from streamlit.web import cli as stcli

def main():
    # Aller dans le dossier où se trouve run_app.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    # exécution équivalente à : streamlit run app.py --server.port 8501
    sys.argv = ["streamlit", "run", "app.py", "--server.port", "8501"]

    # Lance Streamlit SANS créer d'autre processus → impossible de boucler
    stcli.main()

if __name__ == "__main__":
    main()
