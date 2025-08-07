![Screenshot da Calculadora](assets\img.png)

# 🧮 Calculadora com Interface Gráfica (Flet + Python)

Este projeto nasceu de um **desafio lançado em live**, onde fui desafiado a **replicar uma calculadora de terminal feita em Python**, criada por um amigo no Discord, mas **usando Java**. No entanto, decidi ir além e desenvolvi uma versão mais completa, **com interface gráfica moderna utilizando Python e Flet**.

---

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Flet](https://flet.dev/)
- [numexpr](https://github.com/pydata/numexpr)
- [keyboard](https://github.com/boppreh/keyboard)

---

## 🧠 Funcionalidades

- Interface responsiva e estilosa usando Flet.
- Suporte a **teclado físico** (digitação das teclas de operação e números).
- Cálculos com os operadores: `+`, `-`, `*`, `/`, `%`, `=`.
- Botões `AC` (limpar tudo) e `Backspace`.
- Exibição em tempo real da equação e resultado.
- Operação segura usando `numexpr` para evitar `eval`.

---

## 📸 Interface

A interface é semelhante a uma calculadora de bolso tradicional, com:

- Área superior para a **equação digitada** e o **resultado**.
- Grade de botões dispostos em `4x5`, com estilo moderno e cores bem definidas.

---

## 🧪 Como Executar

> Requisitos: Python 3.10+ instalado

1. Instale as dependências:
```bash
pip install flet numexpr keyboard
```

2. Execute o projeto:
```bash
python main.py
```

> Obs.: Em alguns sistemas, a biblioteca `keyboard` pode requerer permissões de administrador.

---

## 🖱️ Controles

Você pode interagir com a calculadora de duas formas:

- **Clique nos botões** com o mouse;
- **Use o teclado** físico: os números e operadores são reconhecidos.

| Tecla         | Função              |
|---------------|---------------------|
| `0-9`         | Dígitos             |
| `+ - * /`     | Operações           |
| `Enter` ou `=`| Calcula resultado   |
| `Backspace`   | Apaga último caractere |
| `Esc`         | Limpa tudo          |
| `,` ou `.`    | Decimal             |
| `%`           | Porcentagem         |

---

## 🧠 Estrutura do Projeto

```
calculadora_flet/
├── main.py         # Arquivo principal com interface e teclado
└── models.py       # Funções de lógica (clique, calcular, apagar, etc.)
```

---

## 📚 O que eu aprendi

Durante o desenvolvimento desse projeto, aprendi bastante sobre:

- Criação de interfaces gráficas com Flet;
- Manipulação de eventos do teclado usando a biblioteca `keyboard`;
- Separação de responsabilidades em módulos (`main.py` para UI e `models.py` para lógica);
- Execução de tarefas paralelas com `threading` para escutar teclas sem travar a UI;
- Expressões numéricas seguras com `numexpr`, evitando o uso de `eval`.

---

## 🐞 Erros e melhorias futuras

Além de pequenas falhas de lógica e comportamentos que ainda quero refinar, o projeto apresenta **erros de arquitetura** importantes que reconheci durante e após o desenvolvimento:

- Toda a estrutura está baseada em funções soltas e globais, sem organização orientada a objetos;
- A maior parte da lógica da interface está concentrada no `main.py`, o que quebra o princípio da responsabilidade única;
- A falta de separação entre lógica de negócio e UI torna o código difícil de manter e expandir;
- O uso de variáveis globais (`t_num`, `t_sinais`) pode gerar conflitos inesperados se o projeto crescer;
- A lógica de teclado e interface está acoplada demais — seria melhor desacoplar os eventos de teclado em um módulo próprio;


Embora funcional, o projeto possui alguns pontos que desejo melhorar futuramente:

- A função de porcentagem ainda é simples e só funciona no último número da equação;
- O botão `,` sempre envia `.` para o cálculo, o que pode confundir usuários brasileiros;
- Quando a equação termina em um operador e o usuário pressiona `=`, o resultado é calculado com base na equação sem o operador, o que pode ser confuso;
- Melhor tratamento de exceções para evitar travamentos com entradas inválidas;
- Testes automatizados e validação da entrada do usuário.

---

## 💡 Possíveis Melhorias Futuras

- Suporte a histórico de cálculos.
- Modo científico com mais operadores.
- Responsividade para diferentes tamanhos de tela.
- Deploy como aplicativo desktop (via PyInstaller ou Flet Desktop).

---

## 🤝 Agradecimentos

Esse projeto foi uma experiência incrível de aprendizado ao vivo. Agradeço à comunidade que acompanhou e desafiou essa construção!

---

## 📜 Licença

Este projeto é livre para estudos e modificações pessoais. Faça bom uso e se divirta codando! 🚀