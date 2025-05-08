import gradio as gr
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="GEMINI_API_KEY")  # Replace with your actual key
model = genai.GenerativeModel('models/gemini-1.5-pro')

# Function 1: Summarize Text
def summarize_text(text):
    prompt = f"Summarize the following Text into 3-5 bullet points:\n\n{text}"
    result = model.generate_content(prompt)
    return result.text.strip()

# Function 2: Rewrite Text
def rewrite_text(text):
    prompt = f"Rewrite the following text in simpler terms:\n\n{text}"
    result = model.generate_content(prompt)
    return result.text.strip()

# Function 3: Generate Text
def generate_text(topic):
    prompt = f"Generate a detailed explanation on the following topic:\n\n{topic}"
    result = model.generate_content(prompt)
    return result.text.strip()

# Function 4: Concept Explanation
def explain_concept(topic):
    prompt = f"Explain {topic} in a simple and easy-to-understand manner."
    result = model.generate_content(prompt)
    return result.text.strip()

# Function 5: Change Tone
def change_tone(text):
    prompt = f"Rewrite the following text to sound more formal and professional:\n\n{text}"
    result = model.generate_content(prompt)
    return result.text.strip()

#Function 6: Tanslate Text
def translate_text(text, target_language):
    prompt = f"Translate the following text to {target_language}:\n\n{text}"
    result = model.generate_content(prompt)
    return result.text.strip()

# Gradio Interface
with gr.Blocks(title="Gemini Tool UI") as demo:
    gr.Markdown("## 🧠 Gemini AI Text Tool")
    gr.Markdown("Choose any of the following AI features:")
    
    with gr.Tab("1️⃣ Summarize Text"):
        input_text = gr.Textbox(label="Enter Text to Summarize", lines=5)
        output = gr.Textbox(label="Summary", lines=5)
        summarize_btn = gr.Button("Summarize")
        summarize_btn.click(fn=summarize_text, inputs=input_text, outputs=output)

    with gr.Tab("2️⃣ Rewrite Text Simply"):
        input_text2 = gr.Textbox(label="Enter Text to Simplify", lines=5)
        output2 = gr.Textbox(label="Rewritten Text", lines=5)
        rewrite_btn = gr.Button("Rewrite")
        rewrite_btn.click(fn=rewrite_text, inputs=input_text2, outputs=output2)
        
    with gr.Tab("3️⃣ Generate Text by Topic"):
        topic = gr.Textbox(label="Enter Topic", lines=1)
        output3 = gr.Textbox(label="Generated Text", lines=8)
        generate_btn = gr.Button("Generate")
        generate_btn.click(fn=generate_text, inputs=topic, outputs=output3)

    with gr.Tab("4️⃣ Explain Concept Simply"):
        concept = gr.Textbox(label="Enter Concept to Explain", lines=1)
        output4 = gr.Textbox(label="Explanation", lines=6)
        explain_btn = gr.Button("Explain")
        explain_btn.click(fn=explain_concept, inputs=concept, outputs=output4)

    with gr.Tab("5️⃣ Change Tone to Professional"):
        input_text5 = gr.Textbox(label="Enter Casual Text", lines=5)
        output5 = gr.Textbox(label="Professional Text", lines=5)
        tone_btn = gr.Button("Make Professional")
        tone_btn.click(fn=change_tone, inputs=input_text5, outputs=output5)

    with gr.Tab("6️⃣ Translate Text"):
        input_text_translate = gr.Textbox(label="Enter Text to Translate", lines=5)
        target_language = gr.Dropdown(
            ["Gujarati","Hindi","Spanish", "French", "German", "Chinese", "Japanese"],
            label="Target Language"
        )
        output_translate = gr.Textbox(label="Translated Text", lines=5)
        translate_btn = gr.Button("Translate")
        translate_btn.click(fn=translate_text, inputs=[input_text_translate, target_language], outputs=output_translate)

# Launch app
demo.launch()
