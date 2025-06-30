
from generator.prompt_generator import generate_prompt_and_caption
from datetime import date

def run():
    today = date.today().strftime("%Y-%m-%d")
    for i in range(3):
        veo_prompt, voice_line, caption = generate_prompt_and_caption()
        print(f"\n🎬 Video {i+1} — {today}")
        print(f"🎞️ Gemini Prompt:\n{veo_prompt}")
        print(f"🎤 Voice Line:\n{voice_line}")
        print(f"📢 Caption:\n{caption}")
        print(f"📌 Tags: #GeminiVeo #FunnyAI #StreetCelebs #FYP")

if __name__ == "__main__":
    run()
