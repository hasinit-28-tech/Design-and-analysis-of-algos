
# Divide & Conquer closest pair algorithm (2D points)

import math
from typing import List, Tuple
Point = Tuple[float, float]
def _dist(a: Point, b: Point) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])

def closest_pair(points: List[Point]) -> Tuple[Point, Point, float]:
    if len(points) < 2:
        raise ValueError("Need at least 2 points")
    px = sorted(points, key=lambda p: (p[0], p[1]))  # by x
    py = sorted(points, key=lambda p: (p[1], p[0]))  # by y
    def _closest(px: List[Point], py: List[Point]):
        n = len(px)
        if n <= 3:
            # brute force
            best = (None, None, float('inf'))
            for i in range(n):
                for j in range(i+1, n):
                    d = _dist(px[i], px[j])
                    if d < best[2]:
                        best = (px[i], px[j], d)
            return best
            
        mid = n // 2
        midx = px[mid][0]
        Qx = px[:mid]
        Rx = px[mid:]
        # split py into Qy and Ry preserving order
        Qy = []
        Ry = []
        for p in py:
            if p[0] <= midx:
                Qy.append(p)
            else:
                Ry.append(p)
        (p1l, p2l, dl) = _closest(Qx, Qy)
        (p1r, p2r, dr) = _closest(Rx, Ry)
        if dl <= dr:
            dmin = dl
            pair = (p1l, p2l)
        else:
            dmin = dr
            pair = (p1r, p2r)
        strip = [p for p in py if abs(p[0] - midx) < dmin]
        # Compare each point to next up to 7 points
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < dmin:
                d = _dist(strip[i], strip[j])
                if d < dmin:
                    dmin = d
                    pair = (strip[i], strip[j])
                j += 1

        return pair[0], pair[1], dmin

    a, b, d = _closest(px, py)
    return a, b, d


