def draw_line(tick_length, tick_label=" "):
    line = "-" * tick_length

    if tick_label:
        line += " " + tick_label

    print(line)
