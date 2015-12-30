var request = require('request')
var util = require('util')

var accessToken = "CAACEdEose0cBAB24efZC4m1xEPzpXZA8IkBlxYXaFN7zpQqFzTmmM8vikwAWhIcGHvOCHSprWx2bH4FCQesFYTdSRSEU2uk7OOExFEv2mt164nj38hwYyufK5Tp8obTxoZCrKPTW1tsRxlwwqLLxqmNWqxitlW5PjTRRL5KpN3YSDXDZCZBX0Cb0IygxmOWAN0a1qDVIhxwZDZD"
var eventId = 1576427339262530
var option = "attending" //TODO create list of possible choices
var limit = 1000
var url = util.format("https://graph.facebook.com/v2.5/%s/%s?access_token=%s&pretty=0&limit=%s", eventId, option, accessToken, limit )


// var a = "a"
// var b = "b"
// if (a == b) {console.log("TAK\n")}
// a = "b"
// if (a == b) {console.log("TAK\n")}
// a = b
// if (a == b) {console.log("TAK\n")}

function f() { 
    console.log("WAITING\n")
}

while(purl != url) {
    console.log(url)
    if(url!="")
    {
        request({
            url: url,
            json: true
        }, function (error, response, body) {
            if (!error && response.statusCode === 200) {
                // console.log("DATA\n")
                // console.log(body.data)
                console.log("NEXT\n")
                console.log(body.paging.next)
                purl = url
                url = body.paging.next
            }
        })
    }
}
