$pptxPath = (Resolve-Path "EcoSense_AI_Yuva_Yodha_Hackathon_2026.pptx").Path
$outDir = Join-Path (Resolve-Path "scratch").Path "slide_previews"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$ppt = New-Object -ComObject PowerPoint.Application
try {
    $pres = $ppt.Presentations.Open($pptxPath, 1, 0, 0)
    $slideIndex = 1
    foreach ($slide in $pres.Slides) {
        $slideFile = Join-Path $outDir "slide_$slideIndex.png"
        $slide.Export($slideFile, "PNG", 1920, 1080)
        Write-Host "Exported Slide $slideIndex to $slideFile"
        $slideIndex++
    }
    $pres.Close()
}
finally {
    $ppt.Quit()
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
