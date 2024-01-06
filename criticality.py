# Tp
process_temperature = 100

# MTSR
max_temp_synth_reaction = 120

# td24
td_24 = 150

# mtt
max_temp_technical = 130


def get_class(tp, mtsr, td24, mtt):
    if mtsr < td24:
        # class 1-3
        if mtt > td24:
            return 2
        else:
            if mtt > mtsr:
                return 1
            else:
                return 3
    else:
        # mtsr is > TD24, must be class 4 or 5
        if mtt > mtsr:
            return 5
        else:
            return 4


print(get_class(100, 190, 150, 200))
