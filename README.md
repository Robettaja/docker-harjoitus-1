# Docker harjoitus 1

Molemmat client ja server ovat toteutettu pythonilla

## Imageiden buildaus
```
docker build -t docker1-server .
docker build -t docker1-client .
``` 

## Verkon luonti
```
docker network create docker1-network
```

## Palvelin kontin muodostus
```
docker run -d --name server --network docker1-network --volume "$(pwd)/serverdata:/serverdata" docker1-server --port 8001
```

## Asiakas kontin muodostus
```
docker run -d --name client --network docker1-network --volume "$(pwd)/clientdata:/clientdata" docker1-client http://server:8001
```

## Checksum tarkistus
```
docker logs client
```

Lopputuloksena docker luo serverdata tai clientdata hakemistot sinne mistä docker run suoritettiin. Näistä hakemistoista löytyy halutut tiedostot
