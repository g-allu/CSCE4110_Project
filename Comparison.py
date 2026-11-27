def print_table(headers, rows):
    # Make each column as wide as its longest entry
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    line = "+-" + "-+-".join("-" * w for w in widths) + "-+"
    print(line)
    print("| " + " | ".join(h.ljust(w) for h, w in zip(headers, widths)) + " |")
    print(line)
    for row in rows:
        print("| " + " | ".join(str(c).ljust(w) for c, w in zip(row, widths)) + " |")
    print(line)


def preview(data, limit=20):
    # Show short lists in full; for long ones show the ends so the screen isn't flooded
    if len(data) <= limit:
        return str(data)
    head = ", ".join(str(x) for x in data[:5])
    tail = ", ".join(str(x) for x in data[-5:])
    return f"[{head}, ..., {tail}] ({len(data)} items)"
