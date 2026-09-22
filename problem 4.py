




def value_call(quality, operate_level, t):
    if t == 5:
        if quality == 'N':
            return -1500
        elif quality == 'S':
            return -600
        else:
            return -150
    else:
        value, decision = expected_value(quality, operate_level, t)
        return value


def expected_value(quality, operate_level, t):
    if quality == 'N':
        if operate_level == 1:
                c1 = 0
                c2 = 120
                c3 = 200
        elif operate_level == .7:
                c1 = 0
                c2 = 0
                c3 = 80
        elif operate_level == .5:
                c1 = 0
                c2 = 0
                c3 = 0
        options = [
            (c1 + .15 * value_call('N', 1, t+1) + .425 * value_call('A', 1, t+1) + .425 * value_call('S', 1, t+1), 1),
            (c2 + .3 * value_call('N', .7, t+1) + .35 * value_call('A', .7, t+1) + .35 * value_call('S', .7, t+1), .7),
            (c3 + .6 * value_call('N', .5, t+1) + .2 * value_call('A', .5, t+1) + .2 * value_call('S', .5, t+1), .5),
        ]
        return min(options, key=lambda o: o[0])

    elif quality == 'S':
        if operate_level == 1:
            c1 = 0
            c2 = 120
            c3 = 200
        elif operate_level == .7:
            c1 = 0
            c2 = 0
            c3 = 80
        elif operate_level == .5:
            c1 = 0
            c2 = 0
            c3 = 0

        options = [
            (c1 + .05 * value_call('N', 1, t+1) + .1 * value_call('A', 1, t+1) + .85 * value_call('S', 1, t+1), 1),
            (c2 + .1 * value_call('N', .7, t+1) + .2 * value_call('A', .7, t+1) + .7 * value_call('S', .7, t+1), .7),
            (c3 + .2 * value_call('N', .5, t+1) + .4 * value_call('A', .5, t+1) + .4 * value_call('S', .5, t+1), .5),
        ]
        return min(options, key=lambda o: o[0])
    elif quality == 'A':
        if operate_level == 1:
            c1 = 0
            c2 = 120
            c3 = 200
        elif operate_level == .7:
            c1 = 0
            c2 = 0
            c3 = 80
        elif operate_level == .5:
            c1 = 0
            c2 = 0
            c3 = 0
        options = [
            (c1 + .2875 * value_call('N', 1, t+1) + .2875 * value_call('A', 1, t+1) + .425 * value_call('S', 1, t+1), 1),
            (c2 + .325 * value_call('N', .7, t+1) + .325 * value_call('A', .7, t+1) + .35 * value_call('S', .7, t+1), .7),
            (c3 + .4 * value_call('N', .5, t+1) + .4 * value_call('A', .5, t+1) + .2 * value_call('S', .5, t+1), .5),
        ]
        return min(options, key=lambda o: o[0])

def recursive_print(quality, operate_level, t, indent=0):
    if t == 5:
        return
    value, decision = expected_value(quality, operate_level, t)
    print('  ' * indent + f"week {t}: quality={quality} level={operate_level} -> decision={decision}")
    for next_quality in ['N', 'A', 'S']:
        recursive_print(next_quality, decision, t + 1, indent + 1)


if __name__ == '__main__':
    recursive_print('N', 1, 1)
