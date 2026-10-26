T_BOUNDS = [-0.45, -0.15, 0.2, 0.55]
H_BOUNDS = [-0.35, -0.1, 0.1, 0.3]
C_BOUNDS = [-1.05, -0.455, -0.19, -0.11, 0.03, 0.3]
E_BOUNDS = [-0.78, -0.375, -0.2225, 0.05, 0.45, 0.55]
PV_BOUNDS = [-0.85, -0.2, 0.2, 0.7]

t = h = c = e = pv = 0      # zone numbers
pos = False                 # True if W>0


def surface():
    if c == 0:
        return "Mushroom Fields"
    if c == 1:
        return ["Deep Frozen Ocean", "Deep Cold Ocean", "Deep Ocean",
                "Deep Lukewarm Ocean", "Warm Ocean"][t]
    if c == 2:
        return ["Frozen Ocean", "Cold Ocean", "Ocean",
                "Lukewarm Ocean", "Warm Ocean"][t]
    return land()


def land():
    global pos
    if pv == 0:
        if e == 6 and c > 3:
            if t > 2:
                return "Mangrove Swamp"
            if t > 0:
                return "Swamp"
            return "Frozen River"
        if e < 2 and c > 4:
            pos = True
            return middle_badlands()
        return rivers()
    if (e == 2 or e == 3) and c > 4:
        if (pv == 2 and c == 6 and e == 2) or (pv > 2 and e == 2) or (pv > 2 and c == 6 and e == 3):
            return plateau()
        return middle_badlands()
    if e < 2:
        if pv == 2 and ((c > 3 and e == 0) or (c == 6 and e == 1)):
            if (t > 2 and e == 0) or (t > 0 and e == 1):
                return plateau()
            if h > 1:
                return "Grove"
            return "Snowy Slopes"
        if (e == 0 and (pv == 4 or (pv == 3 and c > 4))) or (e == 1 and pv == 4 and c > 4):
            return highest_peaks()
        if pv < 3 and c == 3:
            return "Stony Shore"
        if (e == 1 and c > 4 and pv == 3) or (e == 0 and pv == 2) or (e == 0 and pv == 3 and c == 4):
            return expanded_sub_nival()
        if c == 4 and pv == 1:
            return middle_badlands()
        if c == 3 and pv == 3:
            return middle()
        return sub_nival()
    if e < 4:
        if e == 2 and c == 3 and pv < 3:
            return "Stony Shore"
        if e == 3 and c == 3 and pv == 1:
            return beach()
        return middle()
    if c == 3:
        if e == 5 and pos and t > 1 and h < 4:
            return "Windswept Savanna"
        if (pv < 3 and not pos) or (pv == 1 and (e == 4 or e == 6)):
            return beach()
        if e == 5 and pv == 4:
            return shattered()
        return middle()
    if t > 0 and e == 6 and pv < 3 and c > 3:
        if t > 2:
            return "Mangrove Swamp"
        return "Swamp"
    if e == 5 and pv > 1 and c > 4:
        return shattered()
    if e == 5 and c == 4 and pos and t > 1 and h < 4:
        return "Windswept Savanna"
    if e == 5 and pv == 4:
        return shattered()
    return middle()


def rivers():
    if t == 0:
        return "Frozen River"
    return "River"


def middle_badlands():
    if t == 4:
        return badlands()
    return middle()


def badlands():
    if h > 2:
        return "Wooded Badlands"
    if h < 2 and pos:
        return "Eroded Badlands"
    return "Badlands"


def middle():
    if t == 4:
        return "Desert"
    if t == 0:
        if h == 4:
            return "Taiga"
        if h == 2 and pos:
            return "Snowy Taiga"
        return snowy()
    if t == 3:
        if h < 2:
            return "Savanna"
        if h == 2:
            if pos:
                return "Plains"
            return "Forest"
        if pos:
            if h == 3:
                return "Sparse Jungle"
            return "Bamboo Jungle"
        return "Jungle"
    if h == 1:
        return "Plains"
    if h == 2:
        return "Forest"
    if h == 0:
        if pos:
            if t == 1:
                return "Dappled Forest"
            return "Sunflower Plains"
        if t == 1:
            return "Plains"
        return "Flower Forest"
    if t == 1:
        if h == 3:
            return "Taiga"
        if pos:
            return "Old Growth Pine Taiga"
        return "Old Growth Spruce Taiga"
    if h == 4:
        return "Dark Forest"
    if pos:
        return "Old Growth Birch Forest"
    return "Birch Forest"


def beach():
    if t == 0:
        return "Snowy Beach"
    if t == 4:
        return "Desert"
    return "Beach"


def snowy():
    if h > 2:
        return "Snowy Taiga"
    if h > 0:
        return "Snowy Plains"
    if pos:
        return "Ice Spikes"
    return "Snowy Plains"


def plateau():
    if t == 4:
        return badlands()
    if t == 0:
        return snowy()
    if t == 3:
        if h < 2:
            return "Savanna Plateau"
        if h < 4:
            return "Forest"
        return "Jungle"
    if h == 4:
        if t == 2:
            return "Pale Garden"
        if pos:
            return "Old Growth Pine Taiga"
        return "Old Growth Spruce Taiga"
    if t == 2 and pos:
        if h < 2:
            return "Cherry Grove"
        if h == 2:
            return "Forest"
        return "Birch Forest"
    if t == 1 and h == 0 and pos:
        return "Cherry Grove"
    if t == 1 and h == 2 and not pos:
        return "Forest"
    if t == 1 and h == 3 and not pos:
        return "Taiga"
    return "Meadow"


def shattered():
    if t == 4:
        return "Desert"
    if t == 3:
        if h < 2:
            return "Savanna"
        if h == 2:
            if pos:
                return "Plains"
            return "Forest"
        if pos:
            if h == 4:
                return "Bamboo Jungle"
            return "Sparse Jungle"
        return "Jungle"
    if h > 2:
        return "Windswept Forest"
    if h < 2 and t < 2:
        return "Windswept Gravelly Hills"
    return "Windswept Hills"


def highest_peaks():
    if t == 4:
        return badlands()
    if t == 3:
        return "Stony Peaks"
    if pos:
        return "Frozen Peaks"
    return "Jagged Peaks"


def sub_nival():
    if t == 4:
        return badlands()
    if t == 0:
        if h < 2:
            return "Snowy Slopes"
        return "Grove"
    return middle()


def expanded_sub_nival():
    if t > 2:
        return plateau()
    if h < 2:
        return "Snowy Slopes"
    return "Grove"





def zone(value, bounds):      # For loop finds zone from decimal
    z = 0
    for b in bounds:
        if value > b:
            z = z + 1
    return z


def ask(name, bounds):
    mode = input(name + ": 1 = zone number, 2 = decimal value: ")
    if mode == "1":
        return int(input("  zone number: "))
    return zone(float(input("  decimal value: ")), bounds)


while True:
    print()
    t = ask("T", T_BOUNDS)
    h = ask("H", H_BOUNDS)
    c = ask("C", C_BOUNDS)
    e = ask("E", E_BOUNDS)

    mode = input("Weirdness: 1 = PV zone number, 2 = decimal W value: ")
    if mode == "1":
        pv = int(input("  PV zone number: "))
        pos = input("  sign (p/n): ") == "p"
    else:
        w = float(input("  decimal W value: "))
        if abs(w) * 15 > 13.9999999:      # |W|>14/15 forces PV2 zone
            pv = 2
        else:
            pv = zone(1 - abs(3 * abs(w) - 2), PV_BOUNDS)
        if w == 0:
            pos = input("  sign (p/n): ") == "p"
        else:
            pos = w > 0

    print("Biome:", surface())
