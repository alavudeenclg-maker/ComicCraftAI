from app.main import app
from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image

print(app.title)
print(len(generate_outline('demo', 'Alex', 'city', 'adventure', 'comic book').splitlines()))
panels = generate_story('demo', 'Alex', 'city', 'adventure', 'outline')
print(len(panels), panels[0]['panel_number'])
path = generate_image('A heroic pose in a city', 1)
print(path)
