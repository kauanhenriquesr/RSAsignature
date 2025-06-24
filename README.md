# Uso do RSAsignature

Este projeto é operado inteiramente através de uma interface de linha de comando (CLI). Todas as funcionalidades, desde a geração de chaves até a verificação de assinaturas, são acessadas por meio de comandos específicos no seu terminal.

## Comandos Disponíveis

A seguir, estão detalhadas as três funções principais do programa.

### 1\. Gerar um Novo Par de Chaves

Este é o primeiro passo para utilizar o sistema. O comando inicializa e gera um par de chaves RSA (pública e privada) de 2048 bits, junto com o módulo `n` necessário para as operações.

  - **Comando**
    ```bash
    python __main__.py -gen_keys
    ```
  - **O que Acontece?**
      - O programa executa o algoritmo de geração de chaves.
      - As chaves e o módulo `n` são exibidos no terminal.
      - Três arquivos são criados e salvos no diretório `assets/`:
          - `public_key.key`: Contém o expoente da chave pública (`e`).
          - `private_key.key`: Contém o expoente da chave privada (`d`).
          - `n.key`: Contém o módulo comum (`n`).
      - Você **deve** executar este comando antes de tentar assinar ou verificar qualquer arquivo.

### 2\. Assinar um Arquivo

Este comando cria uma assinatura digital para um arquivo de sua escolha. Ele usa a chave privada (gerada no passo anterior) para garantir a autenticidade.

  - **Comando**
    ```bash
    python __main__.py -sign <caminho_do_arquivo>
    ```
  - **Exemplo Prático**
    ```bash
    python __main__.py -sign assets/teste.txt
    ```
  - **O que Acontece?**
      - O programa lê os arquivos `assets/private_key.key` e `assets/n.key`.
      - Ele calcula o hash (SHA3-512) do arquivo especificado (e.g., `assets/teste.txt`).
      - A assinatura é gerada aplicando a operação RSA com a chave privada sobre o hash (utilizando o padding OAEP).
      - A assinatura resultante é codificada em Base64 e salva no arquivo `<caminho_do_arquivo>_assinatura.sig`.

### 3\. Verificar uma Assinatura

Este comando verifica se um arquivo não foi alterado e se a assinatura corresponde à chave pública do remetente.

  - **Comando**
    ```bash
    python __main__.py -verify <caminho_do_arquivo> <caminho_da_assinatura>
    ```
  - **Exemplo Prático**
    ```bash
    python __main__.py -verify assets/teste.txt assets/teste_assinatura.sig
    ```
  - **O que Acontece?**
      - O programa lê os arquivos `assets/public_key.key` e `assets/n.key`.
      - Ele lê a assinatura do arquivo de assinatura especificado (e.g., `assets/assinatura.sig`).
      - A operação RSA com a chave pública é aplicada na assinatura para recuperar o hash original.
      - Paralelamente, o hash do arquivo original (e.g., `assets/teste.txt`) é recalculado.
      - Os dois hashes são comparados. O programa então imprime no terminal se a **assinatura foi verificada com sucesso** ou se ela é **inválida**.

### 4\. Obter Ajuda

Se você esquecer os comandos, pode executar o programa sem argumentos ou com as flags de ajuda.

  - **Comando**
    ```bash
    python __main__.py -h
    ```
    ou
    ```bash
    python __main__.py --help
    ```
  - **O que Acontece?**
      - Uma mensagem de ajuda simples é exibida, listando os comandos disponíveis e seu uso básico.
