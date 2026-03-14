function doGet(e){

var sheet = SpreadsheetApp.getActiveSpreadsheet();

var health = sheet.getSheetByName("HealthData");
var alerts = sheet.getSheetByName("Alerts");

var name = e.parameter.name;
var age = e.parameter.age;
var temp = e.parameter.temp;
var heart = e.parameter.heart;
var alert = e.parameter.alert;

health.appendRow([
name,
age,
new Date(),
temp,
heart
]);

if(alert=="1"){
alerts.appendRow([
name,
new Date()
]);
}

return ContentService.createTextOutput("done");

}
