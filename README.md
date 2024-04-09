# probabilidade-estatistica

Este repositório contém materiais e códigos relacionados ao estudo de probabilidade e estatística.

## Tabela de Frequências

Um dos códigos disponíveis neste repositório é um script Python para gerar uma tabela de frequências para um conjunto de dados. Este script suporta tanto dados contínuos quanto discretos.

Para dados contínuos, o script calcula o número de classes usando a fórmula `K=1+3.32log(n)`, onde `n` é o número de pontos de dados. Ele também calcula a amplitude da amostra (o maior valor menos o menor valor) e a amplitude da classe (a amplitude da amostra dividida pelo número de classes).

A tabela de frequências gerada inclui as seguintes colunas:

- `xi`: As classes (para dados contínuos) ou os valores únicos (para dados discretos)
- `fi`: A frequência absoluta de `xi`
- `Fi`: A frequência absoluta acumulada de `xi`
- `fr`: A frequência relativa de `xi`
- `Fr`: A frequência relativa acumulada de `xi`

## Como usar

Para usar o script de tabela de frequências, você precisará ter Python instalado em seu computador. Você também precisará das bibliotecas pandas e numpy, que podem ser instaladas usando o gerenciador de pacotes pip do Python:

```bash
pip install pandas numpy