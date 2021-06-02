## Exploração de Dados

### Introdução
- Parte arte, parte ciência;
    - acertar na arte sem errar na ciência e vice-versa;
- Comunicar os dados com precisão;
    - Não enganar ou distorcer dados;
    - Se um número é duas vezes maior que outro, mas na visualização eles parecem ser quase iguais, então a visualização está errada;
- Deve ser visualmente agradável;
    - Se uma figura contiver cores dissonantes, elementros visuais desequilibrados ou outros recursos distraem, o observador terá mais dificuldade em interpretar a figura corretamente;
- Figuras:
    - Feias, ruins e erradas
        - Feias: uma figura que tem problemas estéticos, mas por outro lado é clara e informativa;
        - Ruins: Uma figura que tem problemas relacionados à percepção, pode ser pouco claro, confuso, excessivamente complicado ou enganador;
        - Erradas: Uma figura que tem problemas relacionados à matemática; é objetivamente incorreta.

### Diretório de Visualizações
- Valores numéricos mostrados para um conjunto de categorias;
    - Barras verticais ou horizontais
- Histograma e gráficos de densidade fornecem as visualizações mais intuitivas de uma distribuição
- As densidades cumulativas e os gráficos quantil-quantil (q-q) representam os dados fielmente, mas podem ser mais difíceis de interpretar;
- Gráficos de pizza, barras lado a lado ou barras empilhadas;
    - Evitar uso dos graficos de pizza;
- Os gráficos de dispersão (Scatterplots) são normalmente utilizados para mostrar a relação entre duas variáveis quantitativas;
    - Para três variáveis: mapear uma no tamanho do ponto - gráfico de bolhas (bubble chart);
- Representando Incertezas:
    - Barras de erro indicam a faixa de valores prováveis para alguma estimativa ou medição;
        - Estender horizontalmente e+ou verticalmente a partir de algum ponto de referência que representa a estimativa ou medição;

### Matplotlib
- Biblioteca de visualização de dados multiplataforma construída em matrizes NumPy e projetada para funcionar com a pilha SciPy mais ampla;
- Funciona bem com muitos sistemas operacionais e backends gráficos;
- Customização da aparência;
Estilo MATLAB vs Orientado a Objetos;
- A partir de um arquivo python:

        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace (0, 10, 100)
        plt.plot(x, np.sin(x))
        plt.plot(x, np.cos(x))

        plt.show()

- A partir do Jupyter:

        import matplotlib.pyplot as plt
        import numpy as np

        x = np.linspace(0, 10, 100)
        plt.plot(x, np.sin(x), '-')
        plt.plot(x, np.cos(x), '--')