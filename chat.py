import ptvsd
import param
import panel as pn

ptvsd.enable_attach(address=("localhost", 5678))
ptvsd.wait_for_attach()

panels = [] # collect display 
context = []  # accumulate messages
inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))

    return pn.Column(*panels)

def get_completion_from_messages(messages):
    return messages

def action(event):
    print("Nice to be here!")

class App(param.Parameterized):
    action = param.Action(default=action)

    def view(self):
        pn.extension()
        button_conversation = pn.widgets.Button(name="Chat!")
        interactive_conversation = pn.bind(collect_messages, button_conversation)
        dashboard = pn.Column(
            inp,
            pn.Row(button_conversation),
            pn.panel(interactive_conversation, loading_indicator=True, height=300),
        )
        return dashboard
    
app = App()
app.view().servable()