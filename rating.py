import ptvsd
import param
import panel as pn

ptvsd.enable_attach(address=("localhost", 5678))
ptvsd.wait_for_attach()

def model(n=5):
    return "⭐"*n

def action(event):
    print("Nice to be here!")

class App(param.Parameterized):
    action = param.Action(default=action)

    def view(self):
        pn.extension()
        slider = pn.widgets.IntSlider(value=5, start=1, end=5)
        interactive_model = pn.bind(model, n=slider)
        layout = pn.Column(slider, interactive_model)
        return layout
    
app = App()
app.view().servable()