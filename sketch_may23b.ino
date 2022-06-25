#include <WiFi.h>


const char* ssid = "";
const char* password =  "";

WiFiServer wifiServer(80);


#define DT 19
#define SCK 18

int readCount(){
  int i=0;
  int Count=0;
  pinMode(DT, OUTPUT);
  pinMode(SCK, OUTPUT);
  digitalWrite(DT,1);
  digitalWrite(SCK,0);
  pinMode(DT, INPUT);

  while(digitalRead(DT) == 1){
      i=0;
  }
  for(i=0;i<24;i++){
        digitalWrite(SCK,1);
        Count=Count<<1;

        digitalWrite(SCK,0);
        
        if(digitalRead(DT) == 0) 
            Count=Count+1;
  }
        
  digitalWrite(SCK,1);
  Count=Count^0x800000;
  digitalWrite(SCK,0);
  return Count;
}


int sample = readCount();

void setup() {

  Serial.begin(115200);

  delay(1000);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }

  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());

  wifiServer.begin();
}

void loop() {

  WiFiClient client = wifiServer.available();
  char buf[10];
  
  if (client) {

    while (client.connected()) {
        int count = readCount();
        int w = 0;
        w = (count-sample)/100;
        Serial.println(w);
        client.write(itoa(w, buf, 10));

        delay(500);
        
      
      
    }
    
      client.stop();

    }
    
}

  
