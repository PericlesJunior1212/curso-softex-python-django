# run_tests.ps1
# Ativa o .venv (se existir) e executa pytest -v.
# Uso: execute este script a partir da raiz do repositório (duplo-clique no PowerShell ou
#       abra o PowerShell na pasta do repo e rode: .\run_tests.ps1)

# Permite execução temporária de scripts nesta sessão
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$Root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$Activate = Join-Path $Root ".venv\Scripts\Activate.ps1"
$Python = Join-Path $Root ".venv\Scripts\python.exe"

if (Test-Path $Activate) {
    Write-Host "Ativando .venv..." -ForegroundColor Cyan
    . $Activate
    Write-Host "Executando pytest..." -ForegroundColor Cyan
    # Usar explicitamente o python do .venv para evitar problemas com launchers
    if (Test-Path $Python) {
        & $Python -m pytest -v
    } else {
        # Se por algum motivo o python do .venv não for encontrado, usar o pytest no PATH
        pytest -v
    }
} elseif (Test-Path $Python) {
    Write-Host ".venv detectado, mas não foi possível ativar (usando python.exe diretamente)" -ForegroundColor Yellow
    & $Python -m pytest -v
} else {
    Write-Error "Ambiente virtual .venv não encontrado na raiz do repositório. Crie um venv ou execute pytest via outro Python."
    exit 1
}
