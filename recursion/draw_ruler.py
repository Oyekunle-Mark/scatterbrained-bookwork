def draw_line(tick_length, tick_label=" "):
    line = "-" * tick_length

    if tick_label:
        line += " " + tick_label

    print(line)


def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)
