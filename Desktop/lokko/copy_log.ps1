$source = "C:\ProgramData\MySQL\MySQL Server 8.0\Data\DESKTOP-QA5HAO2.log"
$destination = "C:\audit_logs"

while ($true){
    Copy-Item $source -Destination $destination -Force
    Write-Host "Copied at $(Get-Date)" -ForegroundColor Green
    Start-Sleep -Seconds 3
}