 
 
DROP DATABASE IF EXISTS checking;
CREATE SCHEMA checking;
USE checking;
 
CREATE TABLE users(
   user_id int NOT NULL,
   user_name varchar(20) NOT NULL,
   Email_id varchar(50) NOT NULL,
   password varchar(20) NOT NULL,
   Gender char NOT NULL,
   Age int NOT NULL,
   line1 varchar(40) NOT NULL,
   line2 varchar(40) NOT NULL,
   district varchar(20) NOT NULL,
   city varchar(20) NOT NULL,
   state varchar(20) NOT NULL,
   country varchar(20) NOT NULL,
   pincode int NOT NULL,
   primary key (user_id)
)
;
insert into users values (
   12,
   'Alex',
   'Alex.s@gmail.com',
   'Alex',
   'M',
   '21',
   'h.no 1-2-3',
   'Myhome apartments road',
   'rangareddy',
   'Hyderabad',
   'telangana',
   'india',
   '12345' ),(
   13,
   'smith',
   'smith.s@gmail.com',
   'smith',
   'M',
   '22',
   'h.no 1-2-34',
   'clock tower',
   'rangareddy',
   'Hyderabad',
   'telangana',
   'india',
   '12345' ),(
   14,
   'chris',
   'chris.s@gmail.com',
   'chris',
   'M',
   '23',
   'h.no 1-2-345',
   'triveni apartments',
   'hanmkonda',
   'warangal',
   'telangana',
   'india',
   '12345' ),(
   15,
   'satwik',
   'satwik@gmail.com',
   'satwik',
   'M',
   '20',
   'h.no:11-12-13',
   'kamala garden',
   'mahabubnagar',
   'mahabubnagar',
   'telangana',
   'india',
   '509001'
   ),(
   20,
   'gayathri',
   'gayathri@yahoo.com',
   'abcd12345',
   'F',
   '18',
   'h.no:10-20-100/1',
   'clock tower',
   'rangareddy',
   'hyderabad',
   'telangana',
   'india',
   '409002'
   ),(
   21,
   'vijay',
   'vijay@kagool.com',
   'abcd123456',
   'M',
   '22',
   'myhome apartments',
   'gachibowli',
   'rangareddy',
   'hyderabad',
   'telangana',
   'india',
   '409002'
   )
   ;
 
CREATE table phone_no (
   user_id int NOT NULL,
   phone_no int NOT NULL,
   primary key (phone_no,user_id),
   constraint phone_no_dbfk1 foreign key (user_id) references users(user_id)
   on update CASCADE
   on delete CASCADE
);
insert into phone_no values(
   12,1234567890
),(
   13,1234123412
),(
   13,1234123123
),(
   14,1222111122
),(
   15,1234232311
),(
   15,1899765444
),(
   21,1988776655
),(
   20,1234552661
);
 
 
 
CREATE table cards(
   user_id int NOT NULL,
   card_No char(10) NOT NULL,
   card_type varchar(20) NOT NULL,
   Expiry_month int NOT NULL,
   Expiry_year int NOT NULL,
   primary key (user_id,card_No),
   constraint cards_dbfk2 foreign key (user_id) references users (user_id)
   on update CASCADE
   on delete CASCADE
);
insert into cards values(
   12,
   1234567891,
   'visa',
   09,
   2028
),(
   13,
   1231234321,
   'rupay',
   10,
   2025
),(
   13,
   1231245672,
   'axis',
   11,
   1023
),(
   20,
   187654310,
   'visa',
   12,
   2022
),(
   21,
   1234123261,
   'rupay',
   12,
   2025
),(
   15,
   187098765,
   'visa',
   10,
   2030
);
 
 
CREATE TABLE SUPPLIER(
   sellerID int NOT NULL,
   Name varchar(20) NOT NULL,
   line1 varchar(40) NOT NULL,
   line2 varchar(40) ,
   district varchar(20) NOT NULL,
   city varchar(20) NOT NULL,
   state varchar(20) NOT NULL,
   country varchar(20) NOT NULL,
   pincode int NOT NULL,
   primary key(sellerID)
   )
   ;
 
INSERT INTO SUPPLIER values(1,'LIBAS IMPEX','B-19','SECTOR-83 PHASE-2','Gautam Buddha Nagar','NOIDA','UTTAR PRADESH','INDIA',560103),
(2,'Agrawal Enterprises','714-A kakad market','306 kalbadevi road','Mumbai','Mumbai','Maharastra','INDIA',400002),(3,'KESHVI FASHION LLP',
'THIRD FLOOR SHOP NO 3043','NEW SARDAR TRADERS MARKET','SURAT','SURAT','GUJARAT','INDIA',395010),
(4,'INDO ERA DESIGNS','4th FLOOR BLOCK NO B-4021','ASHIRWAD TEXTILE MARKET MAGOB','SURAT','SURAT','GUJARAT','INDIA',395010);
 
 
 
CREATE TABLE PRODUCT(
  productcode int NOT NULL,
   colour varchar(10) NOT NULL,
   name varchar(20) NOT NULL,
   stock int NOT NULL,
   description varchar(350),
   productavailability varchar(20) NOT NULL,
   original_price int NOT NULL,
   no_of_products_sold_out int NOT NULL,
   brandname varchar(15) NOT NULL,
   discount int DEFAULT 0,
   sellerID int NOT NULL,
   companyname varchar(20) NOT NULL,
   Address varchar(200) NOT NULL,
   primary key(productcode),
   CONSTRAINT product_fk1 FOREIGN KEY (sellerID) REFERENCES SUPPLIER(sellerID) ON UPDATE CASCADE 
ON DELETE CASCADE
   );
 
INSERT INTO PRODUCT values
(1000001,'blue','kurta set',150,'navy blue printed kurta with trousers and dupatta ,kurta with round neck,3-quarter sleeves,side slits',
'available',1200,99,'INDO ERA',75,4,'Indo era-designs','Malini vadi,Gali no2,Ring Road,surat-395010'),
(1200001,'pink','kurta with skirt',305,'pink and white bhandani print kurta with skirt,kurta with tie up neck,3-quarter sleeves',
'available',1350,123,'ISHIN',73,2,'Agrawal Enterprises','Shri Bhatia halai majan wadi,306 kalbadevi road,mumbai-400002'),
(1300001,'brown','saree',350,'brown and beige saree with printed border','limited',4000,109,'LIBAS',62,1,
'Libas impex','b-19 first floor sector 83 phase 2 noida U.P -201305'),
(1400001,'red','T-shirt',378,'red solid t-shirt with short sleeves',
'available',799,453,'GERUA',37,3,'keshvi fashion','SHOP NO 3043 TEXTILE MARKEt SURAT GUJARAT-395010'),
(1000002,'blue','shirt',500,'blue solid shirt with long sleeves','available',2500,230,'INDO ERA',20,4,'Indo era-designs','Malini vadi,Gali no2,Ring Road,surat-395010'),
(1300002,'red','saree',23,'red silk saree','limited',9999,12,'LIBAS',62,1,
'Libas impex','b-19 first floor sector 83 phase 2 noida U.P -201305'),
(1200002,'red','frock',267,'red frock','available',400,567,'ISHIN',73,2,'Agrawal Enterprises','Shri Bhatia halai majan wadi,306 kalbadevi road,mumbai-400002'),
(1400002,'pink','sweater',789,'pink self design sweater','available',800,567,'GERUA',37,3,'keshvi fashion','SHOP NO 3043 TEXTILE MARKEt SURAT GUJARAT-395010'),
(1200003,'green','kurta',5778,'green straight kurta','available',900,567,'ISHIN',23,2,'Agrawal Enterprises','Shri Bhatia halai majan wadi,306 kalbadevi road,mumbai-400002'),
(1400003,'yellow','night pant',5467,'yellow cotton night pant','available',600,567,'GERUA',37,3,'keshvi fashion','SHOP NO 3043 TEXTILE MARKEt SURAT GUJARAT-395010');
 
CREATE TABLE AVAILABLESIZES(
       product_code int NOT NULL,
         size varchar(10) NOT NULL,
 
    primary key(size,product_code),
   
   CONSTRAINT size_fk1 FOREIGN KEY(product_code) REFERENCES PRODUCT(productcode)
   on update cascade
   on delete cascade
   );
 
INSERT INTO AVAILABLESIZES values
(1000001,'S'),(1000001,'M'),(1000001,'L'),(1200001,'XS'),(1200001,'S'),(1200001,'M'),(1300001,'ONESIZE'),(1400001,'XL'),(1400001,'XXL'),(1000002,'S'),(1000002,'M'),(1000002,'L'),(1300002,'ONESIZE'),
(1200002,'L'),(1200003,'S'),(1400002,'ONESIZE'),(1400003,'XL'),(1400003,'XXL');
 
CREATE table review(
   Rating int,
   Quality int,
   fitness int,
   transparency int,
   text varchar(100),
   product_code int NOT NULL,
   user_id int NOT NULL,
   primary key (product_code,user_id),
   constraint review_fk1 FOREIGN KEY (product_code) REFERENCES PRODUCT (productcode)
   on update CASCADE
   on delete CASCADE,
   constraint review_fk2 FOREIGN KEY (user_id) REFERENCES users (user_id) on update cascade on delete cascade
);
 
insert into review values(
   8,8,7,6,
   'I am not so satisfied with the product because the colour i expected was completely different',
   1300002,
   12
),(
   9,9,8,8,
   'i really liked the product',
   1400001,
   13
),(
   10,10,10,10,
   'extremely satisfied',
   1400001,
   14
),(
   10,9,8,7,
   'fitness was not as expected',
   1400001,
   15
),(
   4,4,4,4,
   'im deeply disappointed',
   1300001,
   13
),(
   10,10,10,9,
   'Thank you for offering these beautifully unique tops. They are flattering and gorgeous',
   1000001,
   12
);

 
CREATE TABLE Shipper(
  shipper_id int NOT NULL,
  company_name varchar(50) NOT NULL,
  line1 varchar(50) NOT NULL,
  line2 varchar(50) NOT NULL,
  district varchar(50) NOT NULL,
  city varchar(50) NOT NULL,
  state_name varchar(50) NOT NULL,
  country varchar(50) NOT NULL,
  pincode varchar(10) NOT NULL,
  primary key(shipper_id)
 )
;
 
INSERT INTO Shipper VALUES(
   5,
   'Amazon',
   'street no 12',
   'near hitechcity',
   'Hyderabad',
   'Kukatpally',
   'Telangana',
   'India',
   '505503'),(
   7,
   'flipcart',
   'street no 15',
   'Gachoboli',
   'hyderabad',
   'Gachiboli',
   'Telangana',
   'India',
   '505503'),(
    9,
   'myntra',
   'street no 19',
   '1000 pillar temple',
   'Warangal',
   'Hanamkonda',
   'Telangana',
   'India',
   '506002'),(
   10,
   'zomby',
   'street no 5',
   'miyapur',
   'Hyderabad',
   'Kukatpally',
   'Telangana',
   'India',
   '599503'),(
   11,
   'meesho',
   'street no 2',
   'near ayyapa temple',
   'karimnagar',
   'Ananthagiri colony',
   'Telangana',
   'India',
   '507803'),(
   12,
   'Dmart',
   'street no 22',
   'hitechcity',
   'Hyderabad',
   'Madapur',
   'Telangana',
   'India',
   '509503'
   
);
 
CREATE TABLE Orders(
   orderid int NOT NULL,
   shipperid int NOT NULL,
   t_ime varchar(50) NOT NULL,
   s_tatus varchar(20) NOT NULL,
   d_ate  varchar(20) NOT NULL,
   primary key (orderid),
   CONSTRAINT order_fk1 FOREIGN KEY (shipperid) REFERENCES
   Shipper(shipper_id)
   On update cascade
   On delete cascade
)
;
INSERT INTO Orders VALUES(
   3,
   5,
   'oct 22nd 2021',
   'Not Delivered',
   '21st oct 2021'),(
   8,
   7,
   'oct 23rd 2021',
   'not delivered',
   '20th oct 2021'),(
   10,
   9,
   'oct 15th 2021',
   'delivered',
   '18th oct 2021'),(
   12,
   9,
   'oct 16th 2021',
   'delivered',
   '19th oct 2021'),(
   13,
   10,
   'oct 12th 2021',
   'delivered',
   '19th oct 2021'),(
   14,
   12,
   'oct 14th 2021',
   'delivered',
   '18th oct 2021'
   );
 
 
CREATE TABLE payment(
  TransactionID int NOT NULL,
  Modeofpayment varchar(20) NOT NULL,
  status varchar(20) NOT NULL,
  Totalprice  int NOT NULL,
  order_ID int NOT NULL,
  primary key (TransactionID),
  CONSTRAINT payment_fk1 FOREIGN KEY (order_ID) REFERENCES
   Orders(orderid)
   On update cascade
   On delete cascade
 
);
INSERT INTO payment VALUES(
   1235678,
   'online',
   'paid',
   2000,
   3),(
   1222222,
   'offline',
   'paid',
   2500,
   3
   ),(
   1233558,
   'online',
   'paid',
   1888,
   8),(
   111111,
   'online',
   'paid',
   3000,
   10 ),(
   123333,
   'online',
   'paid',
   900,
   13),(
   155558,
   'online',
   'paid',
   1000,
   12

   );
 
CREATE TABLE ord_details(
  customer_ID int NOT NULL,
  orderid int  NOT NULL,
  Product_code int NOT NULL,
  Quantity int NOT NULL,
  size varchar(10) NOT NULL,
  CONSTRAINT details_fk1 FOREIGN KEY (orderid) REFERENCES
   Orders(orderid) on update CASCADE
   on delete CASCADE,
  CONSTRAINT details_fk2 FOREIGN KEY (customer_ID) REFERENCES
   users(user_id) on update CASCADE
   on delete CASCADE,
  CONSTRAINT details_fk3 FOREIGN KEY (product_code) REFERENCES
   PRODUCT(productcode)
   On update cascade
   On delete cascade
 
 
);
 
INSERT INTO ord_details VALUES(
   12,
   3,
   1000001,
   2,
   'XL'),(
   12,
   8,
   1200001,
   3,
   'ONE SIZE'),(
   13,
   10,
   1300002,
   1,
   'S'),(
   13,
   12,
   1400001,
   3,
   'XL'),(
   14,
   13,
   1400001,
   1,
   'XL'),(
   15,
   14,
   1000001,
   1,
   'XL');
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


