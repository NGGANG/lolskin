# Diretório onde estão localizadas as pastas a serem compactadas
$diretorioBase = "D:\Auta\Trabalho\lolskin\skins"

# Verifica se o diretório base existe
if (Test-Path $diretorioBase -PathType Container) {
    # Lista todas as pastas no diretório base
    $pastas = Get-ChildItem -Path $diretorioBase -Directory

    # Verifica se há pastas para compactar
    if ($pastas.Count -gt 0) {
        foreach ($pasta in $pastas) {
            # Define o nome do arquivo ZIP como o nome da pasta
            $nomeArquivoZip = Join-Path -Path $diretorioBase -ChildPath "$($pasta.Name).zip"

            # Compacta a pasta
            Add-Type -AssemblyName System.IO.Compression.FileSystem
            [System.IO.Compression.ZipFile]::CreateFromDirectory($pasta.FullName, $nomeArquivoZip)

            Write-Host "Pasta '$($pasta.Name)' compactada como '$nomeArquivoZip'"
        }
    } else {
        Write-Host "Não há pastas para compactar em '$diretorioBase'."
    }
} else {
    Write-Host "O diretório '$diretorioBase' não existe."
}
