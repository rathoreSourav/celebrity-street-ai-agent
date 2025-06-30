import random
from generator.gpt_funny_line import generate_funny_line

celebrities = [
    "Cristiano Ronaldo", "Taylor Swift", "Elon Musk", "Shah Rukh Khan",
    "Beyoncé", "Narendra Modi", "Kanye West", "Virat Kohli", "Emma Watson"
]

activities = [
    "pani puri bech raha hai", "rickshaw chala raha hai", "chai serve kar raha hai",
    "cycle repair kar raha hai", "street pe dance kar raha hai", "gulab jamun tal raha hai"
]

locations = [
    "Chandni Chowk ke kone pe", "Bandra station ke paas", "Marine Drive par",
    "Old Delhi ke signal pe", "Lajpat Nagar market mein", "Versova beach par"
]

def generate_prompt_and_caption():
    celeb = random.choice(celebrities)
    act = random.choice(activities)
    loc = random.choice(locations)

    veo_prompt = f"{celeb} {act} {loc}, cinematic, cartoonish, funny tone"
    funny_line = generate_funny_line(celeb, act, loc)
    caption = f"{celeb} {act} {loc} 😂\n🗣️ {funny_line}"

    return veo_prompt, funny_line, caption
