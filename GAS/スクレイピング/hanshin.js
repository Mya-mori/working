function getRaceFromCalendar() {

    //スプレッドシートのIDを指定
const spreadsheet = SpreadsheetApp.openById("1063RRv01SkSlZyshNmSA7Jwxua3w9_W83q20R5NUePg")

 //スプレッドシートのシート名を指定
const sheet = spreadsheet.getSheetByName('シート1')

  //最後の行に追記する設定
let lastrow = sheet.getLastRow();
let targetrow = lastrow + 1;
var response = UrlFetchApp.fetch("https://baseball.yahoo.co.jp/npb/teams/5/");
var content = response.getContentText("UTF-8");
var venues = Parser.data(content).from('class="sn-list__itemTitle"').to('</p>').iterate();
////////
for (var index = 0; index < venues.length; index++) {
    var venue = venues[index];
    sheet.getRange("A" + targetrow).setValue(venue);
    targetrow ++
    }
}