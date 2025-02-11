import gradio as gr
from audio import transcribe_with_whisper
from chat import chat


# Function to handle user text input
def do_entry(message, history):
    history += [{"role": "user", "content": message}]
    return "", history


# Function to handle audio input and update chatbot history
def handle_audio_input(audio, history):
    transcribed_text = transcribe_with_whisper(audio)  # Get transcribed text
    history += [{"role": "user", "content": transcribed_text}]  # Add it to the conversation history

    # Now call the chat function with updated history
    history, image ,audio_output= chat(history)  # Call chat method and return history and image



    return history, image,audio_output  # Directly return updated history to chat (no need for textbox update)

def create_ui():
    css = """
    body { background-color: #121212; color: #e0e0e0; font-family: Arial, sans-serif; }
    .gradio-container { background-color: #121212; }
    header { text-align: center; font-size: 24px; font-weight: bold; color: #e0e0e0; padding: 20px; }
    .gradio-chatbot .message { background-color: #333; color: #e0e0e0; }
    .gradio-image .image { background-color: #333; border: 1px solid #444; }
    .gradio-input, .gradio-button { background-color: #333; color: #e0e0e0; border: 1px solid #555; }
    """
    with gr.Blocks(css=css) as ui:
        gr.HTML("<header> Chat Interface</header>")
        with gr.Row():
            chatbot = gr.Chatbot(height=500, type="messages")
            image_output = gr.Image(height=500)
        with gr.Row():
            audio_input = gr.Audio(sources=["microphone"], type="filepath", streaming=True,  show_label=False )
            audio_output = gr.Audio(
                label="Assistant's Voice",
                autoplay=True,
                type="filepath"
            )

        audio_input.change(
            handle_audio_input,
            inputs=[audio_input, chatbot],
            outputs=[chatbot, image_output,audio_output]  # Add audio_input to outputs
        )
        return ui


