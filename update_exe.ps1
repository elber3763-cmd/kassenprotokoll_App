# update_exe.ps1
# Laedt die neueste kassenprotokoll.exe von GitHub Releases
# und speichert sie im aktuellen Verzeichnis.

$repo    = "elber3763-cmd/kassenprotokoll_App"
$outFile = Join-Path $PSScriptRoot "kassenprotokoll.exe"

Write-Host "Suche neueste Version auf GitHub..." -ForegroundColor Cyan

try {
    $release = Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/releases/latest" -UseBasicParsing
    $asset   = $release.assets | Where-Object { $_.name -eq "kassenprotokoll.exe" } | Select-Object -First 1

    if (-not $asset) {
        Write-Host "FEHLER: Keine kassenprotokoll.exe im neuesten Release gefunden." -ForegroundColor Red
        pause; exit 1
    }

    $version = $release.tag_name
    $sizeMB  = [math]::Round($asset.size / 1MB, 1)
    Write-Host "Version $version gefunden ($sizeMB MB). Download startet..." -ForegroundColor Green

    Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $outFile -UseBasicParsing

    Write-Host ""
    Write-Host "Fertig! kassenprotokoll.exe wurde aktualisiert." -ForegroundColor Green
    Write-Host "Gespeichert unter: $outFile" -ForegroundColor Gray
} catch {
    Write-Host "FEHLER: $($_.Exception.Message)" -ForegroundColor Red
}

pause
