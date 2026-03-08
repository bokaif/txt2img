# txt2img

A simple Python GUI app that converts text into a series of images.

## Backstory

Back in my high school days, I decided I should probably start reading more books. The thing is, I wasn’t really a book person (and honestly, I still am not). Plus, carrying a physical book everywhere just wasn't practical.

My daily commute took about an hour each way in traffic, which was a lot of dead time. Since my high school only allowed us to carry basic feature phones, I was stuck with a Benco C25 (with a tiny 2.4" display), a phone incapable of reading ebooks. I realized that if I could just convert the text of a book into images that fit my phone's screen, I could flip through the native image gallery and read during my commute.

And that’s how this project started. It takes a text file, chops it up based on the exact dimensions you give it, and spits out a sequence of images.

## Features

- **Simple UI:** Built with Tkinter.
- **Customizable Dimensions:** Set the exact width and height of the images so they perfectly fit whatever screen you're reading on.
- **Styling:** Choose your own background color, text color, and font size.
- **Custom Fonts:** Load your own `.ttf` font files.
- **Bulk Output:** Imports a `.txt` file (or pasted text) and spits out sequentially numbered `.jpg` files into an `Output` folder.

## Installation & Usage

You'll need Python installed. The only external dependency is `Pillow`.

1. Install the required package:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python main.pyw
   ```
