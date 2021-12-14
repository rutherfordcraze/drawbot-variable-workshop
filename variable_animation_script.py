frames = 60

for frame in range(frames):
    newPage(900, 400)
    frameDuration(1 / 30)
    
    axis_min = 1
    axis_max = 1000
    axis_range = axis_max - axis_min
    
    progress = 2 * pi * frame / frames
    y = (sin(progress) + 1) / 2
    axis = y * axis_range + axis_min
    
    font("NotoSansDisplay-VariableFont_wdth,wght.ttf")
    fontSize(200)
    fontVariations(wght = axis)

    fill(0.2, 0.4, 0.8)
    rect(0, 0, width(), height())
    fill(0.9, 1, 1)

    text(
        "Hello",
        (width() / 2, 132),
        align = "center"
    )

saveImage("animation.gif")

