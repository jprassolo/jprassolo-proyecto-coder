import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph_for_dashboard():
    # Create a new figure and plot some data
    plt.figure()
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.plot(x, y)

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')


def get_graph_for_dashboard2():
    # Create a new figure and plot some data
    manzanas = [20,10,25,30]
    nombres = ["Acciones","Bonos","Crypto","CEDEARS"]
    colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
    plt.pie(manzanas, labels=nombres, autopct="%0.1f %%", colors=colores)
    plt.axis("equal")
    plt.gcf()
    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')