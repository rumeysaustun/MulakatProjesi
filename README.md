# Mülakat Projesi

Projede;
- www.petlebi.com sitesinden veri çekme işlemi ve verileri Json dosyasına yazma ([petlebi_scrapy.py](https://github.com/rumeysaustun/MulakatProjesi/blob/main/petlebi_scrapy.py)),
- Json dosyasında bulunan verileri MySql veri tabanına atma ([import_products.py](https://github.com/rumeysaustun/MulakatProjesi/blob/main/import_products.py))
işlemleri yapılmaktadır.

## Projeyi Çalıştırma 

### petlebi_scrapy.py
------------------------
- petlebi_scrapy.py dosyasını yürütmek için direkt olarak çalıştırmak yeterlidir.
- Diğer bir yöntem ise terminalden

```
py -m scrapy runspider petlebi_scrapy.py
```
komutu yazmak yeterlidir. 

Proje dosyası çalıştırıldıktan sonra çıktı olarak [petlebi_products.json](https://github.com/rumeysaustun/MulakatProjesi/blob/main/petlebi_products.json) dosyasını vermektedir.

![image](https://github.com/rumeysaustun/MulakatProjesi/assets/59111328/2ebd4002-2cc3-49dc-ac07-edd691004ee8)

### petlebi_insert.py
----------------------------------------
- petlebi_insert.py dosyasını yürütmek için direkt olarak çalıştırmak yeterlidir.
Proje dosyası çalıştırıldıktan sonra Json dosyasında bulunan veriler petlebi tablosuna eklenir.

 Petlebi tablosunda bulunan sütunlar;
 - productID (int)
 - productURL (varchar(255))
 - productName (varchar(255))
 - productBarcode (varchar(255))
 - productPrice (varchar(255))
 - productStock (binary)
 - productImages (varchar(255))
 - description (varchar(255))
 - sku (varchar(255))
 - category (varchar(255))
 - brand (varchar(255))

![image](https://github.com/rumeysaustun/MulakatProjesi/assets/59111328/a9913118-d9e7-4269-b8c1-f5f5ce937c94)






  
