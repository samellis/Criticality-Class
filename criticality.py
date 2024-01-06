import matplotlib.pyplot as plt


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


def plot_class(tp, mtsr, td24, mtt):
    fig, ax = plt.subplots(figsize=(3, 6))

    # plt.ylabel("Temperature")
    max_y_value = max(tp, mtsr, td24, mtt)
    ax.set_ylim(top=max_y_value * 1.2)
    ax.set_xlim(left=0, right=1)
    ax.xaxis.set_ticks([])
    ax.set_xlabel("Criticality Class " + str(get_class(tp, mtsr, td24, mtt)))
    ax.set_ylabel("Temperature")
    plt.axhline(y=tp, color="green")
    plt.annotate("Tp", xy=(0.5, tp + 1), color="green", weight="bold", ha="center")

    plt.axhline(y=mtsr, color="blue")
    plt.annotate("MTSR", xy=(0.5, mtsr + 1), color="blue", weight="bold", ha="center")

    plt.axhline(y=mtt, color="brown")
    plt.annotate("MTT", xy=(0.5, mtt + 1), color="brown", weight="bold", ha="center")

    plt.axhline(y=td24, color="red", linestyle="-")
    plt.annotate("TD24", xy=(0.5, td24 - 7), color="red", weight="bold", ha="center")

    plt.fill_between(x=(0, 1), y1=td24, y2=300, facecolor="red", hatch="/")

    plt.tight_layout()
    plt.show()


# Class 4 example:
# plot_class(100, 190, 150, 120)

# Class 1 example:
# plot_class(100, 120, 200, 140)


plot_class(40, 81, 130, 56)
