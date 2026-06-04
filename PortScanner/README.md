# ⚡Port Scanner

> Scanner de portas TCP utilizando pacotes SYN desenvolvido em Python com Scapy.

![python](https://img.shields.io/badge/language-python-blue)
![scapy](https://img.shields.io/badge/library-scapy-orange)
![status](https://img.shields.io/badge/status-active-success)
![license](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Visão Geral

**Port Scanner** é uma ferramenta simples para realizar varreduras TCP utilizando a técnica **TCP SYN Scan**.

O scanner envia pacotes SYN para as portas especificadas e analisa as respostas recebidas para determinar se uma porta está aberta ou fechada.

Esta abordagem é amplamente utilizada em reconhecimento de redes por ser rápida e eficiente.

---

## 🚀 Funcionalidades

* ⚡ Varredura TCP SYN
* 🎯 Múltiplas portas em uma única execução
* 📡 Identificação de portas abertas
* 🔒 Identificação de portas fechadas
* 🐍 Desenvolvido em Python
* 🛠️ Utiliza a biblioteca Scapy
* 💻 Saída simples e objetiva

---

## 📸 Preview

```text id="m2ub7w"
PORTA 22 ABERTA
PORTA 80 ABERTA
PORTA 443 ABERTA
PORTA 8080 FECHADA
```

---

## 🛠️ Requisitos

* Python 3.x
* Scapy
* Permissões de administrador/root

Instale a dependência:

```bash id="kh0b7m"
pip install scapy
```

---

## 📦 Instalação

```bash id="drj02s"
git clone https://github.com/Douglas-fCruz/Tools/PortScanner

cd PortScanner

pip install scapy
```

---

## ⚙️ Utilização

### Escaneando portas específicas

```bash id="e4t2uh"
sudo python portscan.py exemplo.com 80 8080 443
```

---

## 🧩 Parâmetros

| Argumento | Descrição                            |
| --------- | ------------------------------------ |
| Alvo      | IP ou domínio de destino             |
| Portas    | Lista de portas TCP a serem testadas |

### Exemplo

```bash id="7lm4c6"
sudo python portscan.py <domínio> <porta>
```

---

## 🔍 Como Funciona

O scanner utiliza o processo clássico do TCP SYN Scan:

1. Envia um pacote TCP com a flag SYN.
2. Aguarda a resposta do host.
3. Analisa as flags recebidas:

| Resposta       | Significado   |
| -------------- | ------------- |
| SYN + ACK (SA) | Porta aberta  |
| RST + ACK (RA) | Porta fechada |

Esse método permite identificar rapidamente o estado das portas TCP do alvo.

---

## 📁 Estrutura do Projeto

```text id="n7e5im"
PortScanner/
├── portscan.py
└── README.md
```

---

## ⚠️ Aviso Legal

Esta ferramenta foi desenvolvida exclusivamente para fins educacionais e testes autorizados.

O uso indevido contra sistemas sem autorização pode ser ilegal. O autor não se responsabiliza por quaisquer danos ou usos inadequados decorrentes desta ferramenta.

---

## 👨‍💻 Autor

**Douglas Cruz**

🔗 Linkedin: linkedin.com/in/douglas-cruz-a80123275/

---

## 🤝 Contribuições

Contribuições são bem-vindas.

Sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request* com melhorias, correções ou novas funcionalidades.

---

## ⭐ Apoie o Projeto

Se este projeto foi útil para você, considere deixar uma **estrela ⭐** no repositório.
