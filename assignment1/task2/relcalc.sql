a) EXISTS speed, hd, price. PC(model, speed, 512, hd, price)

b) EXISTS model, type. Product(maker, model, type) AND EXISTS speeed, model, ram, hd, price. Laptop(model, speed, ram, hd, 15, price)

c) EXISTS type. Product("E", model, type) AND
(EXISTS speed, ram, hd, screen. Laptop(model, speed, ram, hd, screen, price)
OR
EXISTS speed, ram, hd. PC(model, speed, ram, hd, price)
OR
EXISTS color, type. Printer(model, color, type, price))

d) EXISTS type. Product(maker, model, type) AND
(EXISTS speed, ram, hd, screen. Laptop(model, speed, ram, hd, screen, price)
OR
EXISTS speed, ram, hd. PC(model, speed, ram, hd, price)
OR
EXISTS color, type. Printer(model, color, type, price))

e) Product(maker, model, "printer")
AND NOT(maker="E") AND
EXISTS price. Printer(model, 1, "laser", price)


--Først finder vi de leverandører der ikke sælger printere og så de leverandører der sælger
--PC'er og så union mellem de to sæt
f) NOT(EXISTS model, type. Product(maker, model, type) AND
EXISTS color, type, price. Printer(model, color, type, price)) AND
EXISTS model1, type. Product(maker, model1, type) AND
EXISTS model2, speed, ram, hd, price. PC(model2, speed, ram, hd, price) AND model1=model2

g)EXISTS model1, speed, ram, hd, price. Laptop(model1, speed, ram, hd, screen, price) AND
EXISTS model2, speed, ram, hd, price. Laptop(model2, speed, ram, hd, screen, price) AND NOT(model1 = model2)
--ved at kræve at modellen skal være unik sikre vi at de to sammenlignede laptops ikke er en den samme, 
--ellers vil alle skærmstørrelser fremgå som optrådte de flere gange i databasen

h) 
EXISTS hd1, hd2, hd3. (EXISTS type, model. Product(maker, model, type) AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd1, screen, price)) AND
(EXISTS model, type. Product(maker, model, type) AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd2, screen, price)) AND
(EXISTS model, type. Product(maker, model, type) AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd3, screen, price)) 

AND NOT(hd1=hd2) AND NOT (hd1=hd3) AND NOT(hd2=hd3)
-- Læg mærke til at vi holder maker og model variablen den samme i alle expressions. Vi finder tre
-- Laptops med forskellige diskstørrelse fra samme manufacturer. Allerførst helt uden fra parentesen
-- ignorerer vi så hd, hd2 og hd3 i query resultatet



i)
j)
k)
