FogStripper - Desnudador é uma aplicação gráfica para remoção de fundos de imagens utilizando modelo neural local, baseada no modelo U2Net e acelerada por GPU via CUDA. Esta ferramenta é open source e projetada para usuários que buscam eficiência e privacidade em processamento de imagens.


#### Pré-requisitos

- Python 3.8 ou superior.
- Placa de vídeo NVIDIA com suporte a CUDA para aceleração (recomendado para desempenho otimizado).
- Modelo U2Net (u2net.onnx).

#### Instalação



```
# Clone o repositório:
git clone https://github.com/seuusuario/FogStripperAI.git
cd FogStripperAI
# Crie um ambiente virtual e instale as dependências:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Execute a aplicação:
python main.py 
```

#### Uso
- Arraste e solte imagens na janela ou selecione arquivos via botão "Selecione Imagens".
- Ajuste a potência da GPU utilizando o slider para otimizar o processamento.
- A imagem processada é salva automaticamente com o sufixo _despido.png, e uma mensagem de confirmação permite visualizar a pasta de saída.

##### Dependências
As principais bibliotecas utilizadas incluem:

- PyQt6 para a interface gráfica.
- rembg[gpu] para remoção de fundos com suporte a GPU.
- Pillow para manipulação de imagens.

###### Licença
Esta aplicação é distribuída sob licença open source, permitindo uso, modificação e distribuição livre.FogStripper é uma aplicação gráfica para remoção de fundos de imagens utilizando modelo neural local, baseada no modelo U2Net e acelerada por GPU via CUDA. Esta ferramenta é open source e projetada para usuários que buscam eficiência e privacidade em processamento de imagens.
