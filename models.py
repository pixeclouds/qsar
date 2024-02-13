# P-QSAR
def p_qsar(features):
    AATS1v = features[0]
    ATSC4m = features[1]
    MATS2i = features[2]
    GATS2c = features[3]
    JGI9 = features[4]

    Y = (-0.020759410 * AATS1v) - (0.000797609 * ATSC4m) - (6.536140860 * MATS2i) - (1.548259137 * GATS2c) + (141.753846069 * JGI9) + 11.857033728
    return round(Y, 2)


# C-QSAR
def c_qsar(features):
    ATSC6v = features[0]
    VR1_Dzp = features[1]
    VR2_Dzp = features[2]
    SpMin5_Bhp = features[3]
    ETA_dAlpha_B = features[4]

    Y = (-0.000419117 * ATSC6v) + (0.006914343 * VR1_Dzp) - (0.197988304 * VR2_Dzp) - (1.895865090 * SpMin5_Bhp) - (67.605895028 * ETA_dAlpha_B) + 9.171571170

    # Round the result to four decimal places
    Y_rounded = round(Y, 2)
    return Y_rounded
    


