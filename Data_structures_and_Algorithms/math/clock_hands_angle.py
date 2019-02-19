# just as the clock is divided will add the angle just by adding degrees

def diff(h,m):
    if h==12: h=0
    if m==60: m=0

    h_angle = 0.5*(h*60+m)
    m_angle = 6*m

    angle = abs(h_angle - m_angle)

    angle = min(360-angle, angle)

    return angle