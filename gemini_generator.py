def generate_document(self, document_type, parties, terms, dates):
    prompt = (
        f"Generate a comprehensive legal document titled '{document_type}'\n"
        f"Involved parties: {parties}\n"
        f"Effective Date: {dates}\n"
        f"Terms and conditions: {terms}\n"
        f"Ensure formal legal structure with multiple sections and legal clauses."
    )
    response = self.model.generate_content(prompt)
    return response.text
    # gemini_generator.py
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

self.model = genai.GenerativeModel(model_name)
response = self.model.generate_content(prompt)
```[cite: 3]
