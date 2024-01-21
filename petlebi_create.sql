USE petlebi;
CREATE TABLE petlebi (
    productID INT,
    productURL VARCHAR(255),
    productName VARCHAR(255),
    productBarcode VARCHAR(50),
    productPrice VARCHAR(25),
    productStock BOOLEAN DEFAULT true,
    productImages VARCHAR(255),
    description TEXT,
    sku VARCHAR(50),
    category VARCHAR(255),
    brand VARCHAR(255)
);

