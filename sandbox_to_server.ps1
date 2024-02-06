if (-not $args -contains "--ask") {
    $PRESET = "Testing Grounds"
}
if ($PRESET -ne $null) {
    $source_file = "$HOME\Zomboid\Sandbox Presets\$PRESET.cfg"
} else {
    $userInput = Read-Host "What is the name of the Sandbox Preset you want to convert?"
    $source_file = "$HOME\Zomboid\Sandbox Presets\$userInput.cfg"
}
$source_variables_file = "C:\Users\damiano\Zomboid\Sandbox Presets\source_variables.txt"
$lines = Get-Content -Path $source_file
$filteredLines = $lines | Where-Object { $_ -notmatch "^\s*(#|$)" }
$filteredLines | Out-File -FilePath $source_variables_file -Encoding UTF8

# Percorsi dei file A e B
$template = "$HOME\Zomboid\Server\servertest_SandboxVars.lua"
$output = "$HOME\Desktop\servertest_SandboxVars.lua"

try {
    $content = Get-Content $template
    Get-Content $source_variables_file | ForEach-Object {
        $row = $_ -split '='
        if (-not [string]::IsNullOrWhiteSpace($row[1])) {
            $variable_name = $row[0] -split '\.'
            if (-not [string]::IsNullOrWhiteSpace($variable_name[1])) {
                $name = $variable_name[1]
            } else {
                $name = $variable_name
            }
            $value = $row[1]
            $utf8NoBom = New-Object System.Text.UTF8Encoding $false
            [System.IO.File]::WriteAllLines($output, (Get-Content $template | ForEach-Object {
                if ($_ -match "\b$name" -and $_ -notmatch "--" -and $_ -notmatch "WorldItemRemovalList") {
                    $_ -replace ' (?<==\s).*?(?=,)', $value
                } else {
                    $_
                }
            }), $utf8NoBom)
            Write-Host "Your file has been saved here: $output"
        }
    }
} catch {
    Write-Host "An error occurred: $_"
} finally {
    Remove-Item $source_variables_file
}
