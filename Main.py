from pytube import YouTube
import gradio as gr


def run(url):
    video = YouTube(url).streams.first().download()
    return video


def load_css():
    with open('style.css', 'r') as file:
        css_content = file.read()
    return css_content


demo = gr.Interface(
    fn=run,
    inputs=['text'],
    outputs=['video'],
    title="YouTube Video Downloader",
    description="Download any video from youtube!",
    thumbnail="https://i.imgur.com/wr8dcrz.jpeg/",
    css=load_css()
)
demo.launch()
