#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

String patients[10] = {
"Aarav Sharma",
"Diya Patel",
"Rohan Verma",
"Ananya Reddy",
"Vikram Singh",
"Meera Nair",
"Rahul Das",
"Kavya Iyer",
"Arjun Mehta",
"Sneha Kulkarni"
};

void setup() {

Serial.begin(115200);

WiFi.begin(ssid,password);

while(WiFi.status()!=WL_CONNECTED){
delay(500);
Serial.print(".");
}

Serial.println("WiFi connected");

client.setServer(mqtt_server,1883);

}

void reconnect(){

while(!client.connected()){
client.connect("healthband_real_esp32");
}

}

void loop(){

if(!client.connected()){
reconnect();
}

client.loop();

for(int i=0;i<10;i++){

int heart=random(60,140);
float temp=random(360,380)/10.0;

String payload="{\"name\":\""+patients[i]+"\",\"heart_rate\":"+String(heart)+",\"temperature\":"+String(temp)+"}";

client.publish("healthband/data",payload.c_str());

Serial.println(payload);

delay(1000);

}

}
