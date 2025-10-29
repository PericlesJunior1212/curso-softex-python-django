Como rodar os testes (Windows / PowerShell)

1) Ativar o ambiente virtual (.venv) (opcional — o script já faz isso):

```powershell
cd C:\Git\curso-softex-python-django
. .\.venv\Scripts\Activate.ps1
```

Se ocorrer erro por política de execução (ExecutionPolicy), rode apenas para a sessão atual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
. .\.venv\Scripts\Activate.ps1
```

2) Rodar pytest (após ativar o venv):

```powershell
pytest -v
```

3) Alternativa (sem ativar o venv):

```powershell
C:/Git/curso-softex-python-django/.venv/Scripts/python.exe -m pytest -v
```

4) Script conveniente (executa ativação e pytest automaticamente):

```powershell
cd C:\Git\curso-softex-python-django
.\run_tests.ps1
```

Notas
- Recomendo usar o venv do projeto para evitar instalar pacotes globalmente.
- Se preferir, crie um novo venv com `python -m venv .venv` na raiz e instale as dependências do `requirements.txt`.
