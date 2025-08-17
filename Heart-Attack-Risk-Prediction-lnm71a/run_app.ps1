Write-Host "Starting Heart Attack Risk Prediction Application..." -ForegroundColor Green
Write-Host ""
Write-Host "Using virtual environment: harp" -ForegroundColor Yellow
Write-Host ""
Write-Host "Starting Flask application..." -ForegroundColor Cyan
Write-Host ""
Write-Host "The application will be available at: http://127.0.0.1:5000" -ForegroundColor Magenta
Write-Host ""
Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Red
Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

try {
    & ".\harp\Scripts\python.exe" "app.py"
}
catch {
    Write-Host "Error running the application: $_" -ForegroundColor Red
    Write-Host "Press any key to exit..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
