import matplotlib.pyplot as plt
def show_graph(obsevation):
    targets = []
    for obs in observations:
        targets.append(obs.target)
    et =[]
    for obs in observations:
        et.append(obs.exposure)
    plt.bar(targets, et)
    plt.xlabel("target name")
    plt.ylabel("exposure_time(second)")
    plt.title("target vs exposure")
    plt.show()