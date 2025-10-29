import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent
sys.path.append(str(ROOT_DIR))

# Adiciona o diretório da aula07 ao sys.path para permitir imports locais
AULA07 = ROOT_DIR / "Modulo_03" / "aula07"
if AULA07.exists():
	path_aula07 = str(AULA07)
	if path_aula07 not in sys.path:
		# Inserir no início para ter prioridade sobre outros módulos
		sys.path.insert(0, path_aula07)