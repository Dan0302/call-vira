#!/bin/bash

echo "📦 Starte Server-Setup für Call-VIRA..."

# Update & Grundpakete
sudo apt update && sudo apt install -y python3 python3-pip python3-venv git

# Virtuelle Umgebung erstellen
python3 -m venv venv
source venv/bin/activate

# Abhängigkeiten installieren
pip install --upgrade pip
pip install -r requirements.txt

# .env anlegen, falls nicht vorhanden
if [ ! -f .env ]; then
  cp .env.example .env
  echo "⚠️  Bitte API-Keys in .env eintragen!"
fi

# Rechte setzen
chmod +x deploy/start_server.sh

echo "✅ Setup abgeschlossen. Starte den Server mit:"
echo "   ./deploy/start_server.sh"