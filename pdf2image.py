import subprocess

def convert_pdf_to_image(pdf_path, output_path):
    command = ['convert', '-density', '300', pdf_path, output_path]
    subprocess.run(command)

pdf_file = 'example.pdf'  # Path to your PDF file
output_image = 'output.jpg'  # Path to the output image file

convert_pdf_to_image(pdf_file, output_image)
