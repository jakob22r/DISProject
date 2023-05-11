CREATE TABLE Resturants
    (rID CHAR(20),
    rArea CHAR(50),
    rName CHAR(50),
    rPassword CHAR(20),
    PRIMARY KEY (rID))

CREATE TABLE Customers
    (cID CHAR(20),
    customerName CHAR(50),
    cArea CHAR(50),
    cPassword CHAR(20),
    PRIMARY KEY (cID))

CREATE TABLE Couriers
    (corID CHAR(20)
    couriersName CHAR(50),
    corArea CHAR(50),
    corPassword CHAR(20),
    PRIMARY KEY (corID))

CREATE TABLE Orders
    (orderID CHAR(20),
    cID CHAR(20),
    PRIMARY KEY (orderID, cID),
    FOREIGN KEY (cID) REFERENCES Customers)

CREATE TABLE PartlyOrder_BelongTo
    (orderID CHAR(20),
    rID CHAR(20),
    status INTEGER,
    PRIMARY KEY (orderID, rID),
    FOREIGN KEY (orderID) REFERENCES Orders ON DELETE CASCADE,
    FOREIGN KEY (rID) REFERENCES Resturants)

CREATE TABLE TakeOut
    (orderID CHAR(20),
    rID CHAR(20),
    PRIMARY KEY (orderID, rID),
    FOREIGN KEY (orderID, rID) REFERENCES PartlyOrder_BelongTo)

CREATE TABLE Delevery
    (orderID CHAR(20),
    rID CHAR(20),
    corID CHAR(20),
    PRIMARY KEY (orderID, rID, corID),
    FOREIGN KEY (orderID, rID) REFERENCES PartlyOrder_BelongTo,
    FOREIGN KEY (corID) REFERENCES Couriers)

CREATE TABLE Cuisines
    (cuisineName CHAR(50),
    PRIMARY KEY (cuisineName))

CREATE TABLE Prefers
    (cID CHAR(20),
    cuisineName CHAR(50),
    PRIMARY KEY (cID, cuisineName),
    FOREIGN KEY (cID) REFERENCES Customers,
    FOREIGN KEY (cuisine) REFERENCES Cuisines)

CREATE TABLE Offers
    (cuisineName CHAR(50),
    rID CHAR(20),
    PRIMARY KEY (cuisineName, rID),
    FOREIGN KEY (rID) REFERENCES Resturants,
    FOREIGN KEY (cuisineName) REFERENCES Cuisines)

CREATE TABLE RatesResurants
    (rating CHAR(50),
    like INTEGER,
    cID CHAR(20),
    rID CHAR(20),
    customerName CHAR(50) REFERENCES Customers,
    rName CHAR(50) REFERENCES Resturants,
    PRIMARY KEY (cID, rID, rating, likeDislike),
    FOREIGN KEY (cID) REFERENCES Customers,
    FOREIGN KEY (rID) REFERENCES Resturants)

CREATE TABLE TagsResturants
    (tag INTEGER,
    cID CHAR(20),
    rID CHAR(20),
    customerName CHAR(50) REFERENCES Customers,
    rName CHAR(50) REFERENCES Resturants,
    PRIMARY KEY (cID, rID, tag),
    FOREIGN KEY (cID) REFERENCES Customers,
    FOREIGN KEY (rID) REFERENCES Resturants)

CREATE TABLE RatesCouriers
    (rating CHAR(50),
    cID CHAR(20),
    corID CHAR(20),
    like INTEGER,
    PRIMARY KEY (cID, corID, rating),
    FOREIGN KEY (cID) REFERENCES Customers,
    FOREIGN KEY (corID) REFERENCES Couriers)

CREATE TABLE Dishes
    (dishName CHAR(50),
    PRIMARY KEY (dishName))

CREATE TABLE ConsistOf
    (orderID CHAR(20),
    rID CHAR(20),
    dishName CHAR(50),
    PRIMARY KEY (orderID, rID, dishName),
    FOREIGN KEY (orderID) REFERENCES Orders,
    FOREIGN KEY (rID) REFERENCES Resturants,
    FOREIGN KEY (dishName) REFERENCES Dishes)

CREATE TABLE PrefersToUse
    (corID CHAR(20),
    rID CHAR(20),
    tag INTEGER,
    PRIMARY KEY (corID, rID),
    FOREIGN KEY (corID) REFERENCES Couriers,
    FOREIGN KEY (rID) REFERENCES Resturants)

CREATE TABLE PrefersToDeliverFor
    (corID CHAR(20),
    rID CHAR(20),
    tag INTEGER,
    PRIMARY KEY (corID, rID),
    FOREIGN KEY (corID) REFERENCES Couriers,
    FOREIGN KEY (rID) REFERENCES Resturants)
