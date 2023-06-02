import paho.mqtt.client as mqtt

mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_client = mqtt.Client("MQTTPublisher")
mqtt_client.connect(mqtt_broker)


def publish(topic, message):
    mqtt_client.publish(topic, message)
    print("MQTT: Just published {} to topic {}".format(message, topic))
