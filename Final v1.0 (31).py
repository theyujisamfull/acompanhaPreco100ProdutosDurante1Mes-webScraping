def dataHoje():
    from datetime import date,datetime


    today = date.today()
    date = today.strftime('%d%h')


    hora = datetime.now()
    horaa = hora.strftime('%H:%M')
    
    return date+' '+horaa





def inputaPrecoDeHoje():
    
    amazon = 'https://www.amazon.com.br/Kindle-10a-gera%C3%A7%C3%A3o-ilumina%C3%A7%C3%A3o-embutida/dp/B07FQK1TS9/ref=asc_df_B07FQK1TS9/?tag=googleshopp00-20&linkCode=df0&hvadid=432951822456&hvpos=&hvnetw=g&hvrand=1903739485450411682&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001773&hvtargid=pla-901759904091&psc=1'
    magazine = 'https://www.kabum.com.br/produto/112795/kindle-10-geracao-preto-luz-integrada-wi-fi-8gb-ao0772?gclid=CjwKCAjw2P-KBhByEiwADBYWCkruL6X4mB1ujwgHnH_j4Gltz8BkJMgTv8mERmIjOg2xCBjzHsXYehoCg6YQAvD_BwE'
    casasBahia = 'https://www.casasbahia.com.br/kindle-amazon-10-geracao-com-8gb-tela-de-6-e-iluminacao-embutida-preto-55006484/p/55006484?utm_medium=Cpc&utm_source=GP_PLA&IdSku=55006484&idLojista=10037&utm_campaign=aces_smart-shopping&gclid=CjwKCAjw2P-KBhByEiwADBYWCkfZuIzb7vBZ8NSaO6snWKAkcQdGXosf-ZNlc4COOtIi0cC-J_t-QhoCJJAQAvD_BwE'
    fastShop = 'https://www.fastshop.com.br/web/p/d/A6KINDG10PTO_PRD/e-reader-kindle-10a-geracao-amazon-6-polegadas-8gb-preto-fast?partner=parceiro-google&cm_mmc=cpc_Shopping-_-A6KINDG10PTO_PRD&gclid=CjwKCAjw2P-KBhByEiwADBYWCte6OlVBbzlizqvK8pFhHIN42oyYmndjEMN_fj_bPV_fJDbbnA3rfhoCJ_4QAvD_BwE'
    urls = [amazon,magazine,casasBahia,fastShop]

    amazonClass = 'priceBlockSavingsString'
    magazineClass = 'cIGWul'
    casasBahia = 'product-price-value'
    fastShop = 'price-fraction'
    classes = [amazonClass,magazineClass,casasBahia,fastShop]

    amazonTxt = 'data/kindleAmazon.txt'
    magazineTxt = 'data/kindleMagazine.txt'
    casasBahia = 'data/casasBahia.txt'
    fastShop = 'data/fastShop.txt'
    txtName = [amazonTxt,magazineTxt,casasBahia,fastShop]

    amazonTag = 'span'
    magazineTag = 'h4'
    casasBahia = 'span'
    fastShop = 'span'
    tagName = [amazonTag,magazineTag,casasBahia,fastShop]
    
    for i in [2,3]:
        from selenium import webdriver
        simulator = webdriver.Chrome(executable_path = r"C:\Users\TheYujiSamFull\Downloads\safe\chromedriver.exe")
        simulator.get(urls[i])

        from bs4 import BeautifulSoup
        import time
        site = simulator.page_source.encode('utf-8').strip()
        html = BeautifulSoup(site,'html.parser')
        preco = html.find(tagName[i],class_=classes[i]).get_text()


        file = open(txtName[i],'a')

        file.writelines([dataHoje()+';'+preco+'\n'])
        simulator.quit()

    return preco








def montaGrafico(x,vetorY,legenda):


    import matplotlib.pyplot as plt

    for i in range(len(vetorY)):
        
        plt.plot(x,vetorY[i] , label=legenda[i])
        plt.legend()
        plt.title('Kindle 10')
        plt.ylabel('R$')
        


    plt.show()



def pegaDadosTxt(txtName):

    file = open('data/'+txtName+'.txt','r')

    x = file.readlines()

    lines = []
    for i in x:
        lines.append(i.split(';'))


    x = []
    preco = []
    for i in lines:
        
        x.append(i[0])
        precoAux = i[1]

        #tira \n
        if precoAux[-1] == '\n':
            precoAux = precoAux[0:-1]
        else:precoAux = precoAux[0:]


        for j in range(len(precoAux)):
            num = ['0','1','2','3','4','5','6','7','8','9']
            if precoAux[j] in num:
                break
        preco.append(precoAux[j:])
        


    

    return x,preco





def main():

    
    inputaPrecoDeHoje()

    x,precoAmazon = pegaDadosTxt('kindleAmazon') 
                                  
    y,precoMagazine = pegaDadosTxt('kindleMagazine')

    y,precoCasasBahia = pegaDadosTxt('casasBahia')

    y,precoFastShop = pegaDadosTxt('fastShop')



    y = [precoAmazon,precoMagazine,precoCasasBahia,precoFastShop]
    legenda = ['Amazon','Magazine','Casas Bahia','Fast Shop']
    montaGrafico(x,y,legenda)

    



main()
















