import pyautogui
import os
import time
import pandas

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.PAUSE = 0.5
#passos para acesso ao site

#entrar no navegador
os.system('osascript -e "tell application \\"System Events\\" to key code 49 using {command down}"')
pyautogui.write('chrome')
pyautogui.press('return')

time.sleep(1.5)
#acessar o link
pyautogui.write(link)
pyautogui.press('return')

#entrar na conta
pyautogui.click(x=707, y=400)
pyautogui.write('daniel.junior82@aluno.unip.br')
pyautogui.press('tab')
pyautogui.write('python2024')
pyautogui.press('tab')
pyautogui.press('return')

tabela = pandas.read_csv('produtos.csv')
print('lista')

#codigo,marca,tipo,categoria,preco_unitario,custo,obs
for linha in tabela.index:
    time.sleep(0.1)
    # clicar na caixa de texto para cadastrar os itens
    pyautogui.click(x=707, y=285)
    #cadastrando codigo
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    #cadastrar marca
    pyautogui.write(tabela.loc[linha,'marca'])
    pyautogui.press('tab')
    #cadastrar tipo produto
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    #cadatrar categoria do produto
    pyautogui.write(str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')
    #cadastrar preço do produto
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    #cadastrar custo do produto
    pyautogui.write(str(tabela.loc[linha,'custo']))
    pyautogui.press('tab')
    #cadastrar OBS
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    #precionar return para cadastrar item
    pyautogui.press('return')
    #rolar para o inicio da tela
    pyautogui.scroll(5000)





