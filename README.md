# GS-IOT
# ⚠️ Alerta Climático em Situações de Apagão

## 🌍 Problema

Em muitas regiões, eventos climáticos extremos como enchentes, deslizamentos e tempestades severas frequentemente causam **interrupções no fornecimento de energia elétrica**. Nessas situações, a comunicação e o pedido de ajuda se tornam extremamente difíceis — especialmente em locais escuros ou de difícil acesso.

## 💡 Solução Proposta

Desenvolvemos um sistema inteligente que utiliza **Python e MediaPipe** para **reconhecer gestos corporais específicos** em ambientes com pouca ou nenhuma iluminação, possibilitando o envio de **alertas de emergência** ou o acionamento de **sinais visuais/sonoros**.

Este sistema pode ser útil para:
- Pessoas presas em locais alagados.
- Idosos ou pessoas com deficiência visual durante um apagão.
- Equipes de resgate que precisam detectar movimento em áreas de risco.

## 🛠️ Tecnologias Utilizadas

- Python 3.8+
- [MediaPipe](https://google.github.io/mediapipe/)
- OpenCV

## 📹 Demonstração

👉 [Clique aqui para ver o vídeo demonstrativo](https://youtu.be/SEU-LINK-AQUI) *(até 3 minutos)*

O vídeo apresenta:
- A motivação e importância da solução.
- Como o sistema funciona.
- Simulação prática com reconhecimento de gestos.
  
## 🧠 Funcionamento

1. O sistema utiliza uma câmera comum para captar imagens em tempo real (ou vídeos simulados).
2. A biblioteca MediaPipe identifica **pontos de referência do corpo**.
3. Se for detectado um gesto de socorro (ex: mão levantada acima da cabeça por mais de 2 segundos), o sistema:
   - Emite um alerta no console ou aciona uma resposta (pode ser uma luz, som, ou envio de sinal para outro sistema).
4. Pode funcionar mesmo com **baixa iluminação**, pois MediaPipe detecta padrões estruturais.

## 🧪 Exemplos de Comandos

```bash
# Instale as dependências
pip install mediapipe opencv-python

# Execute o script principal
python alerta_climatico.py
