CREATE TABLE predios(
codigo INT NOT NULL PRIMARY KEY, 
area INT NOT NULL,
latitud INT NOT NULL,
longitud INT NOT NULL,
terreno ENUM ('Planicie',
'Ladera', 'Cenagoso','Desertico') NOT NULL, 
imagen VARCHAR(200) NOT NULL
 );  
 
