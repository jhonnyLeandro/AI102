if (Test-Path .env) {
    Get-Content .env | ForEach-Object {
        # Trim whitespace and skip empty lines or comments
        $line = $_.Trim()
        if ($line -and !$line.StartsWith('#') -and $line -match '=') {
            # Split the line into Key and Value at the first '='
            $key, $value = $line -split '=', 2
            
            # Clean up potential surrounding quotes from the value
            $value = $value.Trim("'").Trim('"')
            
            # Load into the current PowerShell environment session
            [System.Environment]::SetEnvironmentVariable($key.Trim(), $value, [System.EnvironmentVariableTarget]::Process)
        }
    }
} else {
    Write-Warning ".env file not found!"
}
