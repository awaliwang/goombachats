from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. In venenatis mi ac luctus laoreet. Pellentesque suscipit odio eu ligula bibendum, tempor cursus sem placerat. Integer hendrerit pellentesque consequat. Praesent a nisi non dolor sodales feugiat. Fusce tempus ligula dolor, eget hendrerit lorem aliquet nec. Nam convallis elementum purus eget bibendum. In quam sem, auctor non auctor eu, maximus vel mauris. Nullam bibendum massa sed elementum egestas. Suspendisse tincidunt lectus vitae libero ullamcorper eleifend. Donec sodales, lorem dapibus euismod viverra, sem justo viverra purus, ac ultrices lectus leo et nisi. Mauris eget lacus velit. Fusce nec urna sed eros molestie condimentum. Vivamus tristique sagittis nunc at ultricies. Pellentesque dictum lacus sed tincidunt consequat. Donec egestas laoreet elit, ut efficitur nibh maximus eget. Proin justo lorem, commodo quis sapien ac, faucibus imperdiet felis.",
        "Bacon ipsum dolor amet ham meatloaf chicken tenderloin pork belly beef ribs. Short ribs pastrami pork loin tongue shoulder filet mignon t-bone. Ham spare ribs boudin, salami cow ground round fatback landjaeger leberkas. Pig shoulder pastrami frankfurter hamburger buffalo shankle capicola chislic salami shank chuck meatloaf. Flank ground round bacon pig ham. Hamburger short ribs frankfurter capicola shank kielbasa spare ribs ground round corned beef meatball cow filet mignon turducken sirloin.",
        "I love cheese, especially cheesecake caerphilly. Fromage frais cheese and biscuits stinking bishop say cheese squirty cheese cheesy grin manchego edam. Caerphilly emmental st. agur blue cheese port-salut manchego paneer the big cheese camembert de normandie. Blue castello cheese on toast st. agur blue cheese pepper jack."]

@app.route("/lorem_ipsum")
def lorem_ipsum():
    return texts[0]

@app.route("/bacon_ipsum")
def bacon_ipsum():
    return texts[1]

@app.route("/cheese_ipsum")
def cheese_ipsum():
    return texts[2]

@app.route("/page_test")
def page_test():
    return render_template('test.html')
