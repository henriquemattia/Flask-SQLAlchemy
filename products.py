import pandas as pd
import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()

# INSERIR NOVOS DADOS NA TABELA

planilha = pd.read_excel("products.xlsx")

for i, DADOS in enumerate(planilha['id']):
    id = planilha.loc[i,"id"]
    category = planilha.loc[i,"category"]
    name = planilha.loc[i,"name"]
    price = planilha.loc[i,"price"]
    desc_price = planilha.loc[i,"desc_price"]
    sku = planilha.loc[i,"sku"]
    route = planilha.loc[i,"route"]
    alt_img = planilha.loc[i, "alt_img"]
    img_main = planilha.loc[i,"img_main"]
    img_front = planilha.loc[i,"img_front"]
    img_right = planilha.loc[i,"img_right"]
    img_left = planilha.loc[i,"img_left"]
    img_back = planilha.loc[i,"img_back"]
    highlights = planilha.loc[i,"highlights"]
    is_available = planilha.loc[i,"is_available"]      
    

    conn = psycopg2.connect(host=os.environ["DB_HOST"],
                              dbname=os.environ["DB_NAME"],
                              user=os.environ["DB_USER"],
                              password=os.environ["DB_PASS"])
    comando = "insert into public.products (id, category, name, price, desc_price, sku, route, alt_img, img_main, img_front, img_right, img_left, img_back, highlights, is_available) VALUES "
    
    dados = f"({id}, '{category}', '{name}', {price}, {desc_price}, '{sku}', '{route}', '{alt_img}', '{img_main}', '{img_front}', '{img_right}', '{img_left}', '{img_back}', {highlights}, {is_available})"
    
    sql = comando + dados
    # print(sql)
    
    try:
        #Aqui cairá apenas produtos novos a serem inseridos
        cursor = conn.cursor()
        
        cursor.execute(sql)
        conn.commit()
        print("NOVO PRODUTO INSERIDO COM SUCESSO")
        
    except:
        # Aqui irá cair os produtos que já existem
        continue
    
conn.close()



# ATUALIZAR DADOS NA TABELA

planilha = pd.read_excel("products.xlsx")

for i, DADOS in enumerate(planilha['id']):
    id = planilha.loc[i,"id"]
    category = planilha.loc[i,"category"]
    name = planilha.loc[i,"name"]
    price = planilha.loc[i,"price"]
    desc_price = planilha.loc[i,"desc_price"]
    sku = planilha.loc[i,"sku"]
    route = planilha.loc[i,"route"]
    alt_img = planilha.loc[i, "alt_img"]
    img_main = planilha.loc[i,"img_main"]
    img_front = planilha.loc[i,"img_front"]
    img_right = planilha.loc[i,"img_right"]
    img_left = planilha.loc[i,"img_left"]
    img_back = planilha.loc[i,"img_back"]
    highlights = planilha.loc[i,"highlights"]
    is_available = planilha.loc[i,"is_available"]    
    
    
    i = f"id = {id}, "
    c = f"category = '{category}', "
    n = f"name = '{name}', "
    p = f"price = {price}, "
    d_p = f"desc_price = {desc_price}, "
    s = f"sku = '{sku}', "
    r = f"route = '{route}', "
    a_i = f"alt_img = '{alt_img}', "
    i_m = f"img_main = '{img_main}', "
    i_f = f"img_front = '{img_front}', "
    i_r = f"img_right = '{img_right}', "
    i_l = f"img_left = '{img_left}', "
    i_b = f"img_back = '{img_back}', "
    h = f"highlights = {highlights}, "
    is_a = f"is_available = {is_available} "
    
    
    conn = psycopg2.connect(host=os.environ["DB_HOST"],
                              dbname=os.environ["DB_NAME"],
                              user=os.environ["DB_USER"],
                              password=os.environ["DB_PASS"])
    declaração = "UPDATE products SET "
    filtro = f" WHERE id = {id} "
    unificando = declaração + i + c + n + p + d_p + s + r + a_i + i_m + i_f + i_r + i_l + i_b + h + is_a + filtro
    
    # popular dados
    try:
        cursor = conn.cursor()
        
        cursor.execute(unificando)
        conn.commit()
        
    except:
        print('ERRO AO ATUALIZAR PRODUTO')
        continue
    
conn.close() 
        