# Projekt vorbereiten
prepare: create_virtualenv install_requirements
	@echo "Projekt ist jetzt bereit! Du kannst das Notebook ausführen."

# Virtuelle Python-Umgebung erstellen und aktivieren
create_virtualenv:
	@echo "Erstelle virtuelle Python-Umgebung..."
	python3 -m venv venv
	@echo "Aktiviere virtuelle Python-Umgebung..."
	@if [ "$(OS)" = "Windows_NT" ]; then \
		call venv\\Scripts\\activate; \
	elif [ "$(shell uname)" = "Darwin" ] || [ "$(shell uname)" = "Linux" ]; then \
		. venv/bin/activate; \
	else \
		echo "Unbekanntes Betriebssystem, keine Aktivierung der virtuellen Umgebung möglich."; \
	fi
	@echo "Virtuelle Python-Umgebung erstellt und aktiviert!"

# Installieren der Abhängigkeiten aus requirements.txt
install_requirements:
	@echo "Installiere Abhängigkeiten aus requirements.txt..."
	pip install -r requirements.txt
	@echo "Abhängigkeiten installiert!"