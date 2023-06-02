# Air pollution mqtt-kafka demo app

Demo aplikacija da nam pokazaze kako da povezemo mqtt i kafku. Citamo podatke sa public api-ja za zagadjenost vazduha, onda te podatke publishujemo preko mqtt, a kafka bridge se subscribuje na taj topic i prima podatke. Dalje podaci mogu biti preuzeti od strane drugih podsistema (od bekenda na primer za odredjene stvari, big data...)


Kako pokrenuti aplikaciju:
1. Startuj zookeeper:
    - udji u folder gde je kafka instalirana i pokreni prvo komande za startovanje zookeepera, i to bi onda ovako trebalo da izgleda u terminalu

![image](https://github.com/pilac96/air-pollution-mqtt-kafka-demo/assets/35148018/eb87e6be-7adb-4092-a38d-ae9771bc71fd)

2. Startuj kafka server:
    - takodje udji u folder gde je kafka instalirana i pokreni komande za startovanje kafke, i to bi onda ovako trebalo da izgleda u terminalu

![image](https://github.com/pilac96/air-pollution-mqtt-kafka-demo/assets/35148018/076340f7-9c5a-4f7f-b7f9-b6054246c45a)

4. Pokreni mqtt_kafka_bridge.py i to ovako treba da izgleda

![image](https://github.com/pilac96/air-pollution-mqtt-kafka-demo/assets/35148018/7f29029c-a617-4ad5-85e8-ff2bfb3074f5)


5. Zatim pokreni air_pollution_app.py, i aplikacija ce se startovati, i to treba ovako da izgleda
6. 
![image](https://github.com/pilac96/air-pollution-mqtt-kafka-demo/assets/35148018/9e2e2677-8511-4d00-a8a8-da398844a604)

6. Sada ce terminal od mqtt_kafka_bridge.py izgledati ovako:
7. 
![image](https://github.com/pilac96/air-pollution-mqtt-kafka-demo/assets/35148018/d7981bcf-ec46-43e9-921e-5e8053953651)
