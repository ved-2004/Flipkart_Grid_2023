# from flask import Flask, render_template
# import freeGPT
# from asyncio import run

# import freeGPT
# from asyncio import run




# run(main())

# app = Flask(__name__)

# @app.route('/')
# def index():
#     tImages = [
#         'static/dwImg/1.jpeg',
#         'static/dwImg/2.jpeg',
#         'static/dwImg/3.jpeg',
#         'static/dwImg/4.jpeg',
#         'static/dwImg/5.jpeg',
#         'static/dwImg/6.jpeg',
#         'static/dwImg/7.jpeg',
#         'static/dwImg/8.jpeg',
#         'static/dwImg/9.jpeg',
#         'static/dwImg/10.jpeg',
#         'static/dwImg/11.jpeg',
#         'static/dwImg/12.jpeg',
#         'static/dwImg/13.jpeg',
#         'static/dwImg/14.jpeg',
#     ]
#     return render_template('index.html', tImages = tImages)


# @app.route('/details')
# def details():
#     return render_template('details.html')

# @app.route('/chatui')
# def index():
#     return render_template('chat.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     prompt = request.form['user_input']
#     try:
#         response = run_freegpt(prompt)  # Call the freeGPT chat function
#     except Exception as e:
#         response = f"An error occurred: {e}"
    
#     return response

# def run_freegpt(prompt):
#     # This function uses the freeGPT model to generate a response
#     async def main():
#         try:
#             resp = await freeGPT.Completion.create(prompt)
#             return resp.choices[0].text.strip()
#         except Exception as e:
#             return f"An error occurred: {e}"

#     return run(main())


# if __name__ == '__main__':
#     app.run(debug=True, port= 8000)

from flask import Flask, render_template, request
from freePPT import Completion 
from asyncio import run

app = Flask(__name__)

@app.route('/')
def index():
    tImages = [
        'static/dwImg/1.jpeg',
        'static/dwImg/2.jpeg',
        'static/dwImg/3.jpeg',
        'static/dwImg/4.jpeg',
        'static/dwImg/5.jpeg',
        'static/dwImg/6.jpeg',
        'static/dwImg/7.jpeg',
        'static/dwImg/8.jpeg',
        'static/dwImg/9.jpeg',
        'static/dwImg/10.jpeg',
        'static/dwImg/11.jpeg',
        'static/dwImg/12.jpeg',
        'static/dwImg/13.jpeg',
        'static/dwImg/14.jpeg',
    ]
    return render_template('index.html', tImages=tImages)

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/chat_ui')
def chat_ui():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form['user_input']
    try:
        response = run_completion(prompt)  # Call the freeGPT chat function
    except Exception as e:
        response = f"An error occurred: {e}"
    
    return response


def run_completion(prompt):
    completion = Completion()
    return run(completion.create(prompt))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
