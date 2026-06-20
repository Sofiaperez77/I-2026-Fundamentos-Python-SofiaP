import gradio

demo= gradio.Blocks()
with demo :
    gradio.Markdown("Resgistro")
    gradio.Textbox(label="Nombre:")
    gradio.Button("Enviar")

demo.launch()