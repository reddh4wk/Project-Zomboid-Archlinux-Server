if (-not $args -contains "--ask") {
    $PRESET = "Testing Grounds"
}
if($PRESET -ne $null){
    $source_file = "$HOME\Zomboid\Sandbox Presets\$PRESET.cfg"
} else {
    $userInput = Read-Host "What is the name of the Sandbox Preset you want to convert?"
    $source_file = "$HOME\Zomboid\Sandbox Presets\$userInput.cfg"
}
$source_variables_file = "C:\Users\damiano\Zomboid\Sandbox Presets\source_variables.txt"
$lines = Get-Content -Path $source_file
$filteredLines = $lines | Where-Object { $_ -notmatch "^\s*(#|$)" }
$filteredLines | Out-File -FilePath $source_variables_file

# Percorsi dei file A e B
$template = "$HOME\Zomboid\Server\servertest_SandboxVars.lua"
$output = "$HOME\Desktop\servertest_SandboxVars.lua"

try {
    Copy-Item -Path $template -Destination $output
    Get-Content $source_variables_file | ForEach-Object {
        $row = $_ -split '='
        if(-not [string]::IsNullOrWhiteSpace($row[1])){
            $variable_name = $row[0] -split '\.'
            if(-not [string]::IsNullOrWhiteSpace($variable_name[1])){
                $name=$variable_name[1]
            } else {
                $name=$variable_name
            }
            $value = $row[1]
            Get-Content $output | ForEach-Object { 
                if ($_ -match "\b$name" -and $_ -notmatch "--"){
                    $_ -replace '(?<==\s).*?(?=,)', $value;
                }
            }
        }
    }
    Write-Host "Your file has been saved here: $output"
} catch {
    Write-Host "An error occurred: $_"
} finally {
    rm $source_variables_file
}
