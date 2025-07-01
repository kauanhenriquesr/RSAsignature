import base64
from src.verifica_assina import assinatura, verifica
from src.rsa import gera_chave


def assina(file_path, n, private_key):
    assinaturaarq = assinatura(file_path, n, private_key)
    print("Assinatura gerada com sucesso!")
    print("-"*30)
    print("Assinatura:", assinaturaarq)
    with open(file_path[0:-4]+"_assinatura.sig", "w") as f:
        f.write(assinaturaarq)
        print("-"*30)
        print(
            f"Assinatura salva em {file_path[0:-4]}_assinatura.sig com sucesso!")


def verifica_assinatura(file_path, assinatura, n, public_key):
    print("-"*30)
    print("Verificando assinatura do arquivo:", file_path)
    print("-"*30)
    print("Assinatura:", assinatura)
    print("-"*30)
    if verifica(file_path, assinatura, n, public_key):
        print("Assinatura VÁLIDA e corresponde ao arquivo!")
    else:
        print("Assinatura INVÁLIDA ou não corresponde ao arquivo.")


def main(args):
    if args == [] or args[0] in ["-h", "--help"]:
        print("Assinatura Digital")
        print("="*100)
        print("Uso:\n"
              "   - python src/__main__.py -gen_keys\n"
              "   - python src/__main__.py -sign <arquivo>\n"
              "   - python src/__main__.py -verify <arquivo> <assinatura>\n")
        return 0

    elif args[0] == "-gen_keys":
        if len(args) != 1:
            print("Uso: python src/__main__.py -gen_keys")
            return 1
        print("Gerando chaves RSA...")
        n, e, d = gera_chave()
        print("-"*100)
        print("Chaves geradas com sucesso!")
        print("N: ", n)
        print("Public Key: ", e)
        print("Private Key: ", d)
        print("-"*100)

        with open("assets/public_key.key", "w") as f:
            f.write(str(e))
        with open("assets/private_key.key", "w") as f:
            f.write(str(d))
        with open("assets/n.key", "w") as f:
            f.write(str(n))
        print("Chaves salvas em assets/public_key.key, assets/private_key.key e assets/n.key com sucesso!")
        return 0

    elif args[0] == "-sign":
        if len(args) != 2:
            print("Uso: python src/__main__.py -sign <arquivo>")
            return 1
        file_path = args[1]
        try:
            n = int(open("assets/n.key").read())
        except FileNotFoundError:
            print(f"Arquivo de N não encontrado. Por favor, gere as chaves primeiro.\n"
                  " - Se você não gerou as chaves, execute:\n"
                  "   python src/__main__.py -gen_keys")
            return 1
        try:
            private_key = int(open("assets/private_key.key").read())
        except FileNotFoundError:
            print(
                f"Arquivo de chave privada não encontrado. Por favor, gere as chaves primeiro.")
            return 1
        try:
            assina(file_path, n, private_key)
            return 0
        except FileNotFoundError:
            print(f"Arquivo {file_path} não encontrado.")
            return 1

    elif args[0] == "-verify":
        if len(args) != 3:
            print("Uso: python src/__main__.py -verify <arquivo> <assinatura>")
            return 1
        file_path = args[1]
        assinatura_file = args[2]
        try:
            assinatura = open(assinatura_file).read()
        except FileNotFoundError:
            print(
                f"Arquivo de assinatura {assinatura_file} não encontrado. Por favor, gere uma assinatura primeiro.")
            return 1

        try:
            n = int(open("assets/n.key").read())
        except FileNotFoundError:
            print(f"Arquivo de N não encontrado. Por favor, gere as chaves primeiro.")
            return 1

        try:
            public_key = int(open("assets/public_key.key").read())
        except FileNotFoundError:
            print(
                f"Arquivo de chave pública não encontrado. Por favor, gere as chaves primeiro.")
            return 1

        verifica_assinatura(file_path, assinatura, n, public_key)
        return 0
