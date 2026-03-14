# update_exe.ps1
# Laedt die neueste kassenprotokoll.exe von GitHub Releases
# und speichert sie im aktuellen Verzeichnis.

$repo    = "elber3763-cmd/kassenprotokoll_App"
$outFile = "O:\kassenprotokoll_App\kassenprotokoll.exe"

# GitHub Personal Access Token (benoetigt fuer private Repos)
# Token erstellen: https://github.com/settings/tokens (Scope: repo)
$token = $env:GITHUB_TOKEN

Write-Host "Suche neueste Version auf GitHub..." -ForegroundColor Cyan

try {
    $headers = @{ "User-Agent" = "kassenprotokoll-updater" }
    if ($token) { $headers["Authorization"] = "token $token" }

    $release = Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/releases/latest" -Headers $headers -UseBasicParsing
    $asset   = $release.assets | Where-Object { $_.name -eq "kassenprotokoll.exe" } | Select-Object -First 1

    if (-not $asset) {
        Write-Host "FEHLER: Keine kassenprotokoll.exe im neuesten Release gefunden." -ForegroundColor Red
        pause; exit 1
    }

    $version = $release.tag_name
    $sizeMB  = [math]::Round($asset.size / 1MB, 1)
    Write-Host "Version $version gefunden ($sizeMB MB). Download startet..." -ForegroundColor Green

    $dlHeaders = @{ "User-Agent" = "kassenprotokoll-updater"; "Accept" = "application/octet-stream" }
    if ($token) { $dlHeaders["Authorization"] = "token $token" }

    Invoke-WebRequest -Uri $asset.url -Headers $dlHeaders -OutFile $outFile -UseBasicParsing

    Write-Host ""
    Write-Host "Fertig! kassenprotokoll.exe wurde aktualisiert." -ForegroundColor Green
    Write-Host "Gespeichert unter: $outFile" -ForegroundColor Gray
} catch {
    Write-Host "FEHLER: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Tipp: GitHub Token als Umgebungsvariable setzen:" -ForegroundColor Yellow
    Write-Host '  $env:GITHUB_TOKEN = "ghp_IhrTokenHier"' -ForegroundColor Yellow
    Write-Host "Dann dieses Skript erneut ausfuehren." -ForegroundColor Yellow
}

pause
