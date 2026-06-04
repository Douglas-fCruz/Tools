# 📂 Directory Finder

> Ferramenta simples de enumeração de diretórios web utilizando Python e wordlists.

![python](https://img.shields.io/badge/language-python-blue)
![status](https://img.shields.io/badge/status-active-success)
![license](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Visão Geral

**Directory Finder** é uma ferramenta leve desenvolvida em Python para realizar **Directory Bruteforce** em aplicações web.

Utilizando uma wordlist, o script testa múltiplos caminhos em um domínio e identifica diretórios válidos que retornam resposta HTTP **200 OK**.

Ideal para estudantes de segurança ofensiva, pentesters e profissionais que desejam realizar reconhecimento inicial de aplicações web.

---

## 🚀 Funcionalidades

* 📂 Enumeração de diretórios web
* 🔎 Detecção automática de páginas válidas
* ⚡ Execução rápida e simples
* 🌐 Suporte a HTTPS
* 📜 Compatível com qualquer wordlist
* 🐍 Desenvolvido em Python
* 💻 Saída limpa diretamente no terminal

---

## 📸 Preview

```bash
[+] https://example.com/admin
[+] https://example.com/login
[+] https://example.com/uploads
```

---

## 🛠️ Requisitos

* Python 3.x
* Biblioteca Requests

Instale a dependência:

```bash
pip install requests
```

---

## 📦 Instalação

```bash
git clone https://github.com/SEU-USUARIO/Directory-Finder.git

cd Directory-Finder

pip install requests
```

---

## ⚙️ Utilização

### Execução básica

```bash
python directory_finder.py exemplo.com wordlist.txt
```

---

## 🧩 Parâmetros

| Argumento | Descrição                            |
| --------- | ------------------------------------ |
| Domínio   | Alvo da enumeração                   |
| Wordlist  | Lista de diretórios a serem testados |

### Exemplo

```bash
python directory_finder.py alvo.com common.txt
```

---

## 💣 Como Funciona

Para cada entrada da wordlist, a ferramenta:

1. Monta uma URL baseada no domínio informado.
2. Realiza uma requisição HTTP GET.
3. Verifica o código de resposta.
4. Exibe apenas diretórios que retornam **200 OK**.

Exemplo:

```text
admin
login
uploads
backup
```

Resultará em:

```text
https://alvo.com/admin
https://alvo.com/login
https://alvo.com/uploads
https://alvo.com/backup
```

---

## 📁 Estrutura do Projeto

```text
directory-finder/
├── directory_finder.py
├── README.md
└── wordlists/
```

---

## ⚠️ Aviso Legal

Esta ferramenta foi desenvolvida exclusivamente para fins educacionais e testes autorizados.

O uso indevido contra sistemas sem autorização pode violar leis locais e internacionais. O autor não se responsabiliza pelo uso inadequado da ferramenta.

---

## 👨‍💻 Autor

**Douglas Cruz**

🔗 GitHub: https://github.com/Douglas-fCruz

---

## 🤝 Contribuições

Contribuições são bem-vindas.

Sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request* com melhorias, correções ou novas funcionalidades.

---

## ⭐ Apoie o Projeto

Se este projeto foi útil para você, considere deixar uma **estrela ⭐** no repositório.
