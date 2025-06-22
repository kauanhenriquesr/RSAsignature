import base64
import sys
from src.verifica_assina import assinatura, verifica
from src.rsa import gera_chave

if __name__ == '__main__':
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    if args == [] or args[0] in ["-h", "--help"]:
        print("RSA - Assinatura Digital")
        print ("="*100)
        print("Uso:\n" \
        "   - python __main__.py -gen_keys\n" \
        "   - python __main__.py -sign <arquivo>\n" \
        "   - python __main__.py -verify <arquivo>\n")
        sys.exit(1)

    elif args[0] == "-gen_keys" and len(args) == 1:
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
        sys.exit(0)

    elif args[0] == "-sign":
        if len(args) != 2:
            print("Uso: python __main__.py -sign <arquivo>")
            sys.exit(1)
        file_path = args[1]
        try: n = int(open("assets/n.key").read())
        except FileNotFoundError:
            print(f"Arquivo de N {file_path} não encontrado. Por favor, gere as chaves primeiro.\n" \
                  " - Se você não gerou as chaves, execute:\n" \
                  "   python __main__.py -gen_keys")
            sys.exit(1)
        try: private_key = int(open("assets/private_key.key").read())
        except FileNotFoundError:
            print(f"Arquivo de chave privada {file_path} não encontrado. Por favor, gere as chaves primeiro.")
            sys.exit(1)
        try:
            assinatura = assinatura(file_path, n, private_key)
            print("Assinatura gerada com sucesso!")
            print("Assinatura:", assinatura)
            with open("assets/assinatura.sig", "w") as f:
                f.write(assinatura)
                print("Assinatura salva em assets/assinatura.sig com sucesso!")
            sys.exit(0)
        except FileNotFoundError:
            print(f"Arquivo {file_path} não encontrado.")
            sys.exit(1)
    
    elif args[0] == "-verify":
        if len(args) != 3:
            print("Uso: python __main__.py -verify <arquivo> <assinatura>")
            sys.exit(1)
        file_path = args[1]
        assinatura_file = args[2]
        try: assinatura = open(assinatura_file).read()
        except FileNotFoundError:
            print(f"Arquivo de assinatura {assinatura_file} não encontrado. Por favor, gere uma assinatura primeiro.")
            sys.exit(1)

        try: n = int(open("assets/n.key").read())
        except FileNotFoundError:
            print(f"Arquivo de N não encontrado. Por favor, gere as chaves primeiro.")
            sys.exit(1)

        try: public_key = int(open("assets/public_key.key").read())
        except FileNotFoundError:
            print(f"Arquivo de chave pública não encontrado. Por favor, gere as chaves primeiro.")
            sys.exit(1)
        
        try:
            if verifica(file_path, assinatura, n, public_key):
                print("Assinatura verificada com sucesso!")
                sys.exit(0)
            else:
                print("Assinatura inválida ou não corresponde ao arquivo.")
                sys.exit(0)
        except AssertionError as e:
            print(f"Erro ao verificar a assinatura: {e}")
            sys.exit(1)
