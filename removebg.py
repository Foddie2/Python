from rembg import remove
from PIL import Image

input_path = 'masai.jpg'
output_path = 'masai.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)