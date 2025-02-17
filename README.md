# Firewall_ai - Scanner de Rede com IA para Infraestrutura On-Premises
O firewall_ai é uma aplicação desenvolvida com Flask e OpenAI para realizar varreduras de rede em um ambiente on-premises e gerar explicações sobre vulnerabilidades encontradas. Através de um simples formulário, é possível escanear portas e serviços de uma rede local e obter explicações geradas pela IA sobre os riscos e como mitigá-los.
Este sistema usa nmap para escanear a rede e OpenAI para fornecer informações detalhadas sobre vulnerabilidades, ajudando a melhorar a segurança da infraestrutura de TI.

![image](https://github.com/user-attachments/assets/8325befe-786c-442e-8bb2-069b87e6b326)

________________________________________
## Funcionalidades
- Varredura de Rede: Realiza varredura completa de portas de um IP ou domínio utilizando o nmap.
- Análise de Vulnerabilidades: Para cada serviço encontrado, a IA explica potenciais riscos e sugere formas de mitigação.
- Interface Web: O sistema fornece uma interface web simples e interativa para facilitar o uso e a visualização dos resultados.
________________________________________
## Pré-Requisitos
Certifique-se de ter as seguintes dependências instaladas:
- Python 3.6+
- nmap: Utilizado para realizar a varredura de rede.
- Flask: Framework web utilizado para a construção da interface.
- openai: Biblioteca para integração com a API da OpenAI para análise de vulnerabilidades.

Você pode instalar as dependências do projeto utilizando o requirements.txt.
 
## Instalação
- 1.	Clone o repositório:
```
git clone https://github.com/LeviLucena/Firewall_ai.git
cd firewall_ai
```

- 2.	Crie um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
source venv/bin/activate   # Para sistemas Unix
venv\Scripts\activate      # Para sistemas Windows
```

- 3.	Instale as dependências:
```
pip install -r requirements.txt
```

- 4.	Configure a chave da API da OpenAI:
> Abra o arquivo ai_helper.py e substitua "SUA_CHAVE_OPENAI" pela sua chave de API da OpenAI:
```openai.api_key = "SUA_CHAVE_OPENAI"```

## Licença
Este projeto está sob a licença MIT. Você pode obter uma cópia da licença [aqui](https://opensource.org/licenses/MIT).
