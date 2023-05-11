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
EXISTS hd1, hd2, hd3. 

(EXISTS type, model. Product(maker, model, type) AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd1, screen, price)) AND


 AND
(EXISTS model, type. Product(maker, model, type) AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd2, screen, price)) AND
(EXISTS model, type. Product(maker, model, type) AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd3, screen, price)) 

AND NOT(hd1=hd2) AND NOT (hd1=hd3) AND NOT(hd2=hd3)
-- Læg mærke til at vi holder maker og model variablen den samme i alle expressions. Vi finder tre
-- Laptops med forskellige diskstørrelse fra samme manufacturer. Allerførst helt uden fra parentesen
-- ignorerer vi så hd, hd2 og hd3 i query resultatet

i)
EXISTS model1, model2, model3, model4.
(
    (EXISTS type. Product(maker, model1, type) AND
    EXISTS color, type, price. Printer(model1, color, type, price))
    AND
    (EXISTS type. Product(maker, model2, type) AND
    EXISTS color, type, price. Printer(model2, color, type, price))
    AND
    (EXISTS type. Product(maker, model3, type) AND
    EXISTS color, type, price. Printer(model3, color, type, price)) 
    AND NOT
    (EXISTS type. Product(maker, model4, type) AND
    EXISTS color, type, price. Printer(model4, color, type, price)))

AND NOT(model1=model2)AND NOT (model1=model3) AND NOT (model2=model3)
AND NOT(model1=model4)AND NOT(model2=model4) AND NOT (model3=model4)

x


j)


k)


Product
(A,1001,pc)
(A,1002,pc)
(A,1003,pc)
(A,2004,laptop)
(A,2005,laptop)
(A,2006,laptop)
(B,1004,pc)
(B,1005,pc)
(B,1006,pc)
(B,2007,laptop)
(C,1007,pc)
(D,1008,pc)
(D,1009,pc)
(D,1010,pc)
(D,3004,printer)
(D,3005,printer)
(D,3500,printer)
(E,1011,pc)
(E,1012,pc)
(E,1013,pc)
(E,2001,laptop)
(E,2002,laptop)
(E,2003,laptop)
(E,3001,printer)
(E,3002,printer)
(E,3003,printer)
(E,3500,printer)
(F,2008,laptop)
(F,2009,laptop)
(G,2010,laptop)
(H,3006,printer)
(H,3007,printer)

PC
(1001,2660,1024,250,2114)
(1002,2100,512,250,995)
(1003,1420,512,80,478)
(1004,2800,1024,250,649)
(1005,3200,512,250,630)
(1006,3200,1024,320,1049)
(1007,2200,1024,200,510)
(1008,2200,2048,250,770)
(1009,2000,1024,250,650)
(1010,2800,2048,200,770)
(1011,1860,2048,160,959)
(1012,2800,1024,160,649)
(1013,3060,512,80,529)

Laptop
(2001,2000,2048,240,20,3673)
(2002,1730,1024,80,17,949)
(2003,1800,512,60,15,549)
(2004,2000,512,60,13,1150)
(2005,2160,1024,120,17,2500)
(2006,2000,2048,80,15,1700)
(2007,1830,1024,120,13,1429)
(2008,1600,1024,100,15,900)
(2009,1600,512,80,14,680)
(2010,2000,2048,160,15,2300)

Printer
(3001,1,ink-jet,99)
(3002,1,laser,239)
(3003,0,laser,899)
(3004,1,ink-jet,120)
(3005,0,laser,120)
(3006,1,ink-jet,100)
(3007,1,laser,200)
(3500,1,laser,200)