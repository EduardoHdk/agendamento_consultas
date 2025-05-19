# Sistema de Agendamento de Consultas

Este projeto é um sistema simples para agendamento, listagem e cancelamento de consultas, com funcionalidades tanto em um script de Python quanto em uma interface web responsiva.

---

## 📝 Funcionalidades

### Arquivo Python: `Consulta.py`
- **Menu interativo**:
  - Agendar consultas.
  - Listar consultas agendadas.
  - Cancelar consultas.
  - Sair do sistema.
- **Validação de dados**:
  - Verifica se a data é futura ou do dia atual.
  - Restringe horários entre 11:00 e 19:00.
- **Sistema baseado em console**:
  - Usuários interagem com prompts diretamente pelo terminal.

### Arquivo Web: `index.html`
- **Interface responsiva**:
  - Interface moderna utilizando a biblioteca CSS [PicoCSS](https://picocss.com).
- **Funcionalidades principais**:
  - **Agendar consulta**: Formulário que coleta nome, especialidade, data e horário.
  - **Listar consultas**: Lista dinâmica das consultas agendadas.
  - **Cancelar consultas**: Possibilidade de cancelar consultas diretamente na lista.
- **Validação de dados**:
  - Impede seleção de datas anteriores ao dia atual.
  - Verifica se os campos estão preenchidos antes do envio.

---

## 🚀 Como Usar

### Python (Arquivo `Consulta.py`)
1. Certifique-se de ter o Python 3 instalado.
2. Abra o terminal e execute:
   ```bash
   python Consulta.py
