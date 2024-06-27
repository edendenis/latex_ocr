#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `LaTeX OCR` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `LaTeX OCR` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to install/configure/use to `LaTeX OCR` on `Linux Ubuntu`._

# ## Descrição [1]
# 
# ### `LaTeX OCR`
# 
# O `LaTeX OCR` (Reconhecimento Óptico de Caracteres para LaTeX) é uma ferramenta que converte imagens de texto matemático ou científico em código `LaTeX`. Isso é particularmente útil para pesquisadores, engenheiros, cientistas e estudantes que trabalham com documentos que contêm muitas equações matemáticas e querem convertê-las para um formato digital editável sem ter que digitar manualmente o código `LaTeX`.
# 

# ## 1. Configurar/Instalar/Usar o `PyTorch` no `Linux` Ubuntu (caso NÂO tenha sido instalado) [1][2]
# 
# Para executar o modelo você precisa do `Python 3.7+`. Se você não tiver o `PyTorch` instalado. Siga as instruções abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. Você pode instalar o `PyTorch` através do conda, que pode gerenciar as versões CUDA para você: `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch -y`
# 
#     - Aqui, `cudatoolkit=11.3` é um exemplo, e você deve escolher a versão que corresponde ao seu driver CUDA ou à versão que deseja usar.
# 
#     - Se você decidir atualizar o driver da NVIDIA, após a instalação, reinicie o sistema e verifique se o CUDA está funcionando corretamente executando nvidia-smi no terminal.
# 
# 5. Para verificar novamente se o `PyTorch` pode acessar a CUDA após resolver os problemas do driver ou reinstalar uma versão compatível do `PyTorch`, você pode executar o mesmo comando Python:
# 
#     ```
#     import torch
#     print(torch.cuda.is_available())
#     ```
# 
# Espera-se que, depois de seguir esses passos, o `torch.cuda.is_available()` retorne `True`, indicando que o `PyTorch` agora pode acessar a GPU.
# 

# ## 2. Configurar/Instalar o `LaTeX OCR` no `Linux Ubuntu` (caso NÃO tenha sido instalado) [1][2]
# 
# Para instalar o `LaTeX OCR`. Siga as instruções abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. Instale o pacote `pix2tex`: `pip install "pix2tex[gui]"`
# 
#     Os pontos de verificação do modelo serão baixados automaticamente.
#     
# 4. Instale o pacote `xclip`, digite o comando: `sudo apt install xclip -y`
# 
# 5. Instale o pacote `wl-clipboard`: `sudo apt install wl-clipboard -y`
# 
#     Os pontos de verificação do modelo serão baixados automaticamente.
# 

# 6. Existem três maneiras de obter uma previsão de uma imagem.
# 
#     6.1 Você pode usar a ferramenta de linha de comando chamando `pix2tex`. Aqui você pode analisar imagens já existentes no disco e imagens na sua área de transferência ou executar o comando: `pix2tex </caminho/para/sua/imagem>.png`
# 
#     6.2 Graças a `@katie-lim`, você pode usar uma interface de usuário agradável como uma maneira rápida de obter a previsão do modelo. Basta chamar a GUI com `latexocr`. A partir daqui você pode fazer uma captura de tela e o código de latex previsto é renderizado usando MathJax e copiado para sua área de transferência.
# 
# - No Linux, é possível usar a GUI `gnome-screenshot` (que vem com suporte para vários monitores) se `gnome-screenshot` tiver sido instalada anteriormente. Para Wayland, `grim` e `slurp` será usado quando ambos estiverem disponíveis. Observe que `gnome-screenshot` não é compatível com compositores Wayland baseados em wlroots. Como `gnome-screenshot` será preferido quando disponível, talvez seja necessário definir a variável de ambiente `SCREENSHOT_TOOL` como `grim` neste caso (outros valores disponíveis são `gnome-screenshot` e `pil`).
# 
# - Se o modelo não tiver certeza sobre o que está na imagem, ele poderá gerar uma previsão diferente toda vez que você clicar em "Tentar novamente". Com o parâmetro `temperature` você pode controlar esse comportamento (baixa temperatura produzirá o mesmo resultado).
# 

# 6.3 Você pode usar uma API. Isso tem dependências adicionais. Instale `pip install -U "pix2tex[api]"` e execute: `python -m pix2tex.api.run`
# 
# Para iniciar uma demonstração Streamlit que se conecta à API na porta 8502. Há também uma imagem docker disponível para a API: https://hub.docker.com/r/lukasblecher/pix2tex Tamanho da imagem Docker (mais recente por data)
# 
# ```
# docker pull lukasblecher/pix2tex:api
# docker run --rm -p 8502:8502 lukasblecher/pix2tex:api
# ```
# 
# Para executar também a demonstração `streamlit`, execute `docker run --rm -it -p 8501:8501 --entrypoint python lukasblecher/pix2tex:api pix2tex/api/run.py` e navegue até <http://localhost:8501/>
# 

# 6.4 Use de dentro do `Python`:
# 
# Para usar dentro do `Python`, utilize os comandos abaixo:
# 
# ```
# from PIL import Image
# from pix2tex.cli import LatexOCR
# 
# img = Image.open('path/to/image.png')
# model = LatexOCR()
# print(model(img))
# ```
# 
# O modelo funciona melhor com imagens de resolução menor. É por isso que adicionei uma etapa de pré-processamento onde outra rede neural prevê a resolução ideal da imagem de entrada. Este modelo redimensionará automaticamente a imagem personalizada para melhor se assemelhar aos dados de treinamento e, assim, aumentar o desempenho das imagens encontradas em estado selvagem. Ainda assim, não é perfeito e pode não ser capaz de lidar com imagens enormes de maneira ideal, portanto, não aumente o zoom antes de tirar uma foto.
# 
# Sempre verifique o resultado com cuidado. Você pode tentar refazer a previsão com outra resolução se a resposta estiver errada.
# 

# ## 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `LaTeX OCR` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```

# ## Referências
# 
# [1]BLECHER, L.. ***Latex-ocr.*** Disponível em: <https://github.com/lukas-blecher/LaTeX-OCR/blob/main/README.md>. Acessado em: 08/11/2023 08:41.
# 
# [2] OPENAI. ***Instalar pytorch no ubuntu.*** Disponível em: <https://chat.openai.com/c/d24a5115-c7f9-48e1-9c40-f243bc017c08> (texto adaptado). Acessado em: 08/11/2023 08:49.
# 
