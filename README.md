# Painel de Posições de Estoque — UNISO

Repositório público do painel de localização de produtos do CD. O arquivo principal está em `public/index.html` e já contém os mapas atualizados das ruas 1 a 10, Beleza, Mezanino e Garagem Principal.

## Segurança dos dados

Este repositório **não deve conter planilhas, bases JSON ou backups do estoque**. A interface fica no GitHub Pages; registros, saldos e histórico ficam no Cloud Firestore. O `.gitignore` bloqueia os formatos operacionais mais comuns, mas revise os arquivos antes de cada envio.

## 1. Preparar o Firebase

1. Crie um projeto no [Console Firebase](https://console.firebase.google.com/).
2. Em **Authentication → Sign-in method**, habilite **E-mail/senha**.
3. Em **Authentication → Users**, cadastre os usuários do painel.
4. Crie o banco **Cloud Firestore** em modo de produção.
5. Publique `firestore.rules` e `firestore.indexes.json` com a Firebase CLI:

   ```bash
   npm install -g firebase-tools
   firebase login
   firebase use --add
   firebase deploy --only firestore:rules,firestore:indexes
   ```

6. Na coleção `users`, crie um documento para cada usuário. O ID do documento deve ser exatamente o **UID** exibido no Authentication. Inclua o campo de texto `role` com um destes valores:

   - `viewer`: somente consulta;
   - `editor`: consulta, importação e edição do estoque;
   - `admin`: permissões do editor e edição das áreas dos mapas.

O primeiro usuário responsável pela carga inicial deve ser `admin` ou `editor`.

## 2. Configurar o GitHub Pages

1. Crie um repositório e envie todo o conteúdo deste pacote para a branch `main`.
2. No Firebase, registre um **aplicativo Web** e copie o objeto `firebaseConfig`.
3. No GitHub, abra **Settings → Secrets and variables → Actions → Variables**.
4. Crie a variável `FIREBASE_CONFIG_JSON` e cole o objeto como JSON em uma única linha, por exemplo:

   ```json
   {"apiKey":"...","authDomain":"...","projectId":"...","storageBucket":"...","messagingSenderId":"...","appId":"..."}
   ```

5. Em **Settings → Pages**, selecione **GitHub Actions** como origem.
6. Execute o workflow **Publicar painel no GitHub Pages** ou faça um novo push na `main`.
7. Em **Firebase Authentication → Settings → Authorized domains**, inclua o domínio do Pages, como `usuario.github.io`.

A configuração de aplicativo Web é pública por natureza. A proteção real está no login e nas regras do Firestore. Nunca use uma chave privada ou arquivo de conta de serviço no GitHub.

Se a variável não estiver cadastrada, o painel ainda será publicado, porém iniciará no modo local. A configuração também pode ser colada manualmente na tela **Configurações** do painel em cada dispositivo.

## 3. Carregar a base inicial no Firebase

A base inicial é entregue em um pacote privado separado e não pertence a este repositório.

1. Abra o endereço publicado no GitHub Pages.
2. Entre em **Configurações** com o usuário `admin` ou `editor`.
3. Acesse **Importar dados**.
4. Selecione `Base_Inicial_UNISO.json`.
5. Revise a prévia e confirme a importação.
6. Verifique os indicadores: **284 registros, 271 referências, 5 containers, 3.679 caixas e 747.149 unidades informadas**.
7. Pesquise `LN-076`: o registro do container 26016 deve aparecer no **Corredor 7**.
8. Pesquise `ATD-125`: deve existir no container 26021, sem registro no 26020.
9. Exporte um backup completo após a validação.

A importação é idempotente: o mesmo arquivo não soma novamente os recebimentos já existentes. Em uma falha de conexão, reabra a prévia; registros já concluídos serão reconhecidos.

## 4. Checklist de liberação

- Login de `viewer` consulta, mas não edita.
- Login de `editor` importa e altera registros.
- Login de `admin` também ajusta áreas dos mapas.
- Usuário não autenticado não acessa estoque nem histórico.
- GitHub Pages abre pelo celular e pelo computador.
- Busca por REF, COD, container, setor, linha e posição retorna resultados.
- Os dois mapas carregam e destacam as áreas corretas.
- Base e backups não aparecem no repositório público.
- Backup completo foi exportado e armazenado em local restrito.

## Estrutura

```text
.
├── .github/workflows/deploy-pages.yml
├── public/index.html
├── scripts/injetar_config_firebase.py
├── firestore.rules
├── firestore.indexes.json
├── firebase.json
├── .firebaserc.example
├── .gitignore
└── README.md
```

## Atualizações do painel

Substitua `public/index.html` pela nova versão validada e envie para a branch `main`. O workflow preservará a configuração do Firebase durante a publicação. Antes do push, confirme que o HTML contém `const FIREBASE_DEFAULT = null;`; o workflow usa esse marcador para inserir a configuração apenas no artefato publicado.

