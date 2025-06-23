from src.app import main
import sys

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    sys.exit(main(args))