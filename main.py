import asyncio
from playwright.async_api import async_playwright
from time import sleep
import os

async def main():
    async with async_playwright() as playwright:
        print("""
          ▄▄ • ▄▄▄ .▄▄▄   ▄▄▄· ·▄▄▄▄        ▄▄▄      ·▄▄▄▄  ▄▄▄ .     ▄▄▄·▄▄▄ ..▄▄ · .▄▄ ·        ▄▄▄· .▄▄ · 
        ▐█ ▀ ▪▀▄.▀·▀▄ █·▐█ ▀█ ██▪ ██ ▪     ▀▄ █·    ██▪ ██ ▀▄.▀·    ▐█ ▄█▀▄.▀·▐█ ▀. ▐█ ▀. ▪     ▐█ ▀█ ▐█ ▀. 
        ▄█ ▀█▄▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄     ▐█· ▐█▌▐▀▀▪▄     ██▀·▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ ▄█▀▀█ ▄▀▀▀█▄
        ▐█▄▪▐█▐█▄▄▌▐█•█▌▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█•█▌    ██. ██ ▐█▄▄▌    ▐█▪·•▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌▐█ ▪▐▌▐█▄▪▐█
        ·▀▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀    ▀▀▀▀▀•  ▀▀▀     .▀    ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪ ▀  ▀  ▀▀▀▀ ~GabrielFry""")
        input('Pressione Enter para Continuar')
        os.system('cls')
        print("""
          ▄▄ • ▄▄▄ .▄▄▄   ▄▄▄· ·▄▄▄▄        ▄▄▄      ·▄▄▄▄  ▄▄▄ .     ▄▄▄·▄▄▄ ..▄▄ · .▄▄ ·        ▄▄▄· .▄▄ · 
        ▐█ ▀ ▪▀▄.▀·▀▄ █·▐█ ▀█ ██▪ ██ ▪     ▀▄ █·    ██▪ ██ ▀▄.▀·    ▐█ ▄█▀▄.▀·▐█ ▀. ▐█ ▀. ▪     ▐█ ▀█ ▐█ ▀. 
        ▄█ ▀█▄▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄     ▐█· ▐█▌▐▀▀▪▄     ██▀·▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ ▄█▀▀█ ▄▀▀▀█▄
        ▐█▄▪▐█▐█▄▄▌▐█•█▌▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█•█▌    ██. ██ ▐█▄▄▌    ▐█▪·•▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌▐█ ▪▐▌▐█▄▪▐█
        ·▀▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀    ▀▀▀▀▀•  ▀▀▀     .▀    ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪ ▀  ▀  ▀▀▀▀ ~GabrielFry""")
        print('Inicializando...')
        browser = await playwright.firefox.launch(headless=True)
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()
        headers = {'User-Agent': 'Mozilla/5.0 (U; Linux i674 x86_64; en-US) AppleWebKit/533.28 (KHTML, like Gecko) Chrome/53.0.3556.140 Safari/601'}
        await page.set_extra_http_headers(headers)
        await page.goto('https://www.4devs.com.br/gerador_de_pessoas')
        await page.click('input[type="button"][id="bt_gerar_pessoa"]')
        os.system('cls')
        print("""
          ▄▄ • ▄▄▄ .▄▄▄   ▄▄▄· ·▄▄▄▄        ▄▄▄      ·▄▄▄▄  ▄▄▄ .     ▄▄▄·▄▄▄ ..▄▄ · .▄▄ ·        ▄▄▄· .▄▄ · 
        ▐█ ▀ ▪▀▄.▀·▀▄ █·▐█ ▀█ ██▪ ██ ▪     ▀▄ █·    ██▪ ██ ▀▄.▀·    ▐█ ▄█▀▄.▀·▐█ ▀. ▐█ ▀. ▪     ▐█ ▀█ ▐█ ▀. 
        ▄█ ▀█▄▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄     ▐█· ▐█▌▐▀▀▪▄     ██▀·▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ ▄█▀▀█ ▄▀▀▀█▄
        ▐█▄▪▐█▐█▄▄▌▐█•█▌▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█•█▌    ██. ██ ▐█▄▄▌    ▐█▪·•▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌▐█ ▪▐▌▐█▄▪▐█
        ·▀▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀    ▀▀▀▀▀•  ▀▀▀     .▀    ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪ ▀  ▀  ▀▀▀▀ ~GabrielFry""")
        print('Coletando Dados... 3')
        sleep(0.5)
        os.system('cls')
        print("""
          ▄▄ • ▄▄▄ .▄▄▄   ▄▄▄· ·▄▄▄▄        ▄▄▄      ·▄▄▄▄  ▄▄▄ .     ▄▄▄·▄▄▄ ..▄▄ · .▄▄ ·        ▄▄▄· .▄▄ · 
        ▐█ ▀ ▪▀▄.▀·▀▄ █·▐█ ▀█ ██▪ ██ ▪     ▀▄ █·    ██▪ ██ ▀▄.▀·    ▐█ ▄█▀▄.▀·▐█ ▀. ▐█ ▀. ▪     ▐█ ▀█ ▐█ ▀. 
        ▄█ ▀█▄▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄     ▐█· ▐█▌▐▀▀▪▄     ██▀·▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ ▄█▀▀█ ▄▀▀▀█▄
        ▐█▄▪▐█▐█▄▄▌▐█•█▌▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█•█▌    ██. ██ ▐█▄▄▌    ▐█▪·•▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌▐█ ▪▐▌▐█▄▪▐█
        ·▀▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀    ▀▀▀▀▀•  ▀▀▀     .▀    ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪ ▀  ▀  ▀▀▀▀ ~GabrielFry""")
        print('Coletando Dados... 2')
        sleep(0.5)
        os.system('cls')
        print("""
          ▄▄ • ▄▄▄ .▄▄▄   ▄▄▄· ·▄▄▄▄        ▄▄▄      ·▄▄▄▄  ▄▄▄ .     ▄▄▄·▄▄▄ ..▄▄ · .▄▄ ·        ▄▄▄· .▄▄ · 
        ▐█ ▀ ▪▀▄.▀·▀▄ █·▐█ ▀█ ██▪ ██ ▪     ▀▄ █·    ██▪ ██ ▀▄.▀·    ▐█ ▄█▀▄.▀·▐█ ▀. ▐█ ▀. ▪     ▐█ ▀█ ▐█ ▀. 
        ▄█ ▀█▄▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄     ▐█· ▐█▌▐▀▀▪▄     ██▀·▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ ▄█▀▀█ ▄▀▀▀█▄
        ▐█▄▪▐█▐█▄▄▌▐█•█▌▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█•█▌    ██. ██ ▐█▄▄▌    ▐█▪·•▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌▐█ ▪▐▌▐█▄▪▐█
        ·▀▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀    ▀▀▀▀▀•  ▀▀▀     .▀    ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪ ▀  ▀  ▀▀▀▀ ~GabrielFry""")
        print('Coletando Dados... 1')
        nome = await page.locator('//*[@id="nome"]').text_content()
        cpf = await page.locator('//*[@id="cpf"]').text_content()
        rg = await page.locator('//*[@id="rg"]').text_content()
        data = await page.locator('//*[@id="data_nasc"]').text_content()
        sexo = await page.locator('//*[@id="sexo"]').text_content()
        signo = await page.locator('//*[@id="signo"]').text_content()
        #// filiação
        mae = await page.locator('//*[@id="mae"]').text_content()
        pai = await page.locator('//*[@id="pai"]').text_content()
        #//endereço
        cep = await page.locator('//*[@id="cep"]').text_content()
        endereco = await page.locator('//*[@id="endereco"]').text_content()
        numero = await page.locator('//*[@id="numero"]').text_content()
        bairro = await page.locator('//*[@id="bairro"]').text_content()
        cidade = await page.locator('//*[@id="cidade"]').text_content()
        estado = await page.locator('//*[@id="estado"]').text_content()
        os.system('cls')
        print("""
            ▄▄▄  ▄▄▄ ..▄▄ · ▄• ▄▌▄▄▌  ▄▄▄▄▄ ▄▄▄· ·▄▄▄▄        
            ▀▄ █·▀▄.▀·▐█ ▀. █▪██▌██•  •██  ▐█ ▀█ ██▪ ██ ▪     
            ▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄█▌▐█▌██▪   ▐█.▪▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ 
            ▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▄█▌▐█▌▐▌ ▐█▌·▐█ ▪▐▌██. ██ ▐█▌.▐▌
            .▀  ▀ ▀▀▀  ▀▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀  ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪
              
        """)
        print('~~~~~~~~~~INFORMAÇÕES~~~~~~~~~')
        print('Nome:', nome)
        print('Cpf:', cpf)
        print('RG:', rg)
        print('Data de Nascimento:', data)
        print('Sexo:', sexo)
        print('Signo:', signo)
        print('~~~~~~~~~~AFILIAÇÕES~~~~~~~~~')
        print('Mãe:', mae)
        print('Pai:', pai)
        print('~~~~~~~~~~ENDEREÇO~~~~~~~~~')
        print('Cep:', cep)
        print('Endereço:', endereco)
        print('Número:', numero)
        print('Bairro:', bairro)
        print('Cidade:', cidade)
        print('Estado:', estado)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        while True:
            finalizar = input('Gerar Outra Pessoa?: (s) Ou (n):')
            if(finalizar == "n" ):
                print('Finalizando...')
                break
            else:
                os.system('cls')
                await page.click('input[type="button"][id="bt_gerar_pessoa"]')
                os.system('cls')
                print("""
          ▄▄ • ▄▄▄ .▄▄▄   ▄▄▄· ·▄▄▄▄        ▄▄▄      ·▄▄▄▄  ▄▄▄ .     ▄▄▄·▄▄▄ ..▄▄ · .▄▄ ·        ▄▄▄· .▄▄ · 
        ▐█ ▀ ▪▀▄.▀·▀▄ █·▐█ ▀█ ██▪ ██ ▪     ▀▄ █·    ██▪ ██ ▀▄.▀·    ▐█ ▄█▀▄.▀·▐█ ▀. ▐█ ▀. ▪     ▐█ ▀█ ▐█ ▀. 
        ▄█ ▀█▄▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄     ▐█· ▐█▌▐▀▀▪▄     ██▀·▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ ▄█▀▀█ ▄▀▀▀█▄
        ▐█▄▪▐█▐█▄▄▌▐█•█▌▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█•█▌    ██. ██ ▐█▄▄▌    ▐█▪·•▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌▐█ ▪▐▌▐█▄▪▐█
        ·▀▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀    ▀▀▀▀▀•  ▀▀▀     .▀    ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪ ▀  ▀  ▀▀▀▀ ~GabrielFry""")
                print('Coletando Dados... 1')
                nome = await page.locator('//*[@id="nome"]').text_content()
                cpf = await page.locator('//*[@id="cpf"]').text_content()
                rg = await page.locator('//*[@id="rg"]').text_content()
                data = await page.locator('//*[@id="data_nasc"]').text_content()
                sexo = await page.locator('//*[@id="sexo"]').text_content()
                signo = await page.locator('//*[@id="signo"]').text_content()
                #// filiação
                mae = await page.locator('//*[@id="mae"]').text_content()
                pai = await page.locator('//*[@id="pai"]').text_content()
                #//endereço
                cep = await page.locator('//*[@id="cep"]').text_content()
                endereco = await page.locator('//*[@id="endereco"]').text_content()
                numero = await page.locator('//*[@id="numero"]').text_content()
                bairro = await page.locator('//*[@id="bairro"]').text_content()
                cidade = await page.locator('//*[@id="cidade"]').text_content()
                estado = await page.locator('//*[@id="estado"]').text_content()
                os.system('cls')
                print("""
                    ▄▄▄  ▄▄▄ ..▄▄ · ▄• ▄▌▄▄▌  ▄▄▄▄▄ ▄▄▄· ·▄▄▄▄        
                    ▀▄ █·▀▄.▀·▐█ ▀. █▪██▌██•  •██  ▐█ ▀█ ██▪ ██ ▪     
                    ▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄█▌▐█▌██▪   ▐█.▪▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ 
                    ▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▄█▌▐█▌▐▌ ▐█▌·▐█ ▪▐▌██. ██ ▐█▌.▐▌
                    .▀  ▀ ▀▀▀  ▀▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀  ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪
                      
                """)
                print('~~~~~~~~~~INFORMAÇÕES~~~~~~~~~')
                print('Nome:', nome)
                print('Cpf:', cpf)
                print('RG:', rg)
                print('Data de Nascimento:', data)
                print('Sexo:', sexo)
                print('Signo:', signo)
                print('~~~~~~~~~~AFILIAÇÕES~~~~~~~~~')
                print('Mãe:', mae)
                print('Pai:', pai)
                print('~~~~~~~~~~ENDEREÇO~~~~~~~~~')
                print('Cep:', cep)
                print('Endereço:', endereco)
                print('Número:', numero)
                print('Bairro:', bairro)
                print('Cidade:', cidade)
                print('Estado:', estado)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

asyncio.run(main())