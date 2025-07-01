import gradio as gr

def add(num1, num2):
    return num1 + num2

interface = gr.Interface(
    fn = add,
    inputs = ['number', 'number'],
    outputs = 'number',
    title = '계산기',
    description = '숫자 두 개를 입력하세요',
    flagging_mode = "never" # flag를 하지 않음. 근데 이게 내 버전에서는 안되는걸로 챗지피티가 그럼.
)

interface.launch()