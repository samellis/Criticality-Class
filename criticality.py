import matplotlib.pyplot as plt


def get_criticality_class(max_temperature_synthesis_reaction, td24, max_technical_temp):
    """
    Determines the Stoessel criticality class of a process.

    Assumes that temperature of process (Tp) is below all other temps.

    Arguments:
        max_temperature_synthesis_reaction: (MTSR) maximum temperature (in C) of the synthesis reaction
        td24: temperature (in C) at which TMRad is 24 h
        max_technical_temp: (MTT) maximum temperature (in C) for technical reasons

    Returns:
        criticality class (int): 1-5
    """
    if max_temperature_synthesis_reaction < td24:
        # MTSR is < TD24, process is class 1-3
        if max_technical_temp > td24:
            return 2
        else:
            if max_technical_temp > max_temperature_synthesis_reaction:
                return 1
            else:
                return 3
    else:
        # MTSR is >= TD24, process is class 4-5
        if max_technical_temp > max_temperature_synthesis_reaction:
            return 5
        else:
            return 4


def plot_class(
    process_temperature, max_temperature_synthesis_reaction, td24, max_technical_temp
):
    """
    Generates a Stoessel criticality plot for a process.

    Arguments:
        process_temperature: (Tp) temperature of process (in C)
        max_temperature_synthesis_reaction: (MTSR) maximum temperature (in C) of the synthesis reaction
        td24: temperature (in C) at which TMRad is 24 h
        max_technical_temp: (MTT) maximum temperature (in C) for technical reasons

    Returns:
        plot (matplotlib.pyplot)
    """
    fig, ax = plt.subplots(figsize=(3, 6))

    # plt.ylabel("Temperature")
    max_y_value = max(
        process_temperature,
        max_temperature_synthesis_reaction,
        td24,
        max_technical_temp,
    )
    ax.set_ylim(top=max_y_value * 1.2)
    ax.set_xlim(left=0, right=1)
    ax.xaxis.set_ticks([])
    ax.set_xlabel(
        "Criticality Class "
        + str(
            get_criticality_class(
                max_temperature_synthesis_reaction, td24, max_technical_temp
            )
        )
    )
    ax.set_ylabel("Temperature")
    plt.axhline(y=process_temperature, color="green")
    plt.annotate(
        "Tp",
        xy=(0.5, process_temperature + 1),
        color="green",
        weight="bold",
        ha="center",
    )

    plt.axhline(y=max_temperature_synthesis_reaction, color="blue")
    plt.annotate(
        "MTSR",
        xy=(0.5, max_temperature_synthesis_reaction + 1),
        color="blue",
        weight="bold",
        ha="center",
    )

    plt.axhline(y=max_technical_temp, color="brown")
    plt.annotate(
        "MTT",
        xy=(0.5, max_technical_temp + 1),
        color="brown",
        weight="bold",
        ha="center",
    )

    plt.axhline(y=td24, color="red", linestyle="-")
    plt.annotate("TD24", xy=(0.5, td24 - 7), color="red", weight="bold", ha="center")

    plt.fill_between(x=(0, 1), y1=td24, y2=300, facecolor="red", hatch="/")

    plt.tight_layout()
    plt.show()
    return plt


# Class 4 example:
# plot_class(100, 190, 150, 120)

# Class 1 example:
# plot_class(100, 120, 200, 140)
