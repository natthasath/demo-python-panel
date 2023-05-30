import ptvsd
import param
import panel as pn

ptvsd.enable_attach(address=("localhost", 5678))
ptvsd.wait_for_attach()

def action(event):
    print("Nice to be here!")

class App(param.Parameterized):
    action = param.Action(default=action)

    def view(self):
        return pn.Column(pn.pane.Markdown("# Hello Panel World"), self)
    
app = App()
app.view().servable()