## 1) Informações Gerais
### 1.1) Processo
Atualmente a empresa gerencia todos os empréstimos para funcionários através de um controle em Excel com uma estrutura de comunicação e aprovação via e-mail.

### 1.2) Problema
Inexistência de uma plataforma única para centralizar a criação, aprovação e devolução dos materiais com visibilidade dos acontecimentos.

### 1.3) Necessidade
Possuir uma plataforma capaz de gerenciar uma solicitação em sua totalidade, desde a criação, aprovação e devolução e também armazenar o histórico de acontecimentos.

### 1.4) Usuários
EMployee, Manager, Warehouse

## 2) Requisitos
### 2.1) Funcionais
RF01 - O funcionário pode criar requisição
RF02 - O funcionário pode cancelar requisição
RF03 - O funcionário pode solicitar extensão do empréstimo
RF04 - O funcionário poderá visualizar todas as suas requisições, independente do status

RF05 - O gestor pode aprovar uma requisição
RF06 - O gestor pode reprovar uma requisição
RF07 - O gestor pode visualizar as aprovações pendentes de sua equipe
RF08 - O gestor pode visualizar as aprovações e reprovações concluídas de sua equipe

RF09 - O Almoxarifado pode adicionar novos equipamentos
RF10 - O Almoxarifado pode informar entrega do(s) equipamento(s) da requisição
RF11 - O Almoxarifado pode informar recebimento de equipamentos do empréstimo

RF12 - O sistema deve armazenar o histórico de acontecimentos de cada etapa
RF13 - O sistema deve identificar automaticamente empréstimos em atraso
RF14 - O sistema deve permitir registro de novos usuários
RF15 - O sistema deve permitir login de usuários

### 2.2) Não Funcionais
### 2.3) Regras de Negócio
RN01 - O funcionário poderá ter até 3 equipamentos em empréstimo
RN02 - O funcionário  poderá cancelar requisição apenas com status "Aguardando"
RN03 - O funcionário não poderá solicitar mais do que uma extensão de empréstimo

RN04 - Um empréstimo deverá ser devolvido até 30 dias depois da coleta do material
RN05 - Um empréstimo só poderá ser extendido por até 15 dias
RN06 - Uma requisição aprovada terá até 7 dias para retirada dos equipamentos

RN07 - O equipamento não poderá ser emprestado simultaneamente
RN08 - O equipamento de uma solicitação já aprovada não poderá mais ser solicitado simultaneamente por outra requisição 

RN09 - O funcionário somente visualizará as suas solicitações e empréstimos
RN10 - O gestor somente visualizará as aprovações e reprovações concluídas de sua equipe
RN11 - O gestor somente visualizará aprovações pendentes de sua equipe