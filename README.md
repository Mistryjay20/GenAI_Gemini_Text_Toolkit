# 🧠 GenAI Gemini Text Toolkit

**GenAI_Gemini_Text_Toolkit** is an interactive and powerful AI-powered text utility app built using **Google's Gemini 1.5 Pro API** and **Gradio**. It provides users with advanced natural language tools such as summarization, rewriting, concept explanation, tone adjustment, and translation—all from a single intuitive interface.

---

## 🚀 Features

| Feature                         | Description |
|----------------------------------|-------------|
| 🔍 **Summarize Text**           | Condenses long-form content into 3–5 bullet points. |
| ✏️ **Rewrite Text Simply**     | Simplifies complex or technical text into plain language. |
| 📘 **Generate Text by Topic**   | Produces detailed content on user-provided topics. |
| 💡 **Explain Concept Clearly** | Explains topics in an easy-to-understand manner. |
| 🧑‍💼 **Change Tone to Formal** | Converts casual/informal writing to a professional tone. |
| 🌐 **Translate Text**          | Translates input text into multiple global languages. |

---

## 🛠️ Tech Stack

- 🔮 **Google Gemini 1.5 Pro** for AI text generation
- 🎨 **Gradio** for frontend interface and interaction
- 🐍 Python 3.10+

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/GenAI_Gemini_Text_Toolkit.git
cd GenAI_Gemini_Text_Toolkit
pip install -r requirements.txt
```

### `requirements.txt`

```txt
gradio
google-generativeai
```

---

## 🔑 Gemini API Setup

1. Go to [Google AI Studio](https://makersuite.google.com/app) and sign in.
2. Create a project and generate an API key.
3. Open the code and replace the placeholder key with your actual API key:

```python
genai.configure(api_key="your_api_key_here")
```

> ⚠️ **Warning:** Never expose your real API key in public codebases. Use `.env` files or environment variables for security.

---

## 💻 Run the App

Start the Gradio interface:

```bash
python app.py
```

Visit `http://localhost:7860` in your browser.

---

## 🖼️ Interface Preview

> *(Add a screenshot of the running interface here for visual context)*

---

## 🧪 Example Use Cases

- ✨ Summarize meeting notes
- 📝 Rewrite complex documentation
- 🎓 Explain physics or tech topics in simple terms
- 🌍 Translate blog content into multiple languages
- 📢 Make job applications sound more professional

---

## 📂 Project Structure

```
├── app.py              # Main application code
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## 🧠 Code Example

Here’s how the summarization function works:

```python
def summarize_text(text):
    prompt = f"Summarize the following Text into 3-5 bullet points:\n\n{text}"
    result = model.generate_content(prompt)
    return result.text.strip()
```

All other functions follow a similar pattern with specialized prompts.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author: JayKumar Pravinbhai Mistry

- [Your Name](https://github.com/yourusername)
