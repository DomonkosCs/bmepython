# ezzel egyelőre ne foglalkozzunk
from IPython.display import display, HTML

def create_meme(text):
    code = f"""
    <div style="position: relative; width: 50%;">
        <img src="./spongebob.png" style="display: block;">
        <p style="position: absolute; bottom: 0%; left: 50%; transform: translate(-50%, -50%); color: white;-webkit-text-stroke: 1px black;  font-size: 24px; font-weight: bold; margin: 0; width: 80%">
            {text}
        </p>
</div>
    """
    display(HTML(code))