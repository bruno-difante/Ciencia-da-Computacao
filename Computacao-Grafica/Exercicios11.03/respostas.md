
---

## EX11)

**Pergunta:** Ao pressionar as teclas de movimento, o que acontece com os dois triângulos? Por que eles se movem em sincronia?

**Resposta:**
Ao utilizar os comandos de translação, nota-se que ambos os triângulos realizam o deslocamento de forma **agrupada**. Esse fenômeno ocorre porque a instrução `glTranslatef(x, y, -6)` é executada globalmente logo após o reset da matriz (`glLoadIdentity`), afetando todo o fluxo de renderização que vem a seguir. 

Como o OpenGL opera como uma máquina de estados e não existe um comando de isolamento (como o par `glPushMatrix`/`glPopMatrix`) entre o desenho do primeiro e do segundo objeto, ambos acabam "herdando" a mesma transformação espacial. Na prática, eles passam a compartilhar a mesma origem de coordenadas, o que impossibilita o movimento individual neste estágio.

---

## EX13)

**Pergunta:** O que aconteceu? Qual a diferença entre o giro dos triângulos?

**Resposta:**
Nesta etapa, os objetos passaram a apresentar **cadências de rotação distintas**. Ao atribuir variáveis de controle separadas e aplicar incrementos de valores diferentes para cada uma (ex: `r += 3` e `r2 += 2`), os triângulos perdem a sincronia visual. 

Enquanto um completa seu ciclo de rotação mais rapidamente, o outro permanece em um ritmo mais lento. Isso demonstra que a reinicialização da matriz de visualização entre as chamadas de desenho permite que cada componente da cena possua sua própria lógica de animação de forma isolada.

---

## EX14)

**Pergunta:** O que acontece consigo controlar cada triângulo separadamente agora?

**Resposta:**
Com a implementação de variáveis de estado exclusivas para cada objeto e o devido isolamento das matrizes, alcançamos a **independência total** dos elementos na tela. Agora, cada triângulo funciona como uma unidade autônoma no ambiente virtual: as alterações de posição, rotação ou escala (zoom) aplicadas a um não interferem no comportamento do outro. 

Essa organização é o que permite a criação de interações personalizadas, onde o usuário pode manipular um objeto via teclado (WASD / IJKL) e outro via mouse simultaneamente, sem que as transformações se "atropelem" durante o processamento gráfico.
