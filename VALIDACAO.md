# Validação da entrega

Data: 18/09/2026

## Painel

- HTML atualizado preservado como `public/index.html`.
- Dois mapas JPEG incorporados ao próprio HTML.
- Layout de mapas na versão 4.
- Teste em navegador concluído: abertura local, importação da base, busca, destaque no mapa, edição, persistência, reimportação sem duplicidade, exportação/restauração de backup e visualização responsiva.

## Base inicial

- 284 registros.
- 271 referências únicas.
- 5 containers.
- 3.679 caixas informadas.
- 747.149 unidades informadas.
- LN-076 do container 26016 no Corredor 7.
- ATD-125 presente somente no container 26021.

## GitHub e Firebase

- Repositório público não contém a base inicial, planilhas ou backups.
- `.gitignore` bloqueia dados operacionais e credenciais administrativas.
- Workflow publica somente `public/index.html`.
- Configuração Firebase é inserida no artefato de publicação por variável do GitHub.
- Regras Firestore adotam perfis `viewer`, `editor` e `admin`.
- Alterações de estoque exigem evento de auditoria associado.
- Exclusão de estoque e alteração/exclusão do histórico são bloqueadas pelo cliente.

## Dependências externas para entrada em produção

- Projeto Firebase criado pelo responsável da UNISO.
- Authentication e Firestore habilitados.
- Usuários e perfis cadastrados.
- Regras publicadas no projeto real.
- Variável `FIREBASE_CONFIG_JSON` cadastrada no GitHub.
- Domínio do GitHub Pages autorizado no Firebase Authentication.
- Carga inicial importada por usuário autorizado e conferida.

