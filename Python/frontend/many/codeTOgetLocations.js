///downloadObjectAsJson(getUnique(mylocs,'label'),"locsNew27")
/*

downloadObjectAsJson(getUnique(mylocs,'label'),"filteredLabels")
function downloadObjectAsJson(exportObj, exportName) {
    var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportObj));
    var downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", exportName + ".json");
    document.body.appendChild(downloadAnchorNode); // required for firefox
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
}

*/

function checkIfLocationExists(label){
exists=false;
    $.each(mylocs, function(index, loc) {
        if(label==loc.label)
            exists=true;
    })
   return exists
}
function getUnique(arr, comp) {

  const unique = arr
       .map(e => e[comp])

     // store the keys of the unique objects
    .map((e, i, final) => final.indexOf(e) === i && i)

    // eliminate the dead keys & store unique objects
    .filter(e => arr[e]).map(e => arr[e]);

   return unique;
}

function spr(llla) {
    var xhr = new XMLHttpRequest(),
        method = "GET";
    url = llla;

    xhr.open(method, url, true);

    xhr.onreadystatechange = function() {

        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                toAllay(JSON.parse(xhr.responseText))


            }
        }

    };
    xhr.send();

}

var stps = []
var stps2 = []
function toAllay(w) {
    let myArr = w;
    let ll = myArr.workOpportunities;
    $.each(ll, function(index, singleload) {
        var new_load_id = singleload.id + singleload.version + singleload.payout.value;
        loads = singleload["loads"]
        $.each(loads, function(index, load) {
            stops = load["stops"]
            $.each(stops, function(index, stoppp) {
                loc = stoppp.location;
                str = loc.label + loc.state + loc.city + loc.longitude + loc.latitude;
                if(!stps[loc.label] && checkIfLocationExists(loc.label)){
                    stps[loc.label]=true;
                    stps2.push(loc)
                    mylocs.push(loc)
                    console.log("new location: "+ loc.label)
                }
                
                //console.log(str)



            })
        })


    });




}


function downloadObjectAsJson(exportObj, exportName) {
    var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportObj));
    var downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", exportName + ".json");
    document.body.appendChild(downloadAnchorNode); // required for firefox
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
}


// for(i=0;i<10;i++){
//     spr("https://relay.amazon.com/api/tours/loadboard?sortByField=startTime&sortOrder=asc&nextItemToken="+(i*100)+"&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId=&auditContextMap={%22rlbChannel%22:%22EXACT_MATCH%22,%22isOriginCityLive%22:%22false%22,%22isDestinationCityLive%22:%22false%22}")

// }


