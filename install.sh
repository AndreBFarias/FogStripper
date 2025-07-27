#!/bin/bash


pip install -r requirements.txt


mkdir -p ~/.local/share/desnudador_nevoas


cp -r * ~/.local/share/desnudador_nevoas


mkdir -p ~/.local/share/icons/hicolor/128x128/apps
cp desnundador.png ~/.local/share/icons/hicolor/128x128/apps/desnudador.png


cat > ~/.local/share/desnudador_nevoas/desnudador_nevoas.sh << EOL
#!/bin/bash
cd ~/.local/share/desnudador_nevoas
python3 main.py
EOL


chmod +x ~/.local/share/desnudador_nevoas/desnudador_nevoas.sh


cat > ~/.local/share/applications/desnudador_nevoas.desktop << EOL
[Desktop Entry]
Name=Desnudador de Névoas
Exec=~/.local/share/desnudador_nevoas/desnudador_nevoas.sh
Icon=desnundador
Type=Application
Categories=Utility;
EOL

echo "Instalação concluída! Procure 'Desnudador de Névoas' no menu de aplicativos."
