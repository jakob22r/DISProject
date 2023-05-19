a) 
EXISTS speed, hd, price. PC(model, speed, 512, hd, price)

b) 
EXISTS model, type. Product(maker, model, type) 
AND 
EXISTS speeed, model, ram, hd, price. Laptop(model, speed, ram, hd, 15, price)

c)
EXISTS type. Product("E", model, type) AND
(EXISTS speed, ram, hd, screen. Laptop(model, speed, ram, hd, screen, price)
OR
EXISTS speed, ram, hd. PC(model, speed, ram, hd, price)
OR
EXISTS color, type. Printer(model, color, type, price))

d) 
EXISTS type. Product(maker, model, type) AND
(EXISTS speed, ram, hd, screen. Laptop(model, speed, ram, hd, screen, price)
OR
EXISTS speed, ram, hd. PC(model, speed, ram, hd, price)
OR
EXISTS color, type. Printer(model, color, type, price))

e) 
Product(maker, model, "printer")
AND NOT(maker="E") AND
EXISTS price. Printer(model, 1, "laser", price)


--Først finder vi de leverandører der ikke sælger printere og så de leverandører der sælger
--PC'er og så union mellem de to sæt
f) 
NOT(EXISTS model, type. Product(maker, model, type) AND
EXISTS color, type, price. Printer(model, color, type, price)) 
AND
EXISTS model1, type. Product(maker, model1, type) 
AND
EXISTS model2, speed, ram, hd, price. PC(model2, speed, ram, hd, price) 
AND model1=model2

g)
EXISTS model1, speed, ram, hd, price. Laptop(model1, speed, ram, hd, screen, price) AND
EXISTS model2, speed, ram, hd, price. Laptop(model2, speed, ram, hd, screen, price) AND NOT(model1 = model2)
--ved at kræve at modellen skal være unik sikre vi at de to sammenlignede laptops ikke er en den samme, 
--ellers vil alle skærmstørrelser fremgå som optrådte de flere gange i databasen

h) 
EXISTS hd1, hd2, hd3. 

(EXISTS type, model. Product(maker, model, type) 
AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd1, screen, price)) 
AND
(EXISTS model, type. Product(maker, model, type) 
AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd2, screen, price)) 
AND
(EXISTS model, type. Product(maker, model, type) 
AND
EXISTS, speed, ram, screen, price. Laptop(model, speed, ram, hd3, screen, price)) 

AND NOT(hd1=hd2) AND NOT (hd1=hd3) AND NOT(hd2=hd3)
-- Læg mærke til at vi holder maker og model variablen den samme i alle expressions. Vi finder tre
-- Laptops med forskellige diskstørrelse fra samme manufacturer. Allerførst helt uden fra parentesen
-- ignorerer vi så hd, hd2 og hd3 i query resultatet

i)
EXISTS model1, model2, model3.
(
    (EXISTS type. Product(maker, model1, type) AND
    EXISTS color, type, price. Printer(model1, color, type, price))
    AND
    (EXISTS type. Product(maker, model2, type) AND
    EXISTS color, type, price. Printer(model2, color, type, price))
    AND
    (EXISTS type. Product(maker, model3, type) AND
    EXISTS color, type, price. Printer(model3, color, type, price)) 
    AND NOT(model1=model2)AND NOT (model1=model3) AND NOT (model2=model3)
)
    AND NOT 
    (EXISTS model4, type. Product(maker, model4, type) AND
    EXISTS color, type, price. Printer(model4, color, type, price)
    AND
    (NOT(model1=model4) AND NOT(model2=model4) AND NOT(model3=model4))
)


Find those makers that manufacture every type of printer. Do not rely on the fact that there are only two types of printers in the given instance.

Printer(model:int, color:int, type:string, price:int)

(EXISTS m1, c1. Product(maker, m1, c1)) --Der findes en maker
AND ( 
    FORALL m2, k2, k3, type. ( --For loop over alle printere i hele verden (i domain)
        NOT Printer(m2, k2, type, k3) -- Hvis printeren ikke fines, så er det sandt (og det skal være sandt for alle i forall), så det her bliver sandt for alt der ikke findes i printer tabellen
    OR (
        EXISTS m1, c1, c2, c3. Product(maker, m1, c1) 
        AND 
        Printer(m1, c2, type, c3) --> Hvis printeren i tabellen 
--> Så skal den type være lavet af makeren, Intersect på type i Printer og product
        )
    )
)





(EXISTS prodtype, model1. Product(maker, model1, prodtype))
AND ( 
    FORALL model2, color1, price1, type. ( 
        NOT Printer(model2, color1, type, price1) 
    OR (
        EXISTS model1, prodtype, color2, price2. 
            Product(maker, model1, prodtype) 
            AND 
            Printer(model1, color2, type, price2)  
        )
    )
)

k)
-- Validate that the “type” column in Product is correct, i.e., only includes correct labels for PCs,
-- Laptops, and Printers with the respective model number. Your query should be a closed formula
-- that outputs the empty set if and only if the correctness is violated.

(FORALL maker, model, type. Product(maker, model, type)) 
AND (
    
)
