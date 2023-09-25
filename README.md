# Sistema de Monitoramento de Ambiente para Vinícola

>Status: Em desenvolvimento ⚙️
>

Este projeto consiste em um sistema de monitoramento de ambiente para uma vinícola, permitindo o acompanhamento das condições ambientais importantes, como luminosidade, temperatura e umidade. Até o momento, apenas o sensor de luminosidade está em funcionamento.

## Draft da arquitetura
![FiwareDeploy drawio](https://github.com/G3n4r00/Repositorio-Vinheria/assets/126473193/8e16ec46-9d80-491e-9490-236273013a0e)


## Hardware Utilizado

O sistema é controlado por um ESP32, um microcontrolador amplamente utilizado em projetos IoT devido à sua versatilidade e conectividade. Para monitorar a luminosidade, utilizamos um sensor de luminosidade conectado ao ESP32.
Ao longo da implementação do projeto faremos a conexão na nuvem com os sensores de temperatura e umidade igualmente

## Sensor de Luminosidade

O sensor de luminosidade captura dados de luminosidade no ambiente e os envia para o ESP32. O ESP32 processa esses dados e os envia para um sistema de backend para armazenamento e análise posteriores.

## Sensor de Temperatura 

O sensor de temperatura captura os dados de temperatura ao longo do dia e posteriormente utilizaremos para criar gráficos e recomendações ao dono da vinheria

## Sensor de Umidade

O sensor de temperatura captura os dados de temperatura ao longo do dia e posteriormente utilizaremos para criar gráficos e recomendações ao dono da vinheria

## Backend

O sistema de backend é construído com Docker, Fiware e STH Comet:

- **Docker Compose**: Utilizamos contêineres Docker para simplificar o gerenciamento e a implantação de nossos serviços. Isso nos permite manter nosso ambiente de desenvolvimento e produção consistente.

- **Fiware**: Fiware é uma plataforma de código aberto que fornece ferramentas e componentes para o desenvolvimento de aplicativos IoT e Smart Cities. Utilizamos Fiware para gerenciar nossos dados e serviços.

- **STH Comet**: STH Comet é uma extensão do Fiware que permite armazenar e consultar séries temporais de dados de sensores. Usamos o STH Comet para armazenar as leituras do sensor de luminosidade ao longo do tempo.

## Visualização de Dados

Com os dados armazenados no STH Comet, podemos criar gráficos para visualizar as últimas leituras de luminosidade. Isso nos permite acompanhar as variações de luminosidade ao longo do tempo e tomar decisões informadas relacionadas ao ambiente da vinícola.

### Exemplo de Gráfico de Luminosidade 



## Instruções de Uso

1. **Montagem do Hardware**: Monte o hardware, conectando o sensor de luminosidade ao ESP32 conforme as instruções do fabricante.

2. **Configuração do ESP32**: Configure o ESP32 para ler os dados do sensor de luminosidade e enviar esses dados para o sistema de backend. Isso pode ser feito através do código disponível no repositório deste projeto.

3. **Configuração do Backend**:
   - Instale o Docker em seu servidor.
   - Clone este repositório.
   - Execute os contêineres Docker necessários para o Fiware e o STH Comet.
   - Configure o Fiware para receber os dados do ESP32.
   - Configure o STH Comet para armazenar as leituras do sensor de luminosidade.

4. **Visualização de Dados**: Utilize as ferramentas de visualização de dados de sua escolha para criar gráficos com as últimas leituras de luminosidade armazenadas no STH Comet.

## Licença

Este projeto é licenciado sob a [Longest Wave Tech](LongestWaveTech.).

## Autores

- Paloma Mirella - RM551321

- Gabriel Genaro - RM551986
