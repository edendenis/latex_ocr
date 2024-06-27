#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar o `Tex Live` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `Tex Live` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and configurations for configuring/installing `Tex Live` on `Linux Ubuntu`._

# ### Construído com
# 
# Esta seção deve listar todas as principais estruturas/bibliotecas usadas para inicializar seu projeto, bem como a sequência de instalação. Deixe quaisquer complementos/plugins para a seção de agradecimentos. Aqui estão alguns exemplos.
# 
# * [![Texlive](https://img.shields.io/badge/Texlive-3776AB?style=flat-square&logo=latex&logoColor=white)](https://tug.org/texlive/)
# * [![JabRef](https://img.shields.io/badge/JabRef-44A833?style=flat-square&logo=latex&logoColor=white)](https://www.jabref.org/)
# * [![Texstudio](https://img.shields.io/badge/Texstudio-008080?style=flat-square&logo=latex&logoColor=white)](https://www.texstudio.org/)
# * [![MathPix](https://img.shields.io/badge/MathPix-008080?style=flat-square&logo=MathPix&logoColor=white)](https://mathpix.com/)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## Descrição [2]
# 
# ### `Tex Live`
# 
# O TeX Live é uma distribuição abrangente e amplamente utilizada do sistema de composição de documentos TeX, desenvolvido por Donald Knuth. Ele inclui uma vasta coleção de pacotes, fontes e utilitários relacionados ao TeX, tornando-o uma escolha popular entre autores e profissionais que precisam criar documentos de alta qualidade, como artigos acadêmicos, livros, relatórios técnicos e documentos matemáticos. O TeX Live está disponível em várias plataformas, incluindo Windows, macOS e Linux, e oferece suporte a uma variedade de idiomas e scripts. É uma ferramenta essencial para aqueles que desejam produzir documentos tipograficamente precisos e bem formatados.

# ## 1. Configurar/Instalar/Usar o `Tex Live` no `Linux Ubuntu` [1]
# 
# Você pode instalar o `Tex Live` no `Linux Ubuntu` usando o gerenciador de pacotes `apt`. Aqui está um guia passo a passo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.2 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.3 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.4 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.5 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.6 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.7 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 3. **Instale o `Tex Live`:** Agora você pode instalar o Tex Live executando o seguinte comando: `sudo apt install texlive-full -y`
# 
# - Isso instalará o `Tex Live` completo, que inclui uma ampla variedade de pacotes e bibliotecas para a criação de documentos LaTeX.
# 
# 4. **Verifique a instalação:** Depois que a instalação estiver concluída, você pode verificar se o `Tex Live` foi instalado corretamente executando o seguinte comando: `tex --version`
# 
# - Isso deve exibir informações sobre a versão do `Tex Live` instalada.
# 
# Agora você tem o `Tex Live` instalado no seu sistema Ubuntu e pode começar a criar documentos LaTeX. Lembre-se de usar um editor LaTeX, como o TeXworks, para criar e compilar seus documentos.
# 

# ## 1.1 Código completo para configur/instalar
# 
# Para instalar o `Tex Live` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean                                                            
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install texlive-full -y
#     tex --version
#     ```
# 

# ## Referências
# 
# [1] OPEN AI. ***Instalar o tex live no linux ubuntu.*** Disponível em: <https://chat.openai.com/c/5341e112-5d65-410b-bec5-00b9a61a6650> (texto adaptado). ChatGPT. Acessado em: 29/09/2023 18:56.
# 
# [2] OPEN AI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/11/2023 18:56.
# 
