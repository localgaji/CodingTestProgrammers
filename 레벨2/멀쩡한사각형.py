def solution(w,h):

    if w > h:
        w, h = h, w

    width, height = w, h

    while w != h and w >= 1 and h >= 1:
        h = h - w
        if w > h:
            w, h = h, w

    gcd = w
    w_compact, h_compact = width // gcd, height // gcd

    slope = h_compact / w_compact
    block = 0
    for x in range(1, w_compact):
        block += int(slope * x)
    deleted = h_compact * w_compact - block * 2

    return width * height - deleted * gcd