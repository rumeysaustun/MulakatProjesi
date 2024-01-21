import mysql.connector
import json

# Veri tabanı: petlebi
# Sütunlar: productID, productURL, productName, productBarcode, productPrice,
#           productStock, productImages, description, sku, category, brand
def dbInsert():

    # Veri tabanına bağlanır.
    conn = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="root",
    database="petlebi",
    use_pure=True
    )
    cursor = conn.cursor()

    # Json dosyasını aç.
    with open('petlebi_products.json', 'r',encoding="UTF8") as file:
                data = json.load(file)

    # Bütün listedeki verileri dolaşır. Veri tabanına ekleme yapar.
    for item in data:
        stock = True if item["Data"]['productStock'] == "Out of Stock" else False
        stt = """
            INSERT INTO petlebi (productID, productURL, productName, 
                        productBarcode, productPrice, productStock, 
                        productImages, description, sku, category, brand)
            VALUES ({}, '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}');
        """.format(item["Data"]['productID'], item["Data"]['productURL'], item["Data"]['productName'],
                item["Data"]['productBarcode'], item["Data"]['productPrice'], stock,
                item["Data"]['productImages'], item["Data"]['description'], item["Data"]['sku'],
                item["Data"]['category'], item["Data"]['brand'])

        cursor.execute(stt)
        conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
       dbInsert()