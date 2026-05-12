from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        self.expression = ""

        layout = GridLayout(cols=4, padding=10, spacing=10)

        self.input_box = TextInput(
            text="",
            multiline=False,
            readonly=True,
            halign="right",
            font_size=32
        )

        layout.add_widget(self.input_box)

        buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+'
        ]

        for button in buttons:
            btn = Button(text=button, font_size=24)
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)

        clear_btn = Button(text="C", font_size=24)
        clear_btn.bind(on_press=self.clear)
        layout.add_widget(clear_btn)

        return layout

    def on_button_press(self, instance):
        current = instance.text

        if current == "=":
            try:
                self.input_box.text = str(eval(self.expression))
                self.expression = self.input_box.text
            except:
                self.input_box.text = "Error"
                self.expression = ""
        else:
            self.expression += current
            self.input_box.text = self.expression

    def clear(self, instance):
        self.expression = ""
        self.input_box.text = ""

CalculatorApp().run()
