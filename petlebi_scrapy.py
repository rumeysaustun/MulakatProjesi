import scrapy
import json

from scrapy.crawler import CrawlerProcess

def multiplePage(pageNumber):
    arr = []
    for i in range(1,pageNumber+1):
        
        arr.append("https://www.petlebi.com/alisveris/ara?page=" + str(i))
    return arr

class PetlebiSpider(scrapy.Spider):
    name = 'petlebijson'
    allowed_domains = ['www.petlebi.com']
    # start_urls = multiplePage(221)
    start_urls = ["https://www.petlebi.com/papagan-yemi"]
    
    def __init__(self):
        self.data_list = [] 
        
    # Burada spider başlar.
    def parse(self, response):
        products = response.css('a.p-link') # a etiketindeki "p-link" class'ına sahip olanları alır.
        imgTags = response.css('img.img-fluid.lazy.mb-2') # img etiketindeki "img-fluid lazy mb-2" class'ına sahip olanları alır.
        
        for product, imgTag in zip(products, imgTags):
            datas = product.xpath('@data-gtm-product').extract_first() # data-gtm-product içindeki bilgileri alır.
            image = imgTag.xpath('@data-original').extract_first() # data-original içindeki bilgileri alır.
            url = product.xpath('@href').extract_first() # href içindeki bilgileri alır.
            
            # Linklerin hepsine girer. description ve barkod bilgilerini bu şekilde alır.
            yield scrapy.Request(
                url=product.xpath('@href').extract_first(),
                callback=self.parse_product,
                meta={
                    'datas': datas,
                    'image': image,
                    'url': url,
                }
            )

    # Burada Description ve barkod bilgilerini içine girdiği url'den alır.
    def parse_product(self, response):
        datas = response.meta.get('datas')
        image = response.meta.get('image')
        url = response.meta.get('url')

        description = response.xpath('//span[@id="productDescription"]/div')
        temp = ('\n'.join(description.xpath('string()').getall()))
        descriptionLast = temp.split("İçindekiler")[0].strip()

        barcode = response.xpath('//div[@class="row mb-2" and div[@class="col-2 pd-d-t" and text()="BARKOD"]]/div[@class="col-10 pd-d-v"]')
        barcodeLast = barcode.xpath('text()').get()

        # Verileri tutan bir sözlük oluşturup gerekli bilgileri tutar.
        fullDatas = {
            "productID": json.loads(datas)["id"],
            "productURL": url,
            "productName": json.loads(datas)["name"].replace("'", "\\'"),
            "productBarcode": barcodeLast,
            "productPrice": json.loads(datas)["price"],
            "productStock": json.loads(datas)["dimension2"],
            "productImages": image,
            "description": descriptionLast.replace("'", "\\'"),
            "sku": barcodeLast,
            "category": json.loads(datas)["category"].replace("'", "\\'"),
            "brand": json.loads(datas)["brand"].replace("'", "\\'")
        }
        self.data_list.append({'Data': fullDatas})
    
    # Spider kapatıldığında json dosyasına yazar.
    def closed(self, reason):
        with open('C:/Users/pc/Documents/GitHub/MulakatProjesi/petlebi_products.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data_list, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(PetlebiSpider)
    process.start()