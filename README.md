# Jogo-Da-Velha
**Trabalho Cleon**

## Instruções para o Jogo:

O projeto foi construído separando a inteligência da interface gráfica, garantindo um código organizado e eficiente.

###  Estrutura de Pastas do Projeto

* **Pasta `logica/`**: Onde fica o "cérebro" do jogo, aqui está implementado o algoritmo Minimax com a Poda Alfa-Beta
* Esta pasta é responsável por calcular as jogadas perfeitas, identificar casas vazias e definir se houve um vencedor ou empate, sem se preocupar com cores ou botões.
* **Pasta `visual/`**: Onde fica toda a parte gráfica.
* Esta pasta utiliza a biblioteca `tkinter` para renderizar a janela, os botões, os textos coloridos, os mini-tabuleiros e a animação de chuva de confetes.
* **Arquivo `main.py`**: É o arquivo principal, junta a pasta `logica` com a pasta `visual` e dá a partida no jogo.

---

### Modos de Jogo

No menu inicial, você terá três opções de interação.

####  1. Jogar contra Robô
Neste modo, você (Humano) joga como **X** e a Inteligência Artificial joga como **O**. 
Ao clicar neste botão, você será levado para uma tela onde deverá **selecionar a dificuldade**:
* **Fácil (Aleatório):** O robô não usa o algoritmo. Ele apenas escolhe uma casa vazia qualquer, sendo bem fácil de derrotar.
* **Médio:** O robô fica imprevisível. Em 50% das vezes ele joga aleatoriamente, e nos outros 50% ele calcula a melhor jogada.
* **Impossível (Minimax):** A IA entra em força total. O algoritmo Minimax calcula todas as possibilidades futuras do tabuleiro. Ele bloqueia todos os seus ataques e nunca vai perder de você (no máximo, você vai conseguir arrancar um empate).

####  2. Jogar contra Amigo
Este é o modo clássico para dois jogadores humanos no mesmo computador. 
* Não há inteligência artificial aqui. Você e seu amigo dividem o mouse e clicam na tela para alternar as jogadas.
* O sistema controla automaticamente de quem é a vez (mudando de X laranja para O azul) e avisa no topo da tela. 
* Quem conseguir alinhar 3 símbolos primeiro recebe a tela de vitória com confetes.

####  3. Testar Robô 100 vezes
Esta opção é um teste automatizado para provar a robustez matemática da IA desenvolvida para o trabalho.
* O sistema cria um ambiente onde o Robô (no nível Impossível) joga automaticamente 100 partidas consecutivas contra um sistema de jogadas puramente aleatórias.
* A interface desenha 100 mini-tabuleiros em tempo real, mostrando o resultado final de cada partida.
* **A prova:** Você verá os tabuleiros ficarem **Verdes (Robô venceu)** ou **Azuis (Empate)**. Como a IA é invencível, nenhum quadrado ficará **Vermelho (Derrota)**.
