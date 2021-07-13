## Inteligência Artificial - Aula 1
- O que é? 
- Coisas complicadas demais para serem feitas por seres humanos;
- Filme 2001: Odisseia no Espaço - HAL 9000;
- Robô Sophia;
- Em 1969 era ficção científica. Hoje já é uma realidade;
- Podemos construir um hardware tão complexo quanto o cérebro?
    - Quão complexo é o nosso cérebro?
        - a informação é levada para o cérebro em questão de microssegundos por neurônios;
    - Quão complexos são os computadores que conseguimos construir nos dias atuais?
        - pode ser capaz de levar informações em nanossegundos;
    Conclusão:
        - SIM. Podemos ter computadores com tantos eleentos básicos de processamento quanto nosso cérebro;
        - Muito menos interconexões (fios ou sinapses) do que o cérebro;
        - Atualizações muito mais rápidas do que o cérebro;
        - Mas construir hardware é muito diferente de fazer um computador se comportar como um cérebro!
- Um sistema inteligente deve ser infalível?
    - Nunca comete erros?
    - Tipos de possíveis erros:
        - Erros de hardware, por ex, erros de memória;
        - Erros de software, por ex, bugs de codificação;
        - Erros 'semelhantes aos humanos';
    - Claramente, erros de hardware e software são possíveis na prática;
        - e os erros 'semelhantes aos humanos'?
    - Sistema inteligente pode cometer erros e ainda ser inteligente;
        - humanos não estão certos o tempo todo;
        - nós aprendemos e nos adaptamos comentendo erros;
    - Portanto um sistema inteligente NÃO precisa ser a prova de falhas.

### Um pouco de história
- Filosofia, matemática, economia, neurociências, psicologia;
- IA: termo criado por John McCarthy na década de 50;

### Como construir um sistema de IA?
- Thinking Humanly;
- Thinkin Rationally;
- Acting Humanly;
- Acting Rationally;
- Modelando exatamente como os humanos realmente pensam;
    - Modelos cognitivos de raciocínio humano;
- Modelando exatamente como os humanos realmente agem;
    - Modelos de comportamento humano (o que eles fazem, não como pensam);
- Modelagem de como os agentes ideais 'deveriam pensar';
    - Modelos de pensamento 'racional' (lógica formal);
    note: os humanos muitas vezes não são racionais!
- Modelagem de como os agentes ideais 'deveriam agir;
    - Ações racionais, mas não necessariamente raciocínio racional formal;
        - Abordagem de caixa preta/engenharia;
- IA moderna se concentra na última definição;
    - Métodos modernos são inspirados em ciências cognitivas e neurociências (como as pessoas pensam);

### Máquinas que pensam como humanos
- Determinar como os humanos pensam;
- Compreensão do funcionamento real das mentes humanas;
    - Introspecção - capte nossos próprios pensamentos conforme eles passam;
    - Experimentos psicológicos;
- Teoria da mente suficientemente precisa:
    - Expressar a teoria como um programa de computador;
- Se o comportamento de entrada/saída e tempo do programa corresponder ao comportamento humano, isso é evidência de que alguns dos mecanismos do programa também podem estar operando em humanos;
- Como sabemos como os humanos pensam?
- Programas resolvendo problemas corretamente não é suficiente;
    - Comparar o traço de seus passos de raciocínio com traços de sujeitos humanos resolvendo os mesmos problemas;
- Ciência cognitiva: modelos de computador da IA e técnicas experimentais da psicologia;
    - Teorias precisas e testáveis do funcionamento da mente humana;
    - Visão, linguagem natural e aprendizagem;

### Máquinas que agem como humanos
- Comportamento inteligente como a capacidade de alcançar desemenho de nível humano em todas as tarefas cognitivas, suficiente para enganar um agente humano com quem se interage;
- Teste de Turing;
    - Usa o 'Jogo de Imitação' (método usual);
    - Três pessoas jogam (homem, mulher, interrogador);
    - O interrogador determina qual jogador é o homem e qual é a mulher fazendo perguntas;
        - Ex: qual o comprimento do cabelo?
    - Datilografado ou repetido por um intermediário;
    - O jogador A tem como objetivo enganar o Interrogador e o Jogador B tem como objetivo ajudá-lo a acertar;
    - Trocamos o jogador A por um programa de computador;
    - O interrogador decidirá erroneamente com a mesma frequência quando o jogo é jogado dessa forma ou quando o jogo é disputado entre um homem e uma mulher?
    - Existem variações;
    - O entendimento comum diz que o propósito do teste de Turing não é especificamente determinar se um computador é capaz de enganar um interrogador fazendo-o acreditar que é um humano, mas sim se um computador poderia imitar um humano.
    - Requer sucesso em:
        - Processamento de linguagem natural: comunicação com o interrogador;
        - Representação do conhecimento: armazene e recupere o que sabe;
        - Raciocínio automatizado: use as informações armazenadas para responder a perguntas e tirar novas conclusões;
        - Aprendizado de máquina: adapte-se a novas circunstâncias e detecte e extrapole padrões.

### Máquinas que pensam racionalmente
- Aristóteles foi um dos primeiros a tentar codificar pensamento correto;
    - Processos de raciocínio irrefutáveis;
    - Silogismos: padrões para estruturas de argumento: sempre deram conclusões corretas dadas as premissas corretas;
    - Leis do pensamento que deveriam governar o funcionamento da mente;
- A lógica formal fornece uma notação precisa para declarações sobre todos os tipos de coisas no mundo e as relações entre elas;
- Os humanos nem sempre são racionais;
    - Grande diferença entre ser capaz de resolver um problema e fazê-lo;
- Racional - definido em termos de lógica?
- A lógica não pode expressar tudo: conhecimento informar, o conhecimento é menos que 100% certo;
- A abordagem lógica muitas vezes não é viável em termos de tempo de computação (precisa de orientação);

### Máquinas que agem racionalmente
- Comportamento racional: fazer a coisa certa;
- A coisa certa: aquilo que se espera maximizar o alcance das metas, dadas as informações disponíveis;
- A inferência correta não é toda racionalidade;
    - Situações em que não há coisa comprovadamente correta a fazer, mas algo ainda deve ser feito;
    - Formas de agir racionalmente que não podem ser razoavelmente consideradas como envolvendo inferência;
        Ex: puxar a mão de um fogão quente é um reflexo que tem mais sucesso do que uma ação mais lenta realizada após uma deliberação cuidadosa.

### Subáreas da IA
![subareas da IA](subareas_da_IA.png)

- Busca
- Representação de conhecimento e raciocínio
- planejamento
- aprendizado
- processamento de linguagem natural
- interagindo com o ambiente
- *To be continued...*

## Aprendizado de Máquina
- Definições:
    - Ciência (ou arte) da programação de computadores para que eles possam aprender com os dados;
    - 'Campo de estudo que oferece aos computadores a capacidade de aprender sem serem explicitamente programados'. Arthur Samuel, 1959;
    - Um algoritmo determinístico possui regras claras para retornar resultados de acordo com a entrada fornecida;
    - Se a entrada pode variar muito, esse conjunto de regras será muito grande, podendo tornar o tempo de execução inviável.
- Programação 'tradicional' (Sistemas baseados em regras):
    - Natureza dinâmica dos problemas exige redefinição constante das regras;
    - Sistema de detecção de SPAM de e-mail;
        - Ex: um filtro de spam baseado em aprendizado de máquina é capaz de utilizar critérios diversos para fazer tal classificação;
            - Caracterização de um SPAM pode ser adaptada dinamicamente de acordo com marcações atribuídas pelos usuários;
            - Spammers identificam que as regras não detectam números e trocam 'Dois' por 2
- Fundamentalmente, envolve a construção de modelos matemáticos para ajudar entender dados;
    - Funções complexas;
- Ajustes de parâmetros;
    - Permite que os modelos sejam adaptados aos dados observados;
- Desta forma, tais modelos podem ser usados para prever e entender aspectos de dados desconhecidos;

### Utilização de aprendizado de máquina
- Algoritmos podem ser melhorados, a partir da análise dos resultados;
- Aplicação de técnicas avaliar grandes quantidades de dados;
    - Descobrir padrões que não eram aparentes;
- Utilização como um processo iterativo, em busca de soluções a partir dos dados, e otimização do uso dos dados e algoritmos;
- Esse processo pode ser automatizado em algum nível;
