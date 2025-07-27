# FogStripper 

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/AndreBFarias/FogStripper/main/assets/desnudador.png" width="400" alt="Screenshot do FogStripper">
</div>

Uma aplicação gráfica que desnuda fundos de imagens com um toque neural, baseada no modelo U2Net e acelerada por GPU via CUDA. Open source, desenhada para quem busca eficiência e privacidade em cada camada revelada.


---

## Pré-requisitos

- Python 3.8 ou superior.
- Placa de vídeo NVIDIA com suporte a CUDA (recomendado para um desempenho que seduz).
- Modelo U2Net (u2net.onnx).

## Instalação

```bash
# Clone o repositório:
git clone https://github.com/AndreBFarias/FogStripper.git
cd FogStripper
# Crie um ambiente virtual e instale as dependências:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Execute a aplicação:
python main.py 
```

### Uso
- Arraste e solte imagens na janela ou clique em "Selecione Imagens".
- Ajuste a potência da GPU com o slider, sentindo o controle pulsar.
- A imagem processada surge com o sufixo _despido.png, e uma mensagem te guia até a pasta de saída.


### Dependências
As musas deste ritual incluem:
- PyQt6 para a interface que hipnotiza.
- rembg[gpu] para remover fundos com poder bruto.
- Pillow para manipular cada curva da imagem.

### Licença
Distribuída sob licença open source, livre para uso, modificação e entrega aos desejos.